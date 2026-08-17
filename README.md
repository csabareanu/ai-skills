# AI Skills

A personal collection of 19 Codex skills maintained as reusable, independent
building blocks. Skill behavior lives here; project plans, development history,
learner progress, and other working state stay in the projects that use them.

## Skill sets

### Blueprint workflow

[`blueprint/`](blueprint/) contains 18 skills for planning, implementing,
checking, and completing software work in small, human-reviewed steps. It is an
independent Codex-only fork of
[AI Coding Blueprint](https://ai-blueprint.dev/), deliberately curated without
automatic upstream updates.

- [Included skills and deferred upstream features](blueprint/README.md)
- [Installation and project workflow](blueprint/USAGE.md)
- [Fork provenance and maintenance policy](blueprint/FORK.md)

### Mastery Tutor

[`mastery-tutor/`](mastery-tutor/) is a locally authored standalone skill, not
part of the Blueprint fork. It designs and runs adaptive learning journeys,
uses evidence to assess mastery, and preserves progress in a separate learning
studio.

- [Skill definition](mastery-tutor/SKILL.md)
- [Symlink installation and usage](mastery-tutor/USAGE.md)

## Reusing the skills

Link or copy complete skill directories into a consuming repository's
`.agents/skills/` directory. Prefer symlinks for personal projects that should
receive updates from this repository immediately; use reviewed copies when a
project needs a portable snapshot.

Never share project-specific state through those links. Follow the usage guide
for the selected skill set to see which files belong in each consuming project.
