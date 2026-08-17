# Using Mastery Tutor

`mastery-tutor` provides reusable tutoring behavior. The learner profile,
courses, lessons, assessments, and progress records belong to the learning
studio that uses the skill; they must not be stored in this skill directory.

The central rule is:

> Symlink the skill. Keep learning state in the learning studio.

## Link it into an existing project

Use this manual link flow when the project or learning studio already exists.
For a brand-new studio, use the initializer in the next section so the studio
state and optional skill link are created together.

Set the source and target paths for the current shell:

```bash
SKILL_SOURCE=/home/csabareanu/Projects/codex/ai-skills/mastery-tutor
PROJECT_ROOT=/absolute/path/to/your/learning-studio
```

Create the project's skill directory and link the complete skill package:

```bash
mkdir -p "$PROJECT_ROOT/.agents/skills"
ln -sT "$SKILL_SOURCE" "$PROJECT_ROOT/.agents/skills/mastery-tutor"
```

Link the directory, not only `SKILL.md`. The skill also uses its `references/`,
`assets/`, and `agents/` directories.

`ln -sT` refuses to replace an existing path. If `mastery-tutor` is already
installed, inspect that path and decide which version the project should use.

## Create a brand-new learning studio

The initializer accepts a destination that does not exist, is empty, or
contains only `.git`. It refuses every other existing destination and has no
force or overwrite option.

Preview the operation first:

```bash
python3 "$SKILL_SOURCE/scripts/init_learning_studio.py" \
  --dry-run \
  --link-skill \
  "$PROJECT_ROOT"
```

Then create the studio and project-local skill link:

```bash
python3 "$SKILL_SOURCE/scripts/init_learning_studio.py" \
  --link-skill \
  "$PROJECT_ROOT"
```

Omit `--link-skill` when Mastery Tutor is already discovered globally or when
you want to link or copy the skill separately. Do not create the manual symlink
before running the initializer; `.agents/` would correctly make the destination
non-empty.

## Verify discovery

From the learning-studio repository, run:

```bash
test -f .agents/skills/mastery-tutor/SKILL.md
readlink .agents/skills/mastery-tutor
```

Launch Codex from that repository and run `/skills`. The list should include
`mastery-tutor`. If it does not appear after creating the link, restart Codex.

Invoke it explicitly with `$mastery-tutor`, for example:

```text
$mastery-tutor Design a course that takes me from basic probability to being
able to understand Bayesian inference. Start with a compact diagnostic.
```

Design, preview, comparison, and audit requests use consultation mode by
default. They do not create or update learner or course state. To turn an
approved design into a durable course, ask explicitly:

```text
$mastery-tutor Start and track this course in the current learning studio.
```

Mastery Tutor should preserve the approved plan when enrolling. It may complete
an unresolved diagnostic before Lesson 1 and adapt the plan from that evidence,
but it should not redesign the course from scratch.

```text
$mastery-tutor Resume my Laravel architecture course from the recorded next
step and test whether I retained the previous concept.
```

Single lessons and tutorials are untracked by default:

```text
$mastery-tutor Teach me one focused lesson on color temperature.
```

Ask to track the lesson only when you want its evidence and next step preserved
for future sessions.

## Understand the learning studio

For a sustained course, the target repository—not this skill—owns a structure
like this:

```text
AGENTS.md
learner/
  profile.md
courses/
  index.md
  _template/
    course.md
    roadmap.md
    syllabus.md
    progress.md
    misconceptions.md
    lessons/
    sessions/
    assessments/
    artifacts/
```

Each tracked course receives its own directory under `courses/<course-slug>/`
using that template. If the repository is not yet a learning studio, ask
`$mastery-tutor` to start and track the course and tell it where you want
durable state kept. It should confirm the location before creating studio or
course files.

For manual initialization, copy `assets/studio-template/` into an empty target,
copy `assets/course-template/syllabus.md` to
`courses/_template/syllabus.md`, and create empty
`courses/_template/lessons/` and `courses/_template/artifacts/` directories.
The initializer performs these steps consistently and is preferred.

When an older studio has no `courses/_template/syllabus.md`, Mastery Tutor can
copy the canonical syllabus into that existing template without replacing its
other files. This is a narrow compatibility repair, not a schema migration.
Copied studio and syllabus files are project state; do not symlink them back
into this skill.

Keep a root `AGENTS.md` with any repository-specific privacy, tool, and working
rules. Do not place learner history inside the symlinked `mastery-tutor`
directory: edits through that link modify this central `ai-skills` repository.

## Updates and portability

A symlinked project sees changes made to this skill immediately. Restart Codex
if a changed version is not detected.

The link is absolute, so it works only while this repository remains at the
same path. It is suitable for local projects on this machine but not portable
to another machine. For a shared or portable repository, copy and review a
snapshot of the whole `mastery-tutor` directory instead.

To stop using the linked skill without touching its source, remove only the
link from the consuming project:

```bash
unlink "$PROJECT_ROOT/.agents/skills/mastery-tutor"
```

This does not delete course state or the central skill.
