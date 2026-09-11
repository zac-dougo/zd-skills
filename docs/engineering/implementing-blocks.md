## What it does

`implementing-blocks` implements one Spec Kit `tasks.md` block end to end: branch setup, TDD-strict implementation in a subagent, multi-pass review with a capped fix loop, language gates, PR, and a capped CI fix loop.

Its defining constraint is the iteration budget. Review-fix cycles and CI-fix cycles each get three rounds; what survives the budget halts for a human instead of looping forever.

## When to reach for it

Type `/implementing-blocks`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires on Spec Kit projects with block-structured `tasks.md`. The [block-implement](https://aihero.dev/skills-block-implement) skill is its user-invoked front door.

| Your situation | Reach for |
| --- | --- |
| A Spec Kit block is ready to build | `implementing-blocks` |
| No Spec Kit structure exists | [running-tdd-cycles](https://aihero.dev/skills-running-tdd-cycles), [reviewing-changes](https://aihero.dev/skills-reviewing-changes), and [committing-changes](https://aihero.dev/skills-committing-changes) directly |
| The block's tracking issue doesn't exist yet | [block-issues](https://aihero.dev/skills-block-issues) first |

## The TDD fence

The implementation subagent works under a non-negotiable fence: failing tests first (confirmed failing for the right reason), minimal code after, refactor only under green, tasks marked done only when green. The fence travels inside the subagent prompt verbatim, so it holds even where the orchestrator can't see.

## Common questions

**Why a subagent for implementation?**
Context hygiene. The orchestrator keeps the review loop and CI loop bookkeeping; the implementer holds only red, green, and refactor. Findings from later review rounds never pollute the builder's context.

## It's working if

- The filter was validated against `tasks.md` before any subagent saw it.
- Every fix commit maps to a review finding, and review re-ran after each.
- The run ends at an open, CI-green PR, or halted loudly at a spent budget.

## Where it fits

`implementing-blocks` is the whole Spec Kit build chain in one skill: it drives [running-tdd-cycles](https://aihero.dev/skills-running-tdd-cycles), [reviewing-changes](https://aihero.dev/skills-reviewing-changes), and [committing-changes](https://aihero.dev/skills-committing-changes) in sequence. Upstream, its issues come from [creating-block-issues](https://aihero.dev/skills-creating-block-issues).
