---
name: designing-architecture
description: Design components, interfaces, data flow, and migrations before implementation. Use for a requested architecture plan or a consequential design decision.
---

# Designing architecture

Read [working guidance](../../shared/working-guidance.md) once for this task. Produce a design at the depth the decision needs. A design-only request ends with a plan; when design is part of an authorized implementation task, continue into implementation once consequential questions are settled.

## Start from the project

Read the relevant code, architecture notes, contracts, and constraints. Separate agreed requirements from assumptions and open decisions. Resolve routine details using existing conventions; ask about choices that materially affect scope, behaviour, compatibility, or operations.

For a small change, a short explanation of the affected interface, the chosen approach, and verification can be enough. Use a fuller design for new subsystems, uncertain integration, migrations, or substantial operational risk.

## Investigate decisions that are actually open

Prefer existing project capabilities when they meet the requirements. Research alternatives when choosing a new dependency or when evidence suggests the current approach cannot meet a concrete need. Verify relevant support, compatibility, maintenance, licensing constraints, and deployment requirements in primary sources. Popularity and recent commits are signals, not selection rules or proof of suitability. See [research sources](reference/qualified-sources.md) when an external choice is needed.

Compare only plausible alternatives and state the tradeoff driving the choice. Do not require a library survey for work that uses an established dependency unchanged.

## Describe the resulting behaviour

Define the interfaces and ownership that matter, the data flow, and relevant failure handling. Use a diagram when it makes the relationships clearer. Consult [pattern examples](reference/pattern-catalogue.md) only when a concrete design problem warrants it; a named pattern is optional.

For data changes, describe invariants, access patterns, transaction boundaries, and the migration's compatibility requirements. Choose storage and indexes from the workload and query plans. Explain consistency and availability during failures when relevant instead of reducing the choice to a generic checklist.

Address configuration, permissions, secrets, retries, and recovery only where the change introduces or alters them. Distinguish measured performance from targets and estimates.

## Make the plan executable

State the chosen design and its rationale, affected contracts, dependency order, meaningful verification, and unresolved consequential decisions. Scale the document to the change. Use vertical increments where they can remain useful and verifiable; do not force every step into one testing technique.

Behaviour changes need checks that could detect the relevant failure. Existing tests, focused regression tests, an integration exercise, or direct observation may be appropriate. Run required project gates during implementation. Save a document when requested or when its durability helps future work; otherwise an inline plan is sufficient.
