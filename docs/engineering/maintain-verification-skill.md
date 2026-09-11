## What it does

`maintain-verification-skill` keeps a project's verification skill and feature map honest: index hygiene, a read-only source wave per feature, reconciliation, a live pass driving every feature, triage into doc drift / harness gap / product gap, and at most one PR of proven corrections.

Its defining constraint is the outcome contract: clean (no branch, no PR), changed (one PR, re-read first), or blocked (say exactly what blocked). A maintenance run that edits product code or ships unproven corrections has failed.

## When to reach for it

You invoke this by typing `/maintain-verification-skill`, and the agent won't reach for it on its own. Reach for it periodically as the app changes, or when a verification run starts failing and the map is suspect.

| Your situation | Reach for |
| --- | --- |
| The map may have rotted | `maintain-verification-skill` |
| No verification skill exists yet | [create-verification-skill](https://aihero.dev/skills-create-verification-skill) |
| The app itself is broken | Fix the product first; the map records behavior, it doesn't excuse regressions |

## The live pass is mandatory

Source review alone never passes a run. Every feature gets driven at least once against the skill's own launch model, with three invariants held throughout: drive only health-checked instances, evidence survives every cleanup, and nothing a drive started outlives its usefulness. A feature that can't be reached is `verified-unreachable` only with the concrete prerequisite and the route attempted.

## Common questions

**What happens to product bugs found mid-run?**
They're recorded for the user and kept out of the PR. The maintenance PR carries doc, harness, and map corrections only; a regression papered over in docs is worse than a stale map.

## It's working if

- The outcome was declared as clean, changed, or blocked, honestly.
- Every feature file has a returned source summary behind it.
- The shipped PR (if any) contains only corrections that were proven live.

## Where it fits

`maintain-verification-skill` is the upkeep loop for what [create-verification-skill](https://aihero.dev/skills-create-verification-skill) generates. Run notes stay in scratch space, uncommitted; the map stays committed, since it is the repo's verification source.
