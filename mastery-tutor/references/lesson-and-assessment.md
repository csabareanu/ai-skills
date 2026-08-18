# Lesson And Assessment

## Contents

1. Lesson design
2. Conceptual depth and lesson density
3. Durable lesson reference
4. Subject-appropriate evidence
5. Programming authorship
6. Practice and feedback
7. Mastery decisions
8. Assessment integrity

## Lesson Design

Define one coherent outcome for the lesson. Keep three activity types distinct:

- **Diagnostic:** establishes starting or prerequisite evidence before teaching; it is not a numbered lesson.
- **Opening retrieval:** briefly checks previously taught material; it may open a lesson but does not become the lesson by itself.
- **Formal lesson:** teaches toward the next approved syllabus card and includes explanation, practice, feedback, and evidence appropriate to its outcome.

At the start of a formal lesson, name the lesson, roadmap focus, objective, and
role in the course arc. If retrieval is due, normally ask one focused prompt or
one small, tightly related set. Label it explicitly and keep it subordinate to
the lesson. Do not assess new terminology or concepts before teaching them
unless running a clearly labeled diagnostic, and do not record unfamiliar
not-yet-taught material as a misconception.

Present the lesson in the conversation. A Markdown or HTML artifact preserves
the material and learner evidence, but it does not replace visible instruction.
Before independently assessing new material, provide substantial theory, a
mental model, and at least one worked example or demonstration. Predictions may
interrupt the explanation, but do not turn the opening into prolonged grilling.

Use this loop adaptively. A formal lesson should normally retain meaningful
theory, example, learner practice, feedback, and evidence phases even when
their exact form varies by subject:

1. Retrieval or prerequisite check
2. Motivation and learning objective
3. Definitions, theory, and mental model
4. Worked example, demonstration, or source encounter
5. Guided practice
6. Independent application
7. Teach-back, critique, discussion, or transfer
8. Feedback and remediation
9. Mastery check
10. Review scheduling

Make theory substantial when the learner requests depth. Explain how ideas connect, what assumptions they depend on, when they fail, and why alternative models exist. Break long theoretical development with predictions, derivations, examples, or short checks instead of presenting an uninterrupted lecture.

Follow the approved syllabus order. If tooling, accessibility, missing source
material, or another constraint blocks the next card, explain the available
choices and wait for the learner before substituting another lesson. Treat an
approved substitute as an explicit sequencing or pacing adaptation; update the
syllabus and course state. Never silently count a diagnostic or retrieval
checkpoint as completion of the blocked lesson.

## Conceptual Depth And Lesson Density

Default to an academic explanatory style while selecting only dimensions that
genuinely clarify the lesson. Build an appropriate path through:

1. the central problem, question, or abstraction
2. relevant intellectual, historical, or design context
3. the governing theory, semantics, mechanism, or causal model
4. the notation, syntax, procedure, or technique that expresses that model
5. connections to prior knowledge and comparisons with genuine alternatives
6. assumptions, tradeoffs, limits, failure modes, and consequences
7. application, interpretation, critique, or transfer

Do not mechanically force every item into every lesson. Omit decorative history
and superficial comparisons. Do not call a glossary, syntax tour, sequence of
commands, or list of rules substantial theory.

Select disciplinary lenses that reveal structure, causation, interpretation,
or consequences. Use them as questions the subject asks, not as a checklist:

| Subject shape | Useful lenses when relevant |
| --- | --- |
| History and social inquiry | comparison with related events or movements; institutions, class, collective action, economics, political philosophy, ideology, agency versus structure, contingency, memory, and historiography |
| Programming and engineering | design philosophy, semantics, compiler or runtime behavior, type and memory models, paradigms, tooling, organizational consequences, idioms, alternatives, and tradeoffs |
| Mathematics and science | derivation, mechanism, model assumptions, evidence, epistemology, historical development, competing models, approximation, boundary conditions, and empirical limits |
| Literature, art, and design | form, technique, aesthetics, interpretation, historical and cultural context, audience, power, ethics, and comparison with related works or movements |
| Human languages | grammar, semantics, pragmatics, register, comparative linguistics, historical change, culture, discourse, and translation tradeoffs |
| Practical and professional subjects | governing principles, systems context, constraints, safety, ethics, failure analysis, standards, alternatives, and consequences |

For example, a French Revolution lesson should not stop at dates and actors.
According to its outcome, connect events to comparable revolutions or reform
movements, social structure and collective action, economic pressures,
Enlightenment and political philosophy, institutional change, competing causal
explanations, and later historical memory. Make comparison criteria explicit
and avoid false equivalence or presentism.

For programming-language lessons, teach the language as a system of software-
engineering choices. When relevant, explain:

- the problems and priorities that shaped the language
- compiler, runtime, type, memory, error, package, and concurrency models
- how surface syntax expresses those semantics
- idiomatic use and why direct translation from another language may be weak
- comparisons with languages the learner knows, distinguishing syntactic
  resemblance from semantic difference
- benefits purchased by a design choice and the costs or capabilities forgone

Size the lesson to the agreed session duration and current evidence. A full
guided session should contain a substantial conceptual and performance arc, not
one isolated token or tiny exercise. Treat narrow prerequisite repair as a
segment when possible, then continue into the approved lesson after the repair
succeeds. If the learner progresses quickly, deepen the explanation, compare an
alternative, debug a failure, or add transfer instead of ending at the minimum
check.

Use checkpoints only when the response can change the explanation, support, or
next task. Avoid interrupting every small conceptual move for evidence
bookkeeping. For programming, prefer an evolving meaningful program, debugging
episode, design decision, or behavior change over several disconnected toy
edits.

## Durable Lesson Reference

Create or update one lesson artifact under `lessons/` for every formal lesson.
Use the bundled lesson template as a starting point. Make the artifact usable as
a standalone study chapter after the conversation is no longer available.

A durable lesson should normally preserve:

- the outcome, prerequisites, and connection to the course arc
- the central idea, relevant intellectual or design context, important
  vocabulary, theory, mechanisms, and mental models in coherent prose
- meaningful connections, comparisons, alternatives, and tradeoffs
- subject-appropriate disciplinary lenses and important interpretations
- worked examples, demonstrations, cases, or source material actually used
- assumptions, limits, failure modes, common confusions, and corrected models
- a concise summary of what to remember
- retrieval or self-check prompts and links to relevant sources or artifacts

Preserve the final corrected understanding rather than a transcript of every
turn. Keep exact learner answers, grading tables, support conditions, evidence
status, and chronological interaction in `sessions/` and `progress.md`; link to
them when useful. Generalize an observed mistake into a reusable warning only
when doing so improves the lesson.

Do not reveal answers to active independent assessments in the lesson. Include
worked solutions only after they have been discussed or released, and label
tutor-authored examples separately from learner-authored artifacts.

Lessons remain revisable references after their original delivery. Correct
errors and add small clarifications directly. Record substantial later
explanations, examples, changed scope, or source updates in the lesson revision
log, including whether the material was part of the original lesson or added
later. Never rewrite history by presenting later material as originally taught.

## Subject-Appropriate Evidence

| Learning shape | Prefer evidence such as |
| --- | --- |
| Mathematics and formal science | Derivations, proofs, problem sets, model interpretation, error analysis |
| Programming and informatics | Design predictions, implementations, debugging labs, tests, code explanation |
| History and social inquiry | Timelines, primary-source analysis, causal arguments, comparison, oral defense |
| Art and design | Visual comparison, technique study, creation, critique, revision, portfolio |
| Practical procedures | Guided performance, independent demonstration, safety checks, failure recovery |
| Languages | Recall, comprehension, production, conversation, correction, spaced reuse |
| Conceptual or philosophical topics | Teach-back, counterexamples, Socratic dialogue, essays, case analysis |

Mix evidence types when the goal spans knowledge, judgment, and performance.

## Programming Authorship

For programming lessons, identify which code embodies the target concept and
which work is incidental scaffolding. Default the target implementation to
learner-authored work:

- After theory and an analogous worked example, give a bounded behavior,
  constraints, and observable checks without supplying the target solution.
- Let the learner write the smallest meaningful implementation before the tutor
  generates or directly edits it.
- Provide support progressively: clarify the task, ask a guiding question,
  offer a focused hint, show pseudocode, or provide a partial skeleton before a
  complete solution.
- Allow AI to handle setup, repetitive boilerplate, test data, or other
  scaffolding only when those are not themselves the learning objective.
- Allow direct implementation when the learner explicitly requests direct
  instruction or when producing software, rather than deliberate practice, is
  the agreed goal.
- Record whether code was independent, hinted, AI-assisted, or tutor-completed.
  Do not count AI-generated target code as independent evidence.
- After direct assistance, recover evidence through explanation, modification,
  debugging, transfer, or unaided reimplementation. Require at least one
  meaningful independently authored task before marking a programming
  capability demonstrated.

Manual typing is not sufficient evidence when the learner is merely copying a
provided solution. Preserve design and implementation decisions for the
learner, not keystrokes for their own sake.

## Practice And Feedback

- Ask for a prediction or attempt before showing a full solution when practical.
- Use open-ended prompts for reasoning; use multiple choice when discriminating between plausible alternatives is itself useful.
- Present quiz items in small groups or one at a time when answers should influence the next question.
- Design distractors from realistic misconceptions, not trivia or wording traps.
- Separate conceptual errors, procedural errors, and communication issues in feedback.
- Give the smallest hint that unlocks productive progress.
- Require correction or a fresh example after important feedback.
- Add transfer: change the representation, context, constraints, or problem surface.
- Invite free discussion for interpretation, critique, ethics, taste, strategy, and competing explanations.
- Avoid repetitive exercises after the learner has demonstrated flexible understanding.

For hands-on labs, specify the objective, starting point, constraints, available tools, expected artifact, checks, and stopping conditions. For risky physical, financial, medical, legal, or security procedures, narrow the lab to safe and authorized actions and surface professional or safety boundaries.

## Mastery Decisions

Evaluate evidence across four dimensions when relevant:

- `explain`: articulate the idea and its important relationships
- `apply`: use it correctly in a representative task
- `diagnose`: recognize mistakes, limits, and failure modes
- `transfer`: adapt it to a meaningfully different context

Use these states:

- `not assessed`: no useful evidence yet
- `emerging`: partial recall or performance with substantial support
- `developing`: succeeds in familiar cases with limited support
- `demonstrated`: independently meets the stated criterion
- `retained`: demonstrates the ability again after delay or in later integrated work

Do not require every dimension for every concept. Define the needed evidence in the roadmap. Advance after `demonstrated` when later retrieval is scheduled; reserve `retained` for later evidence.

When evidence is insufficient, choose one response:

- reteach with a different representation
- repair a prerequisite
- reduce task complexity while preserving the concept
- assign another deliberate practice variation
- pause and ask the learner to explain their reasoning

## Assessment Integrity

- Keep answers and rubrics hidden until the learner submits or explicitly asks to stop the assessment.
- Do not count work substantially completed by the tutor as independent evidence.
- State when tool use, references, collaboration, or time limits are allowed.
- Grade against disclosed criteria and quote or link the learner's evidence.
- Allow corrections, but distinguish first-attempt evidence from learning after feedback.
- Prefer an oral follow-up or novel variation when authorship or shallow pattern matching is uncertain.
- Record uncertainty honestly rather than forcing a pass/fail judgment.

End a meaningful session by stating what evidence changed, which misconceptions remain, what review is due, and the next smallest useful task. Then update the course state.
