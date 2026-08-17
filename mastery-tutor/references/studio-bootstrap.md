# Learning Studio Bootstrap

## Use This Workflow

Initialize a studio only after the learner explicitly selects tracked-course mode, no studio exists, and the learner confirms the destination. Do not initialize a studio during consultation or an untracked lesson.

Use `scripts/init_learning_studio.py` instead of recreating the structure manually. The script combines the generic studio assets with the canonical syllabus template.

## Safety Contract

- Accept a destination that does not exist, is empty, or contains only `.git`.
- Refuse symlink destinations, files, and directories containing any other entry.
- Never add a force or overwrite path to the initialization workflow.
- Treat an existing studio as a migration case; do not run the initializer against it.
- Run `--dry-run` first and summarize the planned destination and structure before initialization.
- Use `--link-skill` only when the learner wants a project-local absolute symlink to this skill.

## Initialize

From the installed skill directory, preview the complete operation:

```bash
python3 scripts/init_learning_studio.py --dry-run --link-skill /absolute/path/to/learning-studio
```

After the destination and preview are accepted, initialize it:

```bash
python3 scripts/init_learning_studio.py --link-skill /absolute/path/to/learning-studio
```

Omit `--link-skill` when skill discovery is already provided globally or the learner wants to link or copy the skill separately.

## Result

The initialized studio contains:

- `learning-studio.yaml`: schema version and studio type
- `AGENTS.md`: local privacy, state, teaching, and version-control agreement
- `.gitignore`: editor, cache, secret, and disposable-file exclusions
- `learner/profile.md`: durable cross-course learner information
- `courses/index.md`: course registry and status vocabulary
- `courses/_template/`: course, roadmap, syllabus, progress, misconception, assessment, and session templates plus lesson and artifact directories
- `.agents/skills/mastery-tutor`: optional skill symlink created by `--link-skill`

The templates contain no personal history or copied learner preferences.

## Continue After Initialization

1. Read the new studio's `AGENTS.md`, learner profile, and course index.
2. Copy `courses/_template/` to a unique `courses/<course-slug>/` directory.
3. Populate it from the approved consultation plan and any unresolved diagnostic evidence.
4. Register the course in `courses/index.md`.
5. Begin instruction only after the tracked course state is coherent.
