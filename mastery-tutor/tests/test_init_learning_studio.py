#!/usr/bin/env python3

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
INITIALIZER = SKILL_ROOT / "scripts" / "init_learning_studio.py"


class InitLearningStudioTest(unittest.TestCase):
    def run_initializer(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(INITIALIZER), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_initializes_a_complete_new_studio(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "studio"

            result = self.run_initializer(str(destination))

            self.assertEqual(result.returncode, 0, result.stderr)
            expected_files = [
                "learning-studio.yaml",
                ".gitignore",
                "AGENTS.md",
                "learner/profile.md",
                "courses/index.md",
                "courses/_template/course.md",
                "courses/_template/roadmap.md",
                "courses/_template/syllabus.md",
                "courses/_template/progress.md",
                "courses/_template/misconceptions.md",
                "courses/_template/lessons/_template.md",
                "courses/_template/assessments/_template.md",
                "courses/_template/sessions/_template.md",
            ]
            for relative_path in expected_files:
                self.assertTrue(
                    (destination / relative_path).is_file(),
                    f"missing {relative_path}",
                )

            self.assertTrue((destination / "courses/_template/lessons").is_dir())
            self.assertTrue((destination / "courses/_template/artifacts").is_dir())
            self.assertEqual(
                (destination / "courses/_template/syllabus.md").read_bytes(),
                (SKILL_ROOT / "assets/course-template/syllabus.md").read_bytes(),
            )
            self.assertIn(
                "schema_version: 2",
                (destination / "learning-studio.yaml").read_text(),
            )
            self.assertIn(
                "## Course Lifecycle",
                (destination / "courses/_template/course.md").read_text(),
            )
            self.assertIn(
                "| Date | Capability ID | Task or artifact |",
                (destination / "courses/_template/progress.md").read_text(),
            )
            lesson_template = (
                destination / "courses/_template/lessons/_template.md"
            ).read_text()
            self.assertIn("## Big Idea And Intellectual Context", lesson_template)
            self.assertIn(
                "## Connections, Comparisons, And Alternatives",
                lesson_template,
            )
            self.assertIn(
                "## Disciplinary Lenses And Interpretations",
                lesson_template,
            )
            self.assertIn("## What To Remember", lesson_template)
            self.assertIn("## Revision Log", lesson_template)

    def test_initializes_an_existing_empty_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "empty"
            destination.mkdir()

            result = self.run_initializer(str(destination))

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((destination / "learning-studio.yaml").is_file())

    def test_lesson_template_requires_a_pre_delivery_theory_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "studio"

            result = self.run_initializer(str(destination))

            self.assertEqual(result.returncode, 0, result.stderr)
            lesson_template = (
                destination / "courses/_template/lessons/_template.md"
            ).read_text()
            self.assertIn("## Pre-Delivery Theory Gate", lesson_template)
            self.assertIn("Central idea or problem", lesson_template)
            self.assertIn("Governing model or mechanism", lesson_template)
            self.assertIn(
                "Meaningful connection, comparison, or alternative",
                lesson_template,
            )
            self.assertIn(
                "Limits, consequences, or failure modes",
                lesson_template,
            )
            self.assertIn("For programming lessons", lesson_template)
            self.assertIn(
                "Do not begin independent practice until",
                lesson_template,
            )

    def test_refuses_a_non_empty_destination_without_changing_it(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "existing"
            destination.mkdir()
            existing_file = destination / "keep.txt"
            existing_file.write_text("keep me\n")

            result = self.run_initializer(str(destination))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Refusing to initialize", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(existing_file.read_text(), "keep me\n")
            self.assertFalse((destination / "learning-studio.yaml").exists())

    def test_dry_run_reports_files_without_creating_the_destination(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "preview"

            result = self.run_initializer("--dry-run", str(destination))

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(destination.exists())
            self.assertIn("learning-studio.yaml", result.stdout)
            self.assertIn("courses/_template/syllabus.md", result.stdout)

    def test_initializes_a_directory_containing_only_git_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "repository"
            git_directory = destination / ".git"
            git_directory.mkdir(parents=True)

            result = self.run_initializer(str(destination))

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(git_directory.is_dir())
            self.assertTrue((destination / "learning-studio.yaml").is_file())

    def test_optionally_links_the_complete_skill_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            destination = Path(temporary_directory) / "linked"

            result = self.run_initializer("--link-skill", str(destination))

            self.assertEqual(result.returncode, 0, result.stderr)
            skill_link = destination / ".agents/skills/mastery-tutor"
            self.assertTrue(skill_link.is_symlink())
            self.assertEqual(skill_link.resolve(), SKILL_ROOT.resolve())

    def test_refuses_a_symlink_destination_without_changing_its_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            target = root / "target"
            target.mkdir()
            destination = root / "studio-link"
            destination.symlink_to(target, target_is_directory=True)

            result = self.run_initializer(str(destination))

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("through a symlink", result.stderr)
            self.assertFalse((target / "learning-studio.yaml").exists())


if __name__ == "__main__":
    unittest.main()
