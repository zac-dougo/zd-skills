---
name: design
description: Produce a pre-implementation architecture plan for a feature.
disable-model-invocation: true
---

# Design

Call the Skill tool with `designing-architecture` on the design question passed as arguments. The skill is the single source of truth for the research budget, the candidate-comparison rubric, and the output shape (components, data flow, ASCII diagram, hand-off plan).

Read-only: this skill never edits the diff or implements. The output is an implementation plan for the engineering team to execute.

Compose with the repo's language conventions for the target stack and with `engineering-philosophy`.
