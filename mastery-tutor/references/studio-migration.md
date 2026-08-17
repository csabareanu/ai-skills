# Learning Studio Migration

## Scope

Use this workflow for an existing unversioned or schema-1 Mastery Tutor studio.
The current migration targets schema 2. It upgrades structure and preserves
course content; it does not redesign courses, reassess the learner, or infer
historical facts that were never recorded.

Schema 2 introduces:

- evidence rows that separate task, conditions, direct observation, status judgment, uncertainty, and next retrieval
- explicit enrollment, start, completion, archive, and status-transition history
- separate `completed-with-mastery` and `completed-with-gaps` outcomes
- a completion record that distinguishes ending the learning path from demonstrating mastery

## Safety Contract

- Keep the studio read-only until the migration is approved and complete.
- Run `scripts/migrate_learning_studio.py --dry-run` first.
- Require a new, external `--backup-dir` for every real migration. Never reuse or overwrite a backup.
- Build and validate the whole change set before writing, back up every changed existing file, then write files atomically.
- Leave the backup available if migration fails. Roll back any studio files already written in that attempt.
- Test migrations on disposable copies when changing the migration implementation. Do not use a live studio as a development fixture.
- Refuse unsupported, malformed, or newer schemas.
- Refuse customized evidence columns rather than guessing how fields map.
- Refuse an old unqualified `completed` course status. The learner must first decide whether it means `completed-with-mastery` or `completed-with-gaps`.

The migration may record that earlier lifecycle dates and transitions are
unknown. That is more accurate than inventing them.

## Preview

Run the script from the central skill source, not from inside the studio's
project-local symlink:

```bash
SKILL_SOURCE=/home/csabareanu/Projects/codex/ai-skills/mastery-tutor
STUDIO_ROOT=/absolute/path/to/learning-studio

python3 "$SKILL_SOURCE/scripts/migrate_learning_studio.py" \
  --dry-run \
  "$STUDIO_ROOT"
```

Review the source schema, target schema, and complete changed-file list. Resolve
every refusal explicitly; do not edit the version marker by hand to bypass it.

## Migrate

Choose a backup path outside the studio that does not exist:

```bash
BACKUP_ROOT=/absolute/path/to/learning-studio-schema-1-backup

python3 "$SKILL_SOURCE/scripts/migrate_learning_studio.py" \
  --backup-dir "$BACKUP_ROOT" \
  "$STUDIO_ROOT"
```

The backup contains every pre-migration file that the tool changed plus
`migration-manifest.json`. An unversioned studio has no old marker to copy, so
the manifest records `learning-studio.yaml` as a created file.

## Verify

After migration:

1. Confirm `learning-studio.yaml` reports schema 2 and studio type `mastery-tutor`.
2. Review each changed course's lifecycle and completion record; replace `unknown` only when reliable evidence exists.
3. Confirm old evidence text and conditions remain present in the expanded ledger. Blank task, uncertainty, or retrieval cells mean the old schema did not record those facts.
4. Review `courses/index.md` and every course status for consistency.
5. Resume tracked teaching only after the migrated state is coherent.

Do not delete the backup as part of migration. Retention is a separate learner
decision after the upgraded studio has been reviewed.
