---
name: tdd
description: Drive a red-green-refactor TDD cycle on a requirement.
disable-model-invocation: true
---

# TDD

Call the Skill tool with `running-tdd-cycles` on the requirement passed as arguments. The skill is the single source of truth for the red-green-refactor procedure, the fails-for-the-right-reason verification, and the refactor-only-when-green gating.

If the arguments name a phase explicitly (`red`, `green`, `refactor`), run only that phase. Otherwise drive the full cycle.

Compose with the repo's language conventions for the touched files and with `engineering-philosophy`.
