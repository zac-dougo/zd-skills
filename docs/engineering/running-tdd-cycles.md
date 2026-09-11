## What it does

`running-tdd-cycles` enforces strict red-green-refactor discipline on any code change, in any language: one requirement per cycle, one failing test, the minimal code to pass, a refactor under green, commit, repeat.

Its defining constraint is the fails-for-the-right-reason check. A test that fails on a typo or a bad fixture proves nothing; the failure message must name the missing behaviour, or the cycle restarts at red.

## When to reach for it

Type `/running-tdd-cycles`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires on building or fixing a concrete behaviour test-first.

| Your situation | Reach for |
| --- | --- |
| One concrete behaviour to build test-first | `running-tdd-cycles` (or its front door, [tdd](https://aihero.dev/skills-tdd)) |
| A design question no test can settle yet | [prototype](https://aihero.dev/skills-prototype) |
| A bug with no repro and no seam | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

## The fence

Red, green, refactor, each gated. Red ends only when the test fails for the right reason. Green ends only when the suite passes on the minimum change with the test file untouched. Refactor ends only when the suite is still green and the code is simpler. Break the fence and the recovery is fixed: stop, name the violated phase, revert to the last green state, resume from there.

## Common questions

**Does every cycle end in a commit?**
One logical change per commit, so usually yes: a green-plus-refactor lands as a commit before the next red. The message and branch rules come from [committing-changes](https://aihero.dev/skills-committing-changes).

**Where do exploratory spikes go?**
A gitignored scratch file, never the suite and never production code. Spikes are how you learn the shape; the cycle is how you land it.

## It's working if

- No test in the suite passes on the commit before its implementation.
- Each cycle touches one requirement, and a big-feeling cycle gets split instead of pushed through.
- Refactor commits exist, not just red-green pairs.

## Where it fits

`running-tdd-cycles` is the engine inside the build step of the main chain: `grill-with-docs → to-spec → to-tickets → build → code-review`, one cycle per ticket. Its closest neighbours are [committing-changes](https://aihero.dev/skills-committing-changes), which lands each cycle, and [reviewing-changes](https://aihero.dev/skills-reviewing-changes), which confirms the discipline held at the end.
