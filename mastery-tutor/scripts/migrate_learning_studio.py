#!/usr/bin/env python3

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


TARGET_SCHEMA = 2
STUDIO_TYPE = "mastery-tutor"
MARKER_CONTENT = f"schema_version: {TARGET_SCHEMA}\nstudio_type: {STUDIO_TYPE}\n"
REQUIRED_STUDIO_PATHS = (
    Path("AGENTS.md"),
    Path("learner/profile.md"),
    Path("courses/index.md"),
    Path("courses/_template/course.md"),
    Path("courses/_template/progress.md"),
)
COURSE_STATUSES = {
    "planned",
    "active",
    "paused",
    "completed-with-mastery",
    "completed-with-gaps",
    "archived",
}
OLD_EVIDENCE_HEADER = (
    "Concept ID",
    "Status",
    "Evidence",
    "Conditions",
    "Date",
)
NEW_EVIDENCE_HEADER = (
    "Date",
    "Capability ID",
    "Task or artifact",
    "Conditions and support",
    "Observed evidence",
    "Status",
    "Uncertainty",
    "Next retrieval",
)


class MigrationError(Exception):
    pass


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Migrate a Mastery Tutor learning studio to schema 2.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and preview the migration without changing any files.",
    )
    parser.add_argument(
        "--backup-dir",
        type=Path,
        help="Required for a real migration; must name a path that does not exist.",
    )
    parser.add_argument("studio", type=Path)
    return parser.parse_args()


def normalize_path(path: Path) -> Path:
    absolute = Path(os.path.abspath(path.expanduser()))
    return absolute.parent.resolve() / absolute.name


def parse_marker(content: str) -> tuple[int, str]:
    values: dict[str, str] = {}
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise MigrationError("Malformed learning-studio.yaml metadata.")
        key, value = line.split(":", 1)
        normalized_key = key.strip()
        if normalized_key in values:
            raise MigrationError("Malformed learning-studio.yaml metadata.")
        values[normalized_key] = value.strip()

    try:
        schema = int(values["schema_version"])
        studio_type = values["studio_type"]
    except (KeyError, ValueError) as error:
        raise MigrationError("Malformed learning-studio.yaml metadata.") from error
    return schema, studio_type


def detect_schema(studio: Path) -> int | None:
    marker = studio / "learning-studio.yaml"
    if not marker.exists():
        return None
    if not marker.is_file() or marker.is_symlink():
        raise MigrationError("learning-studio.yaml must be a regular file.")

    schema, studio_type = parse_marker(marker.read_text())
    if studio_type != STUDIO_TYPE:
        raise MigrationError(
            f"Unsupported studio type {studio_type!r}; expected {STUDIO_TYPE!r}.",
        )
    if schema > TARGET_SCHEMA:
        raise MigrationError(
            f"Studio schema {schema} is newer than supported schema {TARGET_SCHEMA}.",
        )
    if schema not in {1, TARGET_SCHEMA}:
        raise MigrationError(f"Unsupported studio schema {schema}.")
    return schema


def validate_studio(studio: Path) -> None:
    if studio.is_symlink():
        raise MigrationError(f"Refusing to migrate through a symlink: {studio}")
    if not studio.is_dir():
        raise MigrationError(f"Learning studio is not a directory: {studio}")

    missing = [
        path.as_posix()
        for path in REQUIRED_STUDIO_PATHS
        if not (studio / path).is_file() or (studio / path).is_symlink()
    ]
    if missing:
        raise MigrationError(
            "Directory does not have the required learning-studio structure; "
            f"missing regular files: {', '.join(missing)}",
        )


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        raise MigrationError(f"Unsupported Markdown table row: {line}")

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for character in stripped[1:-1]:
        if character == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
        escaped = character == "\\" and not escaped
        if character != "\\":
            escaped = False
    cells.append("".join(current).strip())
    return cells


def markdown_row(cells: tuple[str, ...] | list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def migrate_evidence_ledger(content: str, relative_path: Path) -> str:
    lines = content.splitlines()
    headings = [index for index, line in enumerate(lines) if line == "## Evidence Ledger"]
    if len(headings) != 1:
        raise MigrationError(
            f"Expected one Evidence Ledger section in {relative_path.as_posix()}.",
        )

    cursor = headings[0] + 1
    while cursor < len(lines) and not lines[cursor].strip():
        cursor += 1
    if cursor >= len(lines):
        raise MigrationError(f"Missing evidence table in {relative_path.as_posix()}.")

    header_index = cursor
    header = tuple(split_markdown_row(lines[header_index]))
    if header not in {OLD_EVIDENCE_HEADER, NEW_EVIDENCE_HEADER}:
        raise MigrationError(
            f"Unrecognized evidence ledger columns in {relative_path.as_posix()}; "
            "manual review is required.",
        )

    expected_columns = len(header)
    separator_index = header_index + 1
    if separator_index >= len(lines):
        raise MigrationError(
            f"Missing evidence table separator in {relative_path.as_posix()}.",
        )
    separator = split_markdown_row(lines[separator_index])
    if len(separator) != expected_columns or any(
        not re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        raise MigrationError(
            f"Unrecognized evidence table separator in {relative_path.as_posix()}.",
        )

    row_end = separator_index + 1
    migrated_rows: list[str] = []
    while row_end < len(lines) and lines[row_end].strip().startswith("|"):
        cells = split_markdown_row(lines[row_end])
        if len(cells) != expected_columns:
            raise MigrationError(
                f"Unrecognized evidence row in {relative_path.as_posix()} at line {row_end + 1}.",
            )
        if header == OLD_EVIDENCE_HEADER:
            concept_id, status, evidence, conditions, date = cells
            migrated_rows.append(
                markdown_row(
                    [date, concept_id, "", conditions, evidence, status, "", ""],
                ),
            )
        row_end += 1

    if header == NEW_EVIDENCE_HEADER:
        return content

    replacement = [
        markdown_row(NEW_EVIDENCE_HEADER),
        markdown_row(tuple("---" for _ in NEW_EVIDENCE_HEADER)),
        *migrated_rows,
    ]
    lines[header_index:row_end] = replacement
    migrated = "\n".join(lines)
    if content.endswith("\n"):
        migrated += "\n"
    return migrated


def read_course_status(content: str, relative_path: Path) -> str:
    matches = re.findall(r"(?m)^- Status:\s*`?([^`\n]+?)`?\s*$", content)
    if len(matches) != 1:
        raise MigrationError(
            f"Expected one course Status field in {relative_path.as_posix()}.",
        )
    status = matches[0].strip()
    if status == "completed":
        raise MigrationError(
            f"Ambiguous completed status in {relative_path.as_posix()}; choose "
            "completed-with-mastery or completed-with-gaps before migrating.",
        )
    if status not in COURSE_STATUSES:
        raise MigrationError(
            f"Unsupported course status {status!r} in {relative_path.as_posix()}.",
        )
    return status


def lifecycle_sections(status: str, *, template: bool) -> str:
    if template:
        enrolled = "`[YYYY-MM-DD or not enrolled]`"
        started = "`[YYYY-MM-DD or not started]`"
        completed = "`[YYYY-MM-DD or not completed]`"
        archived = "`[YYYY-MM-DD or not archived]`"
        path_completed = "[yes or no]"
        mastery_outcome = "[pending, demonstrated, or completed with gaps]"
        gaps = "[Unresolved core capabilities, or none]"
        follow_up = "[Maintenance, remediation, next course, or none]"
        transition = "| [YYYY-MM-DD] | [Previous status] | [New status] | [Evidence or reason] |"
    else:
        enrolled = "unknown (predates schema 2)"
        started = "unknown (predates schema 2)"
        completed = (
            "unknown (predates schema 2)"
            if status.startswith("completed-with-")
            else "not completed"
        )
        archived = "unknown (predates schema 2)" if status == "archived" else "not archived"
        if status == "completed-with-mastery":
            path_completed = "yes"
            mastery_outcome = "demonstrated"
            gaps = "none recorded"
            follow_up = "maintenance or a new learning goal"
        elif status == "completed-with-gaps":
            path_completed = "yes"
            mastery_outcome = "completed with gaps"
            gaps = "see the roadmap and progress ledger"
            follow_up = "address unresolved core capabilities"
        elif status == "archived":
            path_completed = "unknown"
            mastery_outcome = "unknown"
            gaps = "review before resuming"
            follow_up = "none while archived"
        else:
            path_completed = "no"
            mastery_outcome = "pending"
            gaps = "pending assessment"
            follow_up = "continue from progress.md"
        transition = (
            f"| unknown | unknown | {status} | Schema 2 migration recorded the existing "
            "status; earlier transitions were not inferred. |"
        )

    return (
        "## Course Lifecycle\n\n"
        f"- Enrolled: {enrolled}\n"
        f"- Started: {started}\n"
        f"- Completed: {completed}\n"
        f"- Archived: {archived}\n\n"
        "| Date | From | To | Evidence or reason |\n"
        "| --- | --- | --- | --- |\n"
        f"{transition}\n\n"
        "## Completion Record\n\n"
        f"- Learning path completed: {path_completed}\n"
        f"- Mastery outcome: {mastery_outcome}\n"
        f"- Remaining gaps: {gaps}\n"
        f"- Follow-up: {follow_up}\n"
    )


def migrate_course(content: str, relative_path: Path) -> str:
    status = read_course_status(content, relative_path)
    lifecycle_count = content.count("## Course Lifecycle")
    completion_count = content.count("## Completion Record")
    if lifecycle_count not in {0, 1} or completion_count not in {0, 1}:
        raise MigrationError(
            f"Duplicate schema 2 lifecycle sections in {relative_path.as_posix()}; "
            "manual review is required.",
        )
    if lifecycle_count != completion_count:
        raise MigrationError(
            f"Partial schema 2 lifecycle sections in {relative_path.as_posix()}; "
            "manual review is required.",
        )
    if lifecycle_count == 1:
        return content

    migrated = content.rstrip() + "\n\n"
    migrated += lifecycle_sections(status, template=relative_path.parts[-2] == "_template")
    return migrated


def migrate_index(content: str) -> str:
    for line in content.splitlines():
        if not line.strip().startswith("|") or not line.strip().endswith("|"):
            continue
        cells = split_markdown_row(line)
        if any(cell.strip("`").strip() == "completed" for cell in cells):
            raise MigrationError(
                "Ambiguous completed status in courses/index.md; choose "
                "completed-with-mastery or completed-with-gaps before migrating.",
            )

    old_pattern = re.compile(r"(?m)^- `?completed`?:[^\n]*$")
    old_matches = old_pattern.findall(content)
    has_mastery = bool(re.search(r"(?m)^- `?completed-with-mastery`?:", content))
    has_gaps = bool(re.search(r"(?m)^- `?completed-with-gaps`?:", content))

    if has_mastery and has_gaps and not old_matches:
        return content
    if len(old_matches) != 1 or has_mastery or has_gaps:
        raise MigrationError(
            "Unrecognized completion status vocabulary in courses/index.md; "
            "manual review is required.",
        )

    replacement = (
        "- `completed-with-mastery`: learning path ended and completion criteria "
        "were demonstrated independently\n"
        "- `completed-with-gaps`: learning path ended with unresolved core capabilities recorded"
    )
    return old_pattern.sub(replacement, content, count=1)


def collect_course_directories(studio: Path) -> list[Path]:
    courses_root = studio / "courses"
    directories: list[Path] = []
    for path in courses_root.iterdir():
        if path.is_symlink():
            raise MigrationError(
                f"Refusing symlink in courses directory: {path.relative_to(studio).as_posix()}.",
            )
        if path.is_dir():
            directories.append(path)
    for directory in directories:
        for filename in ("course.md", "progress.md"):
            path = directory / filename
            if not path.is_file() or path.is_symlink():
                raise MigrationError(
                    f"Course directory {directory.relative_to(studio).as_posix()} "
                    f"is missing regular file {filename}.",
                )
    return sorted(directories, key=lambda path: path.as_posix())


def build_changes(studio: Path) -> tuple[int | None, dict[Path, bytes], dict[Path, bytes | None]]:
    validate_studio(studio)
    source_schema = detect_schema(studio)

    originals: dict[Path, bytes | None] = {}
    changes: dict[Path, bytes] = {}

    def plan(relative_path: Path, transformed: str) -> None:
        target = studio / relative_path
        original = target.read_bytes() if target.exists() else None
        encoded = transformed.encode()
        originals[relative_path] = original
        if original != encoded:
            changes[relative_path] = encoded

    plan(Path("learning-studio.yaml"), MARKER_CONTENT)

    index_path = Path("courses/index.md")
    plan(index_path, migrate_index((studio / index_path).read_text()))

    for course_directory in collect_course_directories(studio):
        relative_directory = course_directory.relative_to(studio)
        course_path = relative_directory / "course.md"
        progress_path = relative_directory / "progress.md"
        plan(course_path, migrate_course((studio / course_path).read_text(), course_path))
        plan(
            progress_path,
            migrate_evidence_ledger((studio / progress_path).read_text(), progress_path),
        )

    if source_schema == TARGET_SCHEMA:
        if changes:
            changed_paths = ", ".join(
                sorted(path.as_posix() for path in changes),
            )
            raise MigrationError(
                f"Studio claims schema {TARGET_SCHEMA}, but these files still require "
                f"migration: {changed_paths}.",
            )
        return source_schema, {}, originals

    return source_schema, changes, originals


def ensure_unchanged(studio: Path, originals: dict[Path, bytes | None]) -> None:
    for relative_path, original in originals.items():
        target = studio / relative_path
        current = target.read_bytes() if target.exists() else None
        if current != original:
            raise MigrationError(
                f"Studio changed while preparing migration: {relative_path.as_posix()}.",
            )


def create_backup(
    studio: Path,
    backup: Path,
    source_schema: int | None,
    changes: dict[Path, bytes],
    originals: dict[Path, bytes | None],
) -> None:
    if backup.exists() or backup.is_symlink():
        raise MigrationError(f"Backup destination already exists: {backup}")
    if backup == studio or studio in backup.parents:
        raise MigrationError("Backup directory must be outside the learning studio.")

    backup.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".mastery-tutor-backup-",
        dir=backup.parent,
    ) as temporary_directory:
        staging = Path(temporary_directory) / "backup"
        staging.mkdir()
        for relative_path in changes:
            if originals[relative_path] is None:
                continue
            source = studio / relative_path
            target = staging / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

        manifest = {
            "migration": "mastery-tutor-learning-studio",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "studio": str(studio),
            "from_schema": source_schema,
            "to_schema": TARGET_SCHEMA,
            "changed_files": sorted(path.as_posix() for path in changes),
            "created_files": sorted(
                path.as_posix()
                for path in changes
                if originals[path] is None
            ),
        }
        (staging / "migration-manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
        )
        os.replace(staging, backup)


def atomic_write(target: Path, content: bytes) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.",
        dir=target.parent,
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as temporary_file:
            temporary_file.write(content)
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
        if target.exists():
            shutil.copymode(target, temporary)
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()


def apply_changes(
    studio: Path,
    changes: dict[Path, bytes],
    originals: dict[Path, bytes | None],
) -> None:
    attempted: list[Path] = []
    try:
        for relative_path in sorted(changes, key=Path.as_posix):
            attempted.append(relative_path)
            atomic_write(studio / relative_path, changes[relative_path])
    except Exception:
        for relative_path in reversed(attempted):
            target = studio / relative_path
            original = originals[relative_path]
            if original is None:
                if target.exists() or target.is_symlink():
                    target.unlink()
            else:
                atomic_write(target, original)
        raise


def source_label(schema: int | None) -> str:
    return "unversioned" if schema is None else f"schema {schema}"


def migrate(studio: Path, *, dry_run: bool, backup: Path | None) -> None:
    source_schema, changes, originals = build_changes(studio)
    if not changes:
        print(f"Learning studio already uses schema {TARGET_SCHEMA}: {studio}")
        return

    print(
        f"{'Would migrate' if dry_run else 'Migrating'} {studio} "
        f"from {source_label(source_schema)} to schema {TARGET_SCHEMA}",
    )
    for relative_path in sorted(changes, key=Path.as_posix):
        action = "create" if originals[relative_path] is None else "update"
        print(f"  {action} {relative_path.as_posix()}")

    if dry_run:
        print("Dry run complete; no files changed.")
        return
    if backup is None:
        raise MigrationError("A real migration requires --backup-dir.")

    ensure_unchanged(studio, originals)
    create_backup(studio, backup, source_schema, changes, originals)
    ensure_unchanged(studio, originals)
    apply_changes(studio, changes, originals)
    print(f"Migrated learning studio to schema {TARGET_SCHEMA}: {studio}")
    print(f"Backup created at {backup}")


def main() -> int:
    arguments = parse_arguments()
    try:
        migrate(
            normalize_path(arguments.studio),
            dry_run=arguments.dry_run,
            backup=(
                normalize_path(arguments.backup_dir)
                if arguments.backup_dir is not None
                else None
            ),
        )
    except MigrationError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    except (OSError, UnicodeError) as error:
        print(f"error: migration failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
