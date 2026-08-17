#!/usr/bin/env python3

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Iterable


EMPTY_DIRECTORIES = (
    Path("courses/_template/artifacts"),
    Path("courses/_template/lessons"),
)
ALLOWED_EXISTING_NAMES = {".git"}


class InitializationError(Exception):
    pass


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a new Mastery Tutor learning studio.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the planned files without creating them.",
    )
    parser.add_argument(
        "--link-skill",
        action="store_true",
        help="Link this skill into .agents/skills/mastery-tutor.",
    )
    parser.add_argument("destination", type=Path)
    return parser.parse_args()


def collect_sources(skill_root: Path) -> list[tuple[Path, Path]]:
    template_root = skill_root / "assets/studio-template"
    syllabus_source = skill_root / "assets/course-template/syllabus.md"

    if not template_root.is_dir():
        raise InitializationError(f"Missing studio template: {template_root}")
    if not syllabus_source.is_file():
        raise InitializationError(f"Missing syllabus template: {syllabus_source}")

    sources = [
        (source, source.relative_to(template_root))
        for source in template_root.rglob("*")
        if source.is_file()
    ]
    sources.append(
        (syllabus_source, Path("courses/_template/syllabus.md")),
    )
    return sorted(sources, key=lambda item: item[1].as_posix())


def validate_destination(destination: Path) -> None:
    if destination.is_symlink():
        raise InitializationError(
            f"Refusing to initialize through a symlink: {destination}",
        )
    if not destination.exists():
        return
    if not destination.is_dir():
        raise InitializationError(
            f"Refusing to initialize a non-directory: {destination}",
        )

    unexpected_names = sorted(
        entry.name
        for entry in destination.iterdir()
        if entry.name not in ALLOWED_EXISTING_NAMES
    )
    if unexpected_names:
        preview = ", ".join(unexpected_names[:5])
        if len(unexpected_names) > 5:
            preview += ", ..."
        raise InitializationError(
            f"Refusing to initialize non-empty destination {destination}: {preview}",
        )


def normalize_destination(destination: Path) -> Path:
    absolute = Path(os.path.abspath(destination.expanduser()))
    return absolute.parent.resolve() / absolute.name


def planned_paths(
    sources: Iterable[tuple[Path, Path]],
    link_skill: bool,
) -> list[Path]:
    paths = [relative_path for _, relative_path in sources]
    paths.extend(EMPTY_DIRECTORIES)
    if link_skill:
        paths.append(Path(".agents/skills/mastery-tutor"))
    return sorted(set(paths), key=Path.as_posix)


def print_plan(destination: Path, paths: Iterable[Path]) -> None:
    print(f"Would initialize learning studio at {destination}")
    for relative_path in paths:
        print(f"  create {relative_path.as_posix()}")


def prepare_staging_directory(
    staging: Path,
    skill_root: Path,
    sources: Iterable[tuple[Path, Path]],
    link_skill: bool,
) -> None:
    staging.mkdir()
    for source, relative_path in sources:
        target = staging / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    for relative_path in EMPTY_DIRECTORIES:
        (staging / relative_path).mkdir(parents=True, exist_ok=True)

    if link_skill:
        skill_link = staging / ".agents/skills/mastery-tutor"
        skill_link.parent.mkdir(parents=True, exist_ok=True)
        skill_link.symlink_to(skill_root, target_is_directory=True)


def install_staging_directory(staging: Path, destination: Path) -> None:
    validate_destination(destination)
    if not destination.exists():
        os.replace(staging, destination)
        return

    moved_targets: list[Path] = []
    try:
        for source in sorted(staging.iterdir(), key=lambda path: path.name):
            target = destination / source.name
            if target.exists() or target.is_symlink():
                raise InitializationError(
                    f"Refusing to replace existing path: {target}",
                )
            os.replace(source, target)
            moved_targets.append(target)
    except Exception:
        for target in reversed(moved_targets):
            os.replace(target, staging / target.name)
        raise


def initialize(destination: Path, *, dry_run: bool, link_skill: bool) -> None:
    skill_root = Path(__file__).resolve().parents[1]
    sources = collect_sources(skill_root)
    validate_destination(destination)

    paths = planned_paths(sources, link_skill)
    if dry_run:
        print_plan(destination, paths)
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".mastery-tutor-studio-",
        dir=destination.parent,
    ) as temporary_directory:
        staging = Path(temporary_directory) / "studio"
        prepare_staging_directory(staging, skill_root, sources, link_skill)
        install_staging_directory(staging, destination)

    print(f"Initialized learning studio at {destination}")


def main() -> int:
    arguments = parse_arguments()
    try:
        initialize(
            normalize_destination(arguments.destination),
            dry_run=arguments.dry_run,
            link_skill=arguments.link_skill,
        )
    except InitializationError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"error: initialization failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
