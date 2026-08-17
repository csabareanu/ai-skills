# Course Design And State

## Contents

1. Intake and diagnostic
2. Adaptive roadmap
3. Course shape and completion
4. Durable state
5. State update rules

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

## Durable State

Keep shared memory in `learner/profile.md`. Store only lasting preferences, goals, demonstrated strengths, recurring needs, and cross-course prerequisite evidence.

Keep each course under `courses/<course-slug>/`:

- `course.md`: stable goal, constraints, diagnostic baseline, teaching agreement, and completion evidence
- `roadmap.md`: dependency-aware curriculum, mastery criteria, statuses, and adaptation log
- `progress.md`: current position, evidence ledger, review queue, completed work, and next step
- `misconceptions.md`: unresolved and resolved misunderstandings with evidence
- `lessons/`: authored Markdown or HTML lesson artifacts
- `sessions/`: concise records of meaningful tutoring interactions
- `assessments/`: assessment prompts, results, rubrics, and feedback
- `artifacts/`: learner work or links to work retained elsewhere

Create a course by copying the structure in `courses/_template/`. Register it in `courses/index.md`. Use stable, lowercase, hyphenated slugs and never reuse a slug for a different goal.

## State Update Rules

- Record evidence, not praise or guesses.
- Keep an unresolved misconception until later work demonstrates correction and retention.
- Distinguish `not assessed`, `emerging`, `developing`, `demonstrated`, and `retained` instead of inventing precise percentages.
- Record skipped material and the evidence or learner decision that justified skipping it.
- Record source-course evidence when transferring a strength across courses.
- Keep session notes concise; link artifacts rather than embedding large outputs or transcripts.
- Avoid sensitive personal data that does not improve teaching.
- Use the learner's latest explicit statement when stored preferences conflict, then update the state.
- Update dates and the next action before ending a meaningful session.
