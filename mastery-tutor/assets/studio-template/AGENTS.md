# Learning Studio Working Agreement

## Purpose

Use this repository as a private, local-only learning studio for adaptive courses across academic, creative, technical, and practical subjects.

## Tutor Routing

- Use the installed `mastery-tutor` skill for course design, lesson delivery, assessment, and progress work.
- Keep the discoverable skill at `.agents/skills/mastery-tutor` when using a project-local symlink.
- In a tracked course, `mastery-tutor` owns course design, sequencing, theory depth,
  formal lesson delivery, assessment, and durable course state.
- Supporting skills may propose adaptations and run bounded activities, but
  they must not independently relax or replace that contract, resequence the
  course, change mastery criteria, or update course state. Route proposed
  adaptations through `mastery-tutor`; ask the learner before material changes
  to the course goal, depth, or final deliverable.

## State And Memory

- Treat design, preview, comparison, and audit requests as consultation unless the learner explicitly asks to start or track a course.
- Read `learner/profile.md` and `courses/index.md` before creating or resuming a tracked course.
- Keep every tracked course in its own `courses/<course-slug>/` directory.
- Record demonstrated evidence, misconceptions, adaptations, reviews, and next steps.
- Do not treat exposure, confidence, or tutor-authored work as proof of mastery.
- Store curated session evidence, not full transcripts.
- Update the shared learner profile only for durable cross-course information.
- Ask before materially changing a course's goal, depth, or final deliverable.

## Teaching

- Maintain a visible adaptive roadmap and concrete syllabus; author detailed lessons just in time.
- Preserve every formal lesson as a standalone, revisable reference chapter;
  keep chronological interaction and exact evidence in sessions and progress.
- Teach governing ideas, mechanisms, intellectual or design context,
  comparisons, tradeoffs, and limits—not just terminology or syntax—and
  combine that theory with subject-appropriate practice.
- Use relevant disciplinary lenses and interpretations; facts, dates,
  definitions, formulas, syntax, and procedures are material for reasoning,
  not sufficient lessons by themselves.
- Calibrate lesson density to the learner and agreed session length; use narrow
  remediation as a segment and continue into depth or transfer when possible.
- Pause for the learner's response at exercises and assessments.
- Use HTML lessons only when visual or interactive presentation improves learning.
- Keep the next task small enough to attempt and review coherently.

## Privacy And Version Control

- Keep this repository local-only. Do not add a Git remote, push, publish, or share its contents.
- Avoid sensitive personal data that does not improve the learning experience.
- Do not commit unless the user explicitly requests it.
