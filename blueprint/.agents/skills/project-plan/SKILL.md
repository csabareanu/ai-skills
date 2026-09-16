---
name: project-plan
description: "Create the first user-owned Blueprint project plan for a new or freshly scaffolded project from an idea, brief, or conversation. Run an adaptive product interview and technology-fit consultation, distinguish confirmed decisions from recommendations and open questions, confirm shared understanding, and show a draft for approval before writing blueprint/project-plan.md. Use when the user runs /project-plan, invokes $project-plan, or asks to define a new product direction after setup. For a blank repository that still needs stack selection and scaffolding, use start-project; for meaningful shipped behavior, use adopt."
---

# project-plan - define the product direction

## Where it fits

The already-scaffolded new-project path is:

    scaffold -> overlay Blueprint -> /onboard -> /project-plan -> /build-plan -> /overview

`/onboard` tunes the workflow to the repository. Define what the product is
and why it should exist here. Leave implementation ordering to `/build-plan`.

For a blank repository where the stack is not yet chosen, use `/start-project`
instead. It performs product discovery and technology selection before
scaffolding, writes the approved project plan, and then hands off to `/onboard`.

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
to five product discovery questions total. After every answer, re-check the
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
conflicts between answers.

Classify uncertainty consistently:

- `> TODO (blocking): ...` means the plan cannot guide the next stage yet.
- `> Open question: ...` records a non-blocking decision that can be resolved
  later and carried into the overview.

Continue until the problem, primary user, critical journey, MVP boundary,
non-goals, and essential constraints are clear. Optional business, visual, or
deployment details may remain open when they do not affect the MVP. Do not ask
about optional sections one by one merely to make every heading complete; use a
concise proposal or an open question in the draft instead.

### 3. Run a technology-fit consultation

After the product shape is clear, identify technology decisions that materially
affect the architecture, deployment, or roadmap. Ask only the unresolved
questions that matter, such as target platform, the user's experience and
learning goals, delivery speed, data or integration needs, hosting budget, and
privacy or compliance constraints.

If the user has not already made an informed stack choice, recommend one
coherent stack with a short rationale tied to the product and constraints. Offer
one alternative only when it exposes a meaningful tradeoff. Clearly label
recommendations as proposals, verify unstable compatibility, provider, or
pricing claims against authoritative sources when they affect the choice, and
ask the user to accept or adjust the proposal.

Defer low-level libraries and implementation choices that do not affect the
project plan. Do not recommend technology merely because it is popular or
appears in a Blueprint example.

Then present a short "What I think we are building" summary containing:

- confirmed problem, primary user, critical journey, MVP, non-goals, and key
  constraints
- recommended but not yet accepted technology choices, with their rationale
- non-blocking open questions

Ask the user to confirm or correct the product understanding and accept or
adjust each proposed technology choice before drafting.

### 4. Prepare an exact, reviewable draft

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
signals with the problem or MVP, and put explicit non-goals with the MVP. In the
Tech section, name each accepted technology, its role, and the important reason
or constraint behind it. Keep recommendations distinct from accepted choices.
Keep the document concise; use short paragraphs or bullets where they improve
clarity.

Do not present the plan as ready while a blocking TODO remains. Show the complete
proposed contents and ask for approval or corrections. Do not create or write
the file until the user explicitly approves the draft.

### 5. Write and hand off

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
- Recommend technology only after the product and important constraints are
  understood.
- Treat `blueprint/project-plan.md` as user-owned project state.
- Keep the interview adaptive; stop asking when the definition-of-ready is met.
