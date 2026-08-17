# Curriculum Blueprint

## Contents

1. Purpose and resolution
2. Candidate coverage discovery
3. Module and lesson design
4. Source and example spine
5. Assessment and pacing
6. Projects and integration
7. Quality audit
8. Common failure modes

## Purpose And Resolution

Create a concrete first-pass syllabus before detailed lesson delivery. Make the whole learning journey visible enough for the learner to critique while preserving adaptation and just-in-time authoring.

Make the blueprint resemble a complete, well-structured course or book rather than definitions distributed across lesson titles. Give it:

- a deliberate entry point based on the learner's starting evidence
- a central question, performance, artifact, argument, or other through-line
- cumulative modules in which later work uses and transforms earlier learning
- explicit transitions that explain why one module prepares the next
- increasing independence, complexity, ambiguity, or integration
- a culminating performance that resolves the course's central purpose
- a completion boundary that distinguishes a finished course from endless topic accumulation

Use three levels of resolution:

1. `roadmap.md`: capabilities, dependencies, mastery criteria, and evidence status
2. `syllabus.md`: modules, lesson cards, anchors, practice, independent evidence, pacing, and integration milestones
3. `lessons/`: full theory, demonstrations, prompts, materials, solutions, rubrics, and interactive artifacts authored just in time

Do not use the blueprint as proof that content was taught or mastered.

## Candidate Coverage Discovery

Start from the target outcome and diagnostic. Generate candidate coverage from the smallest useful combination of:

- required prerequisites and governing concepts
- representative real-world tasks and failure modes
- authoritative curricula, professional standards, canonical works, or primary sources
- current practice when the subject is changing or source-dependent
- the learner's examples, proposed syllabus, tools, environment, and constraints
- subject-specialist skills when available

Benchmark only when it improves coverage or currency. Prefer a few authoritative references over a broad search. Record important sources or design rationale without copying another curriculum's structure uncritically.

Classify every candidate as `prerequisite`, `core`, `enrichment`, or `advanced`. Do not make a topic core merely because it is recent, popular, difficult, prestigious, or common in a tool ecosystem.

Remove candidates that do not contribute enough to the destination. State deliberate exclusions when a reasonable learner would otherwise expect them.

## Module And Lesson Design

Group capabilities by conceptual dependency and coherent performance, not by brand, tool, chronology, or arbitrary module size.

First design the course arc. Adapt its exact shape to the subject, but normally include:

1. **Orientation and foundations:** establish the problem space, language, prerequisites, and standards of evidence.
2. **Core development:** build the governing concepts, methods, techniques, or source knowledge in dependency order.
3. **Guided integration:** combine capabilities in increasingly realistic, ambiguous, or expressive work.
4. **Limits and variation:** encounter failure modes, counterexamples, alternative interpretations, edge cases, or changed constraints.
5. **Independent synthesis:** complete and defend the final performance, reflect on limitations, and identify legitimate next branches.

These are functional stages, not mandatory module names. Compress, expand, or reshape them when the subject demands another natural arc.

For every module, define:

- purpose and contribution to the destination
- role in the overall course arc
- roadmap capability IDs developed or assessed
- dependencies
- expected entry capability
- exit capability and bridge to the next module
- estimated session range
- expected independent workload
- integration milestone or synthesis task

For every lesson card, define:

- title
- essential question or target capability
- roadmap capability IDs developed or assessed
- key concepts or techniques
- concrete anchors appropriate to the subject, such as systems, cases, source texts, artworks, datasets, scenarios, demonstrations, or materials
- guided practice, lab, problem solving, discussion, rehearsal, critique, or other supported performance
- independent evidence, such as homework, retrieval, transfer, creation, analysis, or demonstration
- dependencies
- approximate session count

State lesson dependencies explicitly, using `none` when there are no prerequisites. Do not rely on module order alone to imply them.

Use concrete anchors to illuminate transferable ideas. For current or proprietary examples, distinguish verified public evidence from analogy or inference.

Keep a lesson coherent. Split a lesson when its concepts, practice, or expected implementation cannot realistically fit the stated session length. Combine lessons when separating them would create disconnected fragments.

Make theory-practice relationships explicit. Do not add a lab merely for activity; identify what concept or capability its evidence can support.

## Source And Example Spine

Curate a small, coherent spine of readings, works, examples, demonstrations, cases, datasets, systems, or other subject-appropriate source material. Organize it by module and state why each item belongs.

Distinguish:

- `required`: central material the planned lesson or practice depends on
- `recommended`: valuable depth or an alternative explanation
- `reference`: material used selectively for lookup, examples, or later work

Prefer primary, authoritative, canonical, or well-supported sources when the subject benefits from them. Use complete courses, books, standards, and established curricula to audit coverage and sequence, but do not reproduce their organization without adapting it to the learner's destination and evidence.

Avoid decorative reading lists. Every required source should prepare a discussion, explanation, practice, assessment, or integration milestone. For current material, record enough source context to revisit freshness later.

## Assessment And Pacing

Create an assessment architecture that maps the syllabus back to the roadmap:

- identify which lessons develop each roadmap capability
- identify where each core capability receives independent mastery evidence
- schedule formative checks before high-stakes or integrative work
- schedule retrieval after delay when retention matters
- include revision, reassessment, or a new transfer case after important feedback
- state meaningful conditions such as allowed references, collaboration, tools, time, or support

Do not require a separate graded artifact for every lesson. Assess coherent capability clusters when that produces stronger and more authentic evidence.

Make pacing honest. Estimate both guided session time and independent workload. Reserve capacity for retrieval, discussion, debugging, critique, remediation, reassessment, and project integration. Do not schedule every available session with new content.

Name adaptation checkpoints where evidence may justify remediation, acceleration, test-out decisions, optional depth, or a revised practice form. Preserve the target outcome unless the learner approves a material change.

## Projects And Integration

Use a progressive project or performance ladder when integration matters:

1. focused practice that isolates a new capability
2. an intermediate artifact combining several capabilities
3. failure, critique, revision, or transfer that exposes limits
4. a final performance aligned with the completion evidence

Prefer one evolving artifact when continuity improves learning. Use several smaller artifacts when variety and transfer matter more.

Define project requirements by observable behavior, constraints, quality, and defense. Do not use component count, tool count, length, or superficial complexity as a proxy for mastery.

Schedule design reviews, critiques, oral defenses, demonstrations, or troubleshooting checkpoints before the final submission when those performances matter to the destination.

## Quality Audit

Before presenting or saving the blueprint, verify:

- Every module contributes materially to the target outcome.
- Every core roadmap capability appears in the blueprint, and every blueprint lesson maps to a capability or justified enrichment goal.
- The beginning is justified by the learner's entry point and the end matches the promised destination.
- A clear through-line connects modules into one course rather than a collection of definitions or standalone units.
- Every module has an exit capability and prepares a named later demand.
- Definitions and prerequisites precede the capabilities that depend on them.
- The sequence develops depth rather than repeating labels at increasing scale.
- Core concepts have concrete anchors and meaningful practice.
- Core capabilities have independent, observable evidence.
- Required sources and concrete anchors have a stated instructional purpose rather than forming a decorative bibliography.
- Labs, exercises, and performances test the claimed behavior, including relevant failures and limits.
- Projects integrate prior learning without introducing uncontrolled scope.
- The workload fits the learner's cadence and the estimated session range.
- The pacing includes independent work, delayed retrieval, integration, and realistic buffer for adaptation.
- Optional material is visibly separate from the core path.
- Current topics are classified by relevance rather than novelty.
- Named tools, technologies, works, or methods are justified by what they teach.
- Comparison tasks specify a decision context and criteria.
- The final evidence samples explanation, application, diagnosis, and transfer as appropriate.
- The plan leaves room for remediation, test-out decisions, retrieval, and learner-directed branches.

If the audit reveals too much material, protect the destination and core depth first. Move valuable excess into enrichment or advanced branches instead of compressing every topic into shallow exposure.

## Common Failure Modes

Avoid:

- a catalog of topics without dependencies or mastery evidence
- lessons that do not map to a roadmap capability or justified enrichment goal
- a glossary, encyclopedia outline, or table of definitions disguised as a course
- modules that could be arbitrarily reordered because they do not build on one another
- an abrupt beginning with no orientation or an endless ending with no completion boundary
- a tool, technology, author, or brand shopping list presented as a curriculum
- memorable theories introduced before their terms and assumptions are understood
- `build X` assignments without constraints, scaffolding, checks, or a learning purpose
- comparisons without a workload, audience, decision context, or evaluation criteria
- projects rewarded for size, component count, or accidental complexity
- one lesson hiding a multi-session implementation, proof, performance, or creative process
- repeated survey coverage that displaces deep practice
- reading or resource lists whose role in learning is unspecified
- pacing that allocates every session to new material and leaves no room for retrieval, feedback, or remediation
- speculative descriptions of proprietary systems or unverifiable current practice
- fashionable specializations displacing required foundations
- fully authored lessons and solutions before learner evidence can shape them
