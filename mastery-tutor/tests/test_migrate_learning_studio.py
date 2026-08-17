#!/usr/bin/env python3

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
MIGRATOR = SKILL_ROOT / "scripts" / "migrate_learning_studio.py"


class MigrateLearningStudioTest(unittest.TestCase):
    def run_migrator(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(MIGRATOR), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def create_schema_one_studio(self, root: Path) -> None:
        files = {
            "learning-studio.yaml": "schema_version: 1\nstudio_type: mastery-tutor\n",
            "AGENTS.md": "# Learning Studio\n",
            "learner/profile.md": "# Learner Profile\n",
            "courses/index.md": (
                "# Course Index\n\n"
                "## Status Vocabulary\n\n"
                "- planned: designed but not started\n"
                "- active: currently taught\n"
                "- paused: intentionally suspended\n"
                "- completed: completion evidence accepted\n"
                "- archived: retained for reference\n\n"
                "| Course | Status | Last activity | Next action |\n"
                "| --- | --- | --- | --- |\n"
                "| example | active | 2026-08-17 | Continue |\n"
            ),
            "courses/_template/course.md": (
                "# Course Contract\n\n"
                "- Status: planned\n"
                "- Created: [YYYY-MM-DD]\n"
                "- Last updated: [YYYY-MM-DD]\n\n"
                "## Target Outcome\n\n[Outcome]\n"
            ),
            "courses/_template/progress.md": (
                "# Progress\n\n"
                "## Evidence Ledger\n\n"
                "| Concept ID | Status | Evidence | Conditions | Date |\n"
                "| --- | --- | --- | --- | --- |\n"
            ),
            "courses/example/course.md": (
                "# Example Course\n\n"
                "- Status: active\n"
                "- Created: 2026-08-17\n"
                "- Last updated: 2026-08-17\n\n"
                "## Target Outcome\n\nExplain the system.\n"
            ),
            "courses/example/progress.md": (
                "# Progress\n\n"
                "## Evidence Ledger\n\n"
                "| Concept ID | Status | Evidence | Conditions | Date |\n"
                "| --- | --- | --- | --- | --- |\n"
                "| C2 | emerging | Predicted duplicate increments. | Without references or hints. | 2026-08-17 |\n\n"
                "## Review Queue\n\n"
                "| Concept ID | Review after | Reason |\n"
                "| --- | --- | --- |\n"
            ),
        }
        for relative_path, content in files.items():
            destination = root / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content)

    def file_snapshot(self, root: Path) -> dict[str, bytes]:
        return {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*")
            if path.is_file()
        }

    def test_migrates_schema_one_without_losing_existing_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            studio = temporary_root / "studio"
            backup = temporary_root / "backup"
            self.create_schema_one_studio(studio)

            original_progress = (studio / "courses/example/progress.md").read_text()
            result = self.run_migrator(
                "--backup-dir",
                str(backup),
                str(studio),
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                "schema_version: 2",
                (studio / "learning-studio.yaml").read_text(),
            )

            course = (studio / "courses/example/course.md").read_text()
            self.assertIn("## Course Lifecycle", course)
            self.assertIn("## Completion Record", course)

            progress = (studio / "courses/example/progress.md").read_text()
            self.assertIn(
                "| Date | Capability ID | Task or artifact | Conditions and support | Observed evidence | Status | Uncertainty | Next retrieval |",
                progress,
            )
            self.assertIn("Predicted duplicate increments.", progress)
            self.assertIn("Without references or hints.", progress)

            index = (studio / "courses/index.md").read_text()
            self.assertIn("completed-with-mastery", index)
            self.assertIn("completed-with-gaps", index)
            self.assertNotIn("- completed:", index)

            self.assertEqual(
                (backup / "courses/example/progress.md").read_text(),
                original_progress,
            )
            manifest = json.loads((backup / "migration-manifest.json").read_text())
            self.assertEqual(manifest["from_schema"], 1)
            self.assertEqual(manifest["to_schema"], 2)
            self.assertIn("courses/example/progress.md", manifest["changed_files"])

    def test_dry_run_reports_the_complete_plan_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            studio = temporary_root / "studio"
            self.create_schema_one_studio(studio)
            before = self.file_snapshot(studio)

            result = self.run_migrator("--dry-run", str(studio))

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)
            self.assertIn("from schema 1 to schema 2", result.stdout)
            self.assertIn("update learning-studio.yaml", result.stdout)
            self.assertIn("update courses/example/progress.md", result.stdout)
            self.assertIn("no files changed", result.stdout)

    def test_migrates_a_structurally_recognizable_unversioned_studio(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            studio = temporary_root / "studio"
            backup = temporary_root / "backup"
            self.create_schema_one_studio(studio)
            (studio / "learning-studio.yaml").unlink()

            result = self.run_migrator(
                "--backup-dir",
                str(backup),
                str(studio),
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                "schema_version: 2",
                (studio / "learning-studio.yaml").read_text(),
            )
            self.assertFalse((backup / "learning-studio.yaml").exists())
            manifest = json.loads((backup / "migration-manifest.json").read_text())
            self.assertIsNone(manifest["from_schema"])
            self.assertIn("learning-studio.yaml", manifest["created_files"])

    def test_schema_two_studio_is_a_no_op_without_a_new_backup(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            studio = temporary_root / "studio"
            backup = temporary_root / "first-backup"
            self.create_schema_one_studio(studio)
            first_result = self.run_migrator(
                "--backup-dir",
                str(backup),
                str(studio),
            )
            self.assertEqual(first_result.returncode, 0, first_result.stderr)
            before = self.file_snapshot(studio)

            result = self.run_migrator(str(studio))

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("already uses schema 2", result.stdout)
            self.assertEqual(self.file_snapshot(studio), before)

    def test_refuses_a_false_schema_two_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            studio = Path(temporary_directory) / "studio"
            self.create_schema_one_studio(studio)
            marker = studio / "learning-studio.yaml"
            marker.write_text("schema_version: 2\nstudio_type: mastery-tutor\n")
            before = self.file_snapshot(studio)

            result = self.run_migrator("--dry-run", str(studio))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("claims schema 2", result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)

    def test_refuses_a_newer_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            studio = Path(temporary_directory) / "studio"
            self.create_schema_one_studio(studio)
            marker = studio / "learning-studio.yaml"
            marker.write_text("schema_version: 3\nstudio_type: mastery-tutor\n")
            before = self.file_snapshot(studio)

            result = self.run_migrator("--dry-run", str(studio))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("newer than supported", result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)

    def test_refuses_an_ambiguous_completed_course_status(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            studio = Path(temporary_directory) / "studio"
            self.create_schema_one_studio(studio)
            course_path = studio / "courses/example/course.md"
            course_path.write_text(
                course_path.read_text().replace("- Status: active", "- Status: completed"),
            )
            before = self.file_snapshot(studio)

            result = self.run_migrator("--dry-run", str(studio))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Ambiguous completed status", result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)

    def test_refuses_an_ambiguous_completed_index_row(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            studio = Path(temporary_directory) / "studio"
            self.create_schema_one_studio(studio)
            index_path = studio / "courses/index.md"
            index_path.write_text(
                index_path.read_text().replace(
                    "| example | active |",
                    "| example | completed |",
                ),
            )
            before = self.file_snapshot(studio)

            result = self.run_migrator("--dry-run", str(studio))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("ambiguous completed status", result.stderr.lower())
            self.assertEqual(self.file_snapshot(studio), before)

    def test_refuses_a_custom_evidence_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            studio = Path(temporary_directory) / "studio"
            self.create_schema_one_studio(studio)
            progress_path = studio / "courses/example/progress.md"
            progress_path.write_text(
                progress_path.read_text().replace(
                    "| Concept ID | Status | Evidence | Conditions | Date |",
                    "| Concept ID | Status | Evidence | Assistance | Date |",
                ),
            )
            before = self.file_snapshot(studio)

            result = self.run_migrator("--dry-run", str(studio))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unrecognized evidence ledger columns", result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)

    def test_real_migration_requires_a_new_backup_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            studio = temporary_root / "studio"
            self.create_schema_one_studio(studio)
            before = self.file_snapshot(studio)

            missing_backup_result = self.run_migrator(str(studio))

            self.assertNotEqual(missing_backup_result.returncode, 0)
            self.assertIn("requires --backup-dir", missing_backup_result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)

            backup = temporary_root / "existing-backup"
            backup.mkdir()
            existing_backup_result = self.run_migrator(
                "--backup-dir",
                str(backup),
                str(studio),
            )

            self.assertNotEqual(existing_backup_result.returncode, 0)
            self.assertIn("already exists", existing_backup_result.stderr)
            self.assertEqual(self.file_snapshot(studio), before)


if __name__ == "__main__":
    unittest.main()
