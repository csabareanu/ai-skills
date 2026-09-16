---
name: start-project
description: "Start a greenfield Blueprint project before application scaffolding. Interview for product intent and MVP scope, recommend a fitting technology stack, confirm shared understanding, draft the user-owned project plan, and scaffold only after separate approval. Use when the Blueprint skills are linked into an empty or near-empty repository and the user wants to start a new application. For an already scaffolded early app, use onboard and project-plan; for meaningful shipped behavior, use adopt."
---

# start-project - discover before scaffolding

## Where it fits

The preferred greenfield path is:

    link Blueprint skills -> [start-project] -> scaffold -> copy Blueprint state -> /onboard -> /build-plan -> /overview

Use this skill before a framework choice has been locked in. Its job is to make
the product, MVP boundary, and technology decision explicit before application
files or dependencies are generated.

`/start-project` is available from the consuming repository's
`.agents/skills/start-project` link or copy. It is not a global skill and does
not install itself.

## Input

No formal brief is required. Use any idea, constraints, preferred technologies,
project name, or target path already supplied by the user. Do not ask again for
information that is already available.

## Step 0 - confirm this is a safe greenfield start

Inspect the current working directory and git status before interviewing.

- Proceed when there is no meaningful application code yet. A git repository,
  linked Blueprint skills, and untouched Blueprint worksheet files are fine.
- If an application has already been scaffolded but has no meaningful shipped
  behavior, hand off to `/onboard` and then `/project-plan`.
- If the repository has meaningful shipped behavior, hand off to `/adopt`.
- If `blueprint/project-plan.md` contains substantive user-owned decisions, do
  not overwrite it. Ask whether the user wants to continue from that plan or
  make a targeted edit.
- Preserve unrelated files and local changes. Never delete or force-overwrite
  files to make a scaffolder accept the directory.

Do not create files, initialize a framework, or install dependencies during this
check.

## Step 1 - discover the product

Ask the highest-value unanswered question one at a time. Include a suggested
answer when the user's idea provides enough evidence, together with the main
implication. Do not turn every topic into a mandatory questionnaire.

Establish:

- the problem and desired outcome
- the primary user and their critical journey
- the smallest recognizable MVP
- explicit non-goals and success signals
- important data, ownership, sensitivity, or retention needs
- required integrations or platform capabilities
- relevant business, visual, deployment, budget, or compliance constraints

Challenge vague scope, bundled features, and solution-first assumptions. Keep
asking until the problem, user, critical journey, MVP boundary, non-goals, and
hard constraints are coherent. Stop early if the user asks to see the current
understanding; record non-blocking uncertainty as an open question.

## Step 2 - run a technology-fit consultation

Choose technology only after the product shape is clear. Ask only questions
whose answers could materially change the stack, architecture, deployment, or
roadmap. Relevant topics include:

- target platform and delivery shape, such as web, mobile, desktop, CLI, API,
  background processing, offline use, or real-time collaboration
- the user's existing experience and whether the priority is shipping quickly,
  learning, portability, or long-term operation
- data shape, scale expectations, search, files, real-time needs, and external
  integrations
- hosting preferences, budget, compliance, privacy, regional, or operational
  constraints

Avoid selecting low-level libraries that can safely wait for feature design or
implementation.

When the user has not already made an informed stack choice:

1. Recommend one coherent stack and explain briefly how it fits the product and
   the user's constraints.
2. Offer one alternative only when it exposes a meaningful tradeoff.
3. Clearly label both as proposals, not accepted decisions.
4. Verify current, unstable claims such as provider support, compatibility, or
   pricing against authoritative sources when they affect the recommendation.
5. Ask the user to accept or adjust the recommendation.

Do not recommend technology merely because it is popular or present in a
Blueprint example.

## Step 3 - confirm shared understanding

Present a concise review packet with these labels:

- **Confirmed** - problem, primary user, critical journey, MVP features,
  non-goals, and constraints the user has accepted
- **Recommended** - technology choices proposed by Codex, with a short rationale
- **Open questions** - non-blocking decisions that can wait

State the MVP as a concrete feature list. Ask the user to correct the product
understanding and accept or adjust the technology recommendation. Do not draft
the plan while a contradiction or blocking decision remains.

## Step 4 - draft and approve the project plan

Prepare the complete contents of `blueprint/project-plan.md` using this shape:

    # Project Plan

    ## 1. Problem - What problem are we solving?
    ## 2. Users - Who is this for?
    ## 3. Features - What does the MVP need?
    ## 4. Data - What are we storing?
    ## 5. Tech - What stack are we using?
    ## 6. Monetize - How will this make money?
    ## 7. UI/UX - How should this look and feel?
    ## 8. Deployment - Where and how will this ship?

Replace worksheet prompts with actual decisions. Include success signals and
non-goals with the problem or MVP. In the Tech section, name each accepted
technology, its role, and the important reason or constraint behind it. Keep
unresolved non-blocking matters as `> Open question: ...` and never present a
recommendation as accepted.

Show the exact draft and ask for approval. After approval, create
`blueprint/project-plan.md` or replace only an untouched worksheet. Create the
`blueprint/` directory when it is absent. Do not create the build plan, generated
overview, application code, or git commits here.

## Step 5 - propose scaffolding separately

Derive an exact scaffold command from the accepted stack. Before running it,
show:

- the command and working directory
- the runtime and package manager it will use
- the important options selected
- the files or directories it is expected to create
- whether it installs dependencies or initializes git

Ask for separate explicit approval to run that exact command. Approval of the
project plan is not approval to scaffold, install dependencies, initialize git,
or contact external services.

After approval:

- re-check the target directory for conflicts
- run only the approved command
- do not add force, overwrite, or cleanup flags that were not approved
- if the scaffolder cannot safely operate beside `.agents/` or
  `blueprint/project-plan.md`, stop and propose a safe target or staging approach
  rather than deleting workflow files
- verify the command succeeded by inspecting the generated manifest, lockfile,
  framework configuration, and available scripts
- report partial output honestly if scaffolding fails; do not improvise repeated
  destructive retries

If the user prefers to run the command manually, stop with the exact command and
resume verification after they report completion.

## Step 6 - hand off to repository setup

After successful scaffolding, report:

- the agreed product and MVP in one short summary
- the accepted stack and why it was selected
- the scaffold command and verification evidence
- open questions and assumptions
- the created project-plan path
- that the remaining Blueprint state templates must be copied with no-clobber
  semantics if they are not present yet
- the next command: `/onboard` (or `$onboard` in Codex)

`/onboard` owns repository setup, real command detection, coding standards,
ignore rules, adapter decisions, and comparison of the scaffolded stack with the
approved plan. `/build-plan` follows onboarding because it turns the approved MVP
into ordered feature slices.

## Rules

- Product understanding comes before technology selection.
- Ask one question at a time and stop when the decisions are sufficient.
- Keep confirmed decisions, recommendations, and open questions distinct.
- Recommend a coherent default rather than a catalog of tools.
- Do not invent product requirements, accepted technologies, or constraints.
- Never run a scaffold command or dependency installation without separate
  explicit approval of the exact command.
- Never force a scaffolder through file conflicts or delete Blueprint files.
- Treat `blueprint/project-plan.md` as user-owned project state.
- Do not create commits, push, deploy, provision services, or create external
  resources.

## Formatting

When `blueprint/context/ai-interaction.md` exists, follow its formatting
conventions. Otherwise use concise, scannable Markdown with lists for decisions
and a table only when comparing stacks across the same criteria.
