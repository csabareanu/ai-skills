# Course Design And State

## Contents

1. Operating mode boundary
2. Intake and diagnostic
3. Adaptive roadmap
4. Concrete course blueprint
5. Course shape and completion
6. Durable state
7. State update rules

## Operating Mode Boundary

Treat course design and course enrollment as separate decisions.

- In `consultation`, design or audit the roadmap and blueprint without creating or updating learner or course state. Save a standalone proposal only when the learner explicitly asks for a file.
- In `tracked course`, create and maintain durable state after the learner explicitly asks to start, enroll in, track, or resume the course.
- In `untracked lesson`, teach without requiring a studio or preserving evidence after the session.

Do not interpret a request to design, preview, compare, or audit a course as consent to enroll the learner or mutate an existing course.

When consultation becomes a tracked course, copy the approved roadmap and blueprint into durable state rather than restarting the design process. Complete any unresolved diagnostic or verify any consequential assumption before Lesson 1, then revise only what the new evidence justifies.

## Intake And Diagnostic

Gather only information that changes the course:

- Desired real-world outcome and reason for learning
- Target depth, quality bar, and deadline if any
- Available time, cadence, tools, accessibility needs, and constraints
- Prior exposure and adjacent skills
- Preferred balance of theory, guidance, independence, and feedback

Ask one focused question at a time when the answer gates the next decision. Include a recommendation for design choices, but do not suggest answers to diagnostic questions.

Test representative prerequisites with a small task, explanation, interpretation, or demonstration. Avoid long placement exams unless the subject or stakes justify them. Record demonstrated evidence and uncertainty separately from self-reported confidence.

## Adaptive Roadmap

Publish a complete first-pass map before detailed lesson delivery. Organize it into:

- `prerequisite`: knowledge required to approach the goal safely or coherently
- `core`: concepts and abilities required by the target outcome
- `enrichment`: optional context, breadth, or alternative perspectives
- `advanced`: deeper branches that exceed the initial goal

For every core item, define an observable mastery criterion such as:

- derive or prove a result under stated assumptions
- implement and test a behavior independently
- analyze evidence and defend an interpretation
- identify, compare, and critique visual techniques
- perform a procedure and diagnose common failures
- explain the concept and transfer it to an unfamiliar case

Expose dependencies and the current recommended path. Detail upcoming lessons just in time. Insert remediation when evidence reveals a missing prerequisite, allow a learner to test out of mastered material, and explain roadmap adaptations.

Do not erase history when the roadmap changes. Record the reason in the roadmap's adaptation log. Ask before changing the target outcome, depth, or final deliverable.

## Concrete Course Blueprint

For a tracked course, create `syllabus.md` after the initial roadmap. In consultation, use the same conceptual distinction without creating state files. Keep the two artifacts distinct:

- `roadmap.md` records what must be mastered, why it depends on other capabilities, how mastery will be observed, and current status.
- `syllabus.md` records the concrete teaching path: course arc, modules, lesson cards, source and example spine, practice, assessment architecture, independent workload, pacing, and integration milestones.

The blueprint is more concrete than the roadmap but less detailed than an authored lesson. Name what each lesson will address and what the learner will do without prewriting explanations, solutions, code, assessment answers, or detailed facilitation scripts.

Follow [curriculum blueprint](curriculum-blueprint.md) for candidate discovery, lesson-card fields, project progression, and the quality audit.

## Course Shape And Completion

Choose the learning shape from the goal rather than the subject label alone:

| Goal shape | Strong concluding evidence |
| --- | --- |
| Build or perform | Capstone, practical demonstration, troubleshooting scenario |
| Create or develop taste | Portfolio, critique, revision narrative |
| Explain or argue | Essay, source analysis, oral defense, structured discussion |
| Solve formal problems | Cumulative problem set, proof, written or oral exam |
| Gain broad literacy | Mixed assessment plus a synthesis project |
| Complete a narrow procedure | Independent run-through plus failure recovery |

Use projects throughout a course when integration matters; do not reserve all application for the end. Use an exam only when recall under constraints or broad independent coverage is meaningful.

Treat lifecycle, path completion, and mastery as related but distinct facts:

- `planned`: designed but not started
- `active`: currently progressing
- `paused`: intentionally deferred with a recorded resume point
- `completed-with-mastery`: the learning path ended and the agreed completion evidence was demonstrated under meaningful independent conditions
- `completed-with-gaps`: the learning path ended, but named core capabilities remain unresolved
- `archived`: retained without an active learning goal; this says nothing by itself about completion or mastery

Never use an unqualified `completed` status. Record enrollment, start,
completion, and archive dates when they occur, and append every status change to
the lifecycle history. Preserve the current status when a course goal changes;
change status only when the course actually crosses a lifecycle boundary.

Before completing a course, reconcile the final evidence with every core roadmap
criterion and the agreed completion evidence. Record whether the planned path
ended, the mastery outcome, remaining gaps, and the next maintenance,
remediation, or progression step. A learner may deliberately finish a course
with gaps; report that honestly instead of silently extending the course or
claiming mastery.

## Durable State

Use durable state only for a tracked course.

New studios include `learning-studio.yaml` with a structure schema version. Treat it as studio metadata, not learner evidence. Schema 2 uses the explicit evidence ledger and lifecycle contract in this reference, and it is the only schema supported by the current skill. If an existing marker is absent, malformed, or reports another schema or studio type, keep the studio read-only. Do not add, remove, or change the marker to bypass that boundary.

Keep shared memory in `learner/profile.md`. Store only lasting preferences, goals, demonstrated strengths, recurring needs, and cross-course prerequisite evidence.

Keep each course under `courses/<course-slug>/`:

- `course.md`: stable goal, constraints, diagnostic baseline, teaching agreement, lifecycle history, completion evidence, and completion record
- `roadmap.md`: dependency-aware curriculum, mastery criteria, statuses, and adaptation log
- `syllabus.md`: complete course arc, concrete modules and lesson cards, roadmap mappings, representative sources and anchors, assessment architecture, independent workload, pacing, integration milestones, and blueprint revisions
- `progress.md`: current position, explicit evidence ledger, review queue, completed work, and next step
- `misconceptions.md`: unresolved and resolved misunderstandings with evidence
- `lessons/`: authored Markdown or HTML lesson artifacts
- `sessions/`: concise records of meaningful tutoring interactions
- `assessments/`: assessment prompts, results, rubrics, and feedback
- `artifacts/`: learner work or links to work retained elsewhere

After the learner explicitly selects tracked mode, create a course by copying the structure in `courses/_template/`. If that template lacks `syllabus.md`, copy `assets/course-template/syllabus.md` into it without overwriting any customized state. For an existing course that needs curriculum planning but has no syllabus, copy the studio's syllabus template into the course and reconcile it with the existing goal and roadmap. Register every course in `courses/index.md`. Use stable, lowercase, hyphenated slugs and never reuse a slug for a different goal.

## State Update Rules

- Record evidence, not praise or guesses.
- For each ledger entry, keep the task or artifact, conditions and support, observed evidence, status judgment, uncertainty, and next retrieval distinct.
- Use uncertainty to identify what still needs testing. Do not interpret a blank observation, missing artifact, or unattempted task as failed performance.
- Keep an unresolved misconception until later work demonstrates correction and retention.
- Distinguish `not assessed`, `emerging`, `developing`, `demonstrated`, and `retained` instead of inventing precise percentages.
- Record skipped material and the evidence or learner decision that justified skipping it.
- Record source-course evidence when transferring a strength across courses.
- Keep session notes concise; link artifacts rather than embedding large outputs or transcripts.
- Avoid sensitive personal data that does not improve teaching.
- Use the learner's latest explicit statement when stored preferences conflict, then update the state.
- Update dates and the next action before ending a meaningful session.
- Record lifecycle transitions without rewriting history, and reconcile the completion record whenever a course reaches either completion status.
