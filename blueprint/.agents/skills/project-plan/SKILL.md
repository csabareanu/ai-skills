---
name: project-plan
description: "Create the first user-owned Blueprint project plan for a new project from an idea, brief, or conversation. Run an adaptive, one-question-at-a-time discovery interview, distinguish confirmed decisions from assumptions and open questions, confirm the product understanding, and show a draft for approval before creating or writing blueprint/project-plan.md. Use when the user runs /project-plan, invokes $project-plan, or asks to define a new product direction. For an existing codebase with meaningful shipped behavior, use /adopt instead."
---

# project-plan - define the product direction

## Where it fits

The new-project path is:

    scaffold -> overlay Blueprint -> /onboard -> /project-plan -> /build-plan -> /overview

`/onboard` tunes the workflow to the repository. Define what the product is
and why it should exist here. Leave implementation ordering to `/build-plan`.

## Workflow

### 1. Protect existing project decisions

Inspect `blueprint/project-plan.md` before asking questions.

- If it is missing, continue and create it from the canonical structure only
  after the user approves the draft.
- If it is empty, untouched, or contains only worksheet prompts, continue.
- If it contains substantive user-owned decisions, stop. Report that this skill
  initializes a plan; do not overwrite or silently refresh it. Ask for a
  separate, targeted plan-editing request instead.

Read any idea, brief, or conversation context the user already supplied. Do not
ask for information that is already available.

### 2. Run the discovery grill

Ask the highest-value unanswered question one at a time. Include a suggested
answer only when repository or conversation evidence supports it, and state the
important implication briefly. Do not lead the user when there is no sound basis
for a recommendation.

Treat the topics below as coverage prompts, not a questionnaire. Aim for three
to five discovery questions total. After every answer, re-check the
definition-of-ready below. Exceed five only when a contradiction or
`> TODO (blocking)` would otherwise make the draft unsafe, and explain why the
extra decision is necessary. If the user says the model has enough context or
asks to see the summary, stop questioning immediately and classify any remaining
non-blocking uncertainty as an open question.

Cover only what remains relevant:

- the problem, desired outcome, and why it matters
- the primary user and their critical journey
- MVP capabilities, explicit non-goals, and success signals
- important entities, ownership, sensitivity, or retention constraints
- hard technical constraints, integrations, and platform requirements
- monetization, pricing, or access model
- intended UX shape and visual direction
- deployment, operations, or compliance constraints

Challenge vague scope, bundled features, solution-first assumptions, and
conflicts between answers. If the user wants help choosing a stack or another
open direction, offer a clearly labeled proposal with a short rationale; do not
present it as an accepted decision.

Classify uncertainty consistently:

- `> TODO (blocking): ...` means the plan cannot guide the next stage yet.
- `> Open question: ...` records a non-blocking decision that can be resolved
  later and carried into the overview.

Continue until the problem, primary user, critical journey, MVP boundary,
non-goals, and essential constraints are clear. Optional business, visual, or
deployment details may remain open when they do not affect the MVP. Do not ask
about optional sections one by one merely to make every heading complete; use a
concise proposal or an open question in the draft instead.

Then present a short "What I think we are building" summary containing the
problem, primary user, critical journey, MVP, non-goals, and key constraints.
Ask the user to confirm or correct that understanding before drafting.

### 3. Prepare an exact, reviewable draft

After the understanding is confirmed, draft the complete file with this shape:

    # Project Plan

    ## 1. Problem - What problem are we solving?
    ## 2. Users - Who is this for?
    ## 3. Features - What does the MVP need?
    ## 4. Data - What are we storing?
    ## 5. Tech - What stack are we using?
    ## 6. Monetize - How will this make money?
    ## 7. UI/UX - How should this look and feel?
    ## 8. Deployment - Where and how will this ship?

Replace all worksheet prompts and examples with actual plan content. Put success
signals with the problem or MVP, and put explicit non-goals with the MVP. Keep
the document concise; use short paragraphs or bullets where they improve
clarity.

Do not present the plan as ready while a blocking TODO remains. Show the complete
proposed contents and ask for approval or corrections. Do not create or write
the file until the user explicitly approves the draft.

### 4. Write and hand off

After approval, create or replace only `blueprint/project-plan.md`. Do not edit
`blueprint/build-plan.md`, `blueprint/context/project-overview.md`, skills,
source code, dependencies, or git state.

Report:

- that the project plan was created
- non-blocking open questions and important assumptions
- the next command: `/build-plan` (or `$build-plan` in Codex)

## Rules

- Treat this as product definition, not implementation or detailed architecture.
- Never scaffold, install dependencies, run migrations, or change application
  code.
- Never overwrite a substantive project plan in this create-only workflow.
- Do not invent users, features, business rules, or accepted technology and
  deployment choices.
- Treat `blueprint/project-plan.md` as user-owned project state.
- Keep the interview adaptive; stop asking when the definition-of-ready is met.
