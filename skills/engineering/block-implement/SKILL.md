---
name: block-implement
description: Implement one Spec Kit tasks.md block end to end (TDD, review, PR, CI loop).
disable-model-invocation: true
---

# Block Implement

Call the Skill tool with `implementing-blocks`, passing the arguments through as the block filter (a block name verbatim, a task-ID range, `next`, or empty to analyse and propose). The skill is the single source of truth for:

- Spec Kit `tasks.md` parsing and block dependency analysis.
- Block-selection confirmation flow and branch naming.
- TDD-strict implementation with the red-green-refactor fence.
- Multi-pass review via `reviewing-changes` with an iteration cap.
- Language-appropriate final gates.
- Push, PR, CI watch, and CI fix loop with an iteration cap.

Use on a Spec Kit project. Echo any state-changing `git` or `gh` command back to the user before running it.
