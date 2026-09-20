## What it does

`engineering-philosophy` weights code decisions with KISS, YAGNI, DRY, SOLID, fail-fast, and seventeen other principles. The principles are judgement weights, not rules: when two conflict, the workflow skill driving the task decides which dominates.

It never acts on its own. A philosophy without a workflow is a lecture; this skill only fires underneath real work.

## When to reach for it

The agent reaches for it automatically when a task fits: it is model-invoked, and fires on any code decision with a trade-off in it. Different workflows lean on different weights: design leans KISS and YAGNI, review leans SOLID and fail-fast, TDD leans small steps.

| Your situation | Reach for |
| --- | --- |
| A code decision needs weighting | The philosophy loads underneath the workflow |
| A proposed change violates a principle | Name the principle and its consequence |
| A workflow is already running | The workflow picks the dominant weights |

## Common questions

**What happens when principles conflict?**
The driving skill breaks the tie. During design, simplicity beats completeness; during review, explicitness beats brevity. The skill lists which weights dominate under each workflow so the call is made, not improvised.

## It's working if

- Trade-offs get named as principles with consequences, not asserted as taste.
- Violations are surfaced with the principle named, never silently refused.
- No principle fires where the driving workflow says another dominates.

## Where it fits

`engineering-philosophy` is the vocabulary layer underneath the engineering skills rather than a step in any chain. Its closest neighbours are [designing-architecture](https://aihero.dev/skills-designing-architecture), [code-review](https://aihero.dev/skills-code-review), and [committing-changes](https://aihero.dev/skills-committing-changes).
