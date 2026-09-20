## What it does

`designing-architecture` produces a pre-implementation architecture plan: requirements, evaluated technology candidates with rejected alternatives, patterns, components and data flow, and a TDD-ready step list that hands directly to implementation.

Its defining constraint is minimum viable architecture. Every library is researched before it is recommended, every pattern earns its place against the current feature, and speculative configurability is rejected on sight.

## When to reach for it

Type `/designing-architecture`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires on open architecture questions. The [design](https://aihero.dev/skills-design) skill is its user-invoked front door.

| Your situation | Reach for |
| --- | --- |
| Libraries, patterns, and components are undecided | `designing-architecture` |
| The plan is settled and needs stress-testing | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| One question needs a runnable answer, not a document | [prototype](https://aihero.dev/skills-prototype) |

## Research before recommending

No library enters the plan unchecked: activity, docs, license, dependency footprint, and at least one alternative, verified against official docs rather than star counts. The output is a single Markdown document whose step list is sized for red-green-refactor cycles, so the plan feeds implementation without translation.

## Common questions

**What if the design includes a data layer?**
A database overlay runs as a mini-pipeline inside the same skill: technology family via CAP framing, schema from conceptual to physical, indexing strategy, zero-downtime migration plan, and security. It lands in the same document, not a second one.

## It's working if

- Rejected alternatives are listed with reasons, not silently dropped.
- Each implementation step is independently testable and dependency-ordered.
- Open questions are explicit; nothing load-bearing was decided quietly.

## Where it fits

`designing-architecture` sits ahead of the build: its step list feeds implementation, and [code-review](https://aihero.dev/skills-code-review) later checks the result against the requirements and repository standards. Its closest neighbours are [engineering-philosophy](https://aihero.dev/skills-engineering-philosophy), whose KISS and YAGNI weights dominate during design, and [grill-with-docs](https://aihero.dev/skills-grill-with-docs), which settles the decisions this skill records.
