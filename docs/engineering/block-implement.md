## What it does

`block-implement` implements one Spec Kit `tasks.md` block end to end through the `implementing-blocks` skill: branch setup, TDD-strict implementation, multi-pass review with a fix loop, final gates, PR, and a CI fix loop.

One invocation is one block is one PR. Anything wider gets split before it starts, never during.

## When to reach for it

You invoke this by typing `/block-implement`, and the agent won't reach for it on its own. Pass a block name verbatim, a task-ID range, `next`, or nothing to analyse and propose. It applies only to Spec Kit projects with a GitHub remote.

| Your situation | Reach for |
| --- | --- |
| A Spec Kit block is ready to build | `block-implement` |
| No Spec Kit structure exists | Build with `tdd`, then [code-review](https://aihero.dev/skills-code-review) |
| The block's issues don't exist yet | [block-issues](https://aihero.dev/skills-block-issues) first |

## Common questions

**What happens when review findings survive three iterations?**
The skill halts. It does not push, does not auto-resolve, and surfaces the unfixed issues for human review. The iteration cap is the point: a fourth round is a design problem, not a fix problem.

## It's working if

- The branch follows the block naming convention and the baseline SHA is printed before implementation.
- Every fix commit maps to a review finding, and review re-runs against each new HEAD.
- The run ends at an open, CI-green PR. Merging stays human.

## Where it fits

`block-implement` is the user-invoked front door to [implementing-blocks](https://aihero.dev/skills-implementing-blocks), which owns the phases, the TDD fence, and the iteration caps it enforces. Upstream, its issues come from [block-issues](https://aihero.dev/skills-block-issues); inside, it drives [running-tdd-cycles](https://aihero.dev/skills-running-tdd-cycles), [reviewing-changes](https://aihero.dev/skills-reviewing-changes), and [committing-changes](https://aihero.dev/skills-committing-changes).
