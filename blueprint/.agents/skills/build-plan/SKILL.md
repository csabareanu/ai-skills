---
name: build-plan
description: "Create the first user-owned Blueprint build roadmap from an approved project-plan.md. Confirm the product interpretation, run an adaptive roadmap grill for scope and sequencing, decompose the MVP into ordered feature outcomes, and show the exact numbered checklist for approval before creating or writing blueprint/build-plan.md. Use when the user runs /build-plan, invokes $build-plan, or asks to turn a project plan into an implementation roadmap. For an existing codebase whose shipped behavior must first be reflected in the plans, use /adopt instead."
---

# build-plan - turn product scope into build slices

## Where it fits

The new-project path is:

    /project-plan -> /build-plan -> /overview -> /brief -> /feature -> /implement

`project-plan.md` defines the product direction. Turn its approved MVP into an
ordered roadmap of feature outcomes here. Leave feature-level implementation
details and splitting to `/feature`.

## Workflow

### 1. Check inputs and protect existing plans

Read `blueprint/project-plan.md` and `blueprint/build-plan.md`.

- If the project plan is missing, empty, or still a worksheet, stop and hand off
  to `/project-plan`.
- If `> TODO (blocking)` decisions prevent a coherent MVP or build order, list
  them and stop until the user resolves them. Carry non-blocking
  `> Open question` entries forward when appropriate.
- If the build plan is missing, empty, untouched, or only contains placeholder
  examples, continue and create it after approval.
- If the build plan contains substantive user-owned roadmap items, stop. Report
  that this skill initializes a plan; do not overwrite or silently restructure
  it. If the project overview is absent or no longer reflects the plans, hand off
  to `/overview`; otherwise hand off to `/feature`.

Do not modify either planning file during this check.

### 2. Confirm the product interpretation

Summarize the approved project plan in a few bullets:

- problem and primary user
- critical user journey
- MVP boundary and explicit non-goals
- important constraints and dependencies

Ask the user to correct only material misunderstandings. If a correction changes
product scope, stop and propose the corresponding targeted
`blueprint/project-plan.md` edit before planning against it.

### 3. Run the roadmap grill

Do not repeat the full product interview. Ask the highest-value unresolved
sequencing question one at a time. Include a suggested answer only when the plan
supports it, with a brief tradeoff.

Apply a roadmap-impact test before asking: different plausible answers must
change a feature boundary, dependency, MVP inclusion, or build order. Otherwise,
do not ask. Carry the matter as a non-blocking implementation choice for
`/feature` or `/implement`. In particular, do not select vendors, libraries,
schema details, endpoint shapes, or deployment settings unless that choice
materially changes the roadmap.

Aim for one to three roadmap questions. Re-check readiness after every answer
and stop immediately when the first useful slice, major dependencies, MVP order,
and deferred scope are clear.

Challenge:

- the smallest release that delivers recognizable value
- capabilities that unlock later outcomes
- work that can be deferred without weakening the core value
- items that are infrastructure tasks rather than product outcomes
- premature assumptions about auth, billing, administration, integrations, or
  deployment

Stop when the smallest useful first slice, major dependencies, MVP ordering, and
deferred scope are clear.

### 4. Derive and red-team the roadmap

Build a short ordered set of feature-sized outcomes:

- trace every MVP item to the approved project plan
- state the user or domain outcome, not a list of coding tasks
- keep each item independently understandable and reviewable
- order items by prerequisites and shortest path to a useful product
- include data, auth, integration, or deployment work only when it enables a
  concrete outcome at that point
- make the first item the smallest useful vertical slice
- leave implementation steps and non-obvious sub-feature splitting to
  `/feature`

Do not add ideas merely because they are common for the stack. Do not turn
project-plan non-goals into Post-MVP work automatically. Include a deferred idea
under `## Post-MVP` only when the user explicitly wants it tracked.

Before review, confirm that no item hides unrelated outcomes, no prerequisite is
missing, infrastructure is not planned for its own sake, scaffolding and
temporary prototypes are absent, and no blocking TODO remains.

### 5. Prepare an exact, reviewable draft

Use this output shape:

    # Build Plan

    > Living roadmap. Keep completed item numbers stable and append new work
    > using the next unused number.

    ## MVP

    - [ ] 1. **Feature title** - concrete user or domain outcome
    - [ ] 2. **Feature title** - concrete user or domain outcome

    ## Post-MVP

    - [ ] 3. **Deferred feature** - concrete outcome

Require sequential numbers and unchecked boxes for a new project. Omit
`## Post-MVP` when there is no approved deferred work. Remove all worksheet
instructions, Good/Avoid examples, and placeholder items such as `Feature one`
and `Feature two`.

Show the complete roadmap, its ordering rationale, and any non-blocking open
questions. Ask the user to approve or adjust it. Do not create or write the file
until the user explicitly approves the proposal.

### 6. Write and hand off

After approval, create or replace only `blueprint/build-plan.md`. Do not edit
`blueprint/project-plan.md`, `blueprint/context/project-overview.md`, skills,
source code, dependencies, or git state.

Report:

- the MVP ordering and explicitly deferred items
- non-blocking open questions or assumptions
- the next command: `/overview` (or `$overview` in Codex)

## Rules

- Treat this as roadmap definition, not implementation or detailed design.
- Never scaffold, install dependencies, run migrations, or change application
  code.
- Never overwrite a substantive build plan in this create-only workflow.
- Prefer a short roadmap that can evolve over a speculative master plan.
- Treat both planning files as user-owned project state.
- Keep the grill adaptive; stop asking when the definition-of-ready is met.
