## What it does

`tdd` drives a red-green-refactor cycle on one requirement through the `running-tdd-cycles` skill: one failing test, the minimal code to pass it, a refactor under green, then the next requirement.

It does no designing itself. The cycle assumes the requirement is already settled; anything undecided goes back to grilling, not into the test.

## When to reach for it

You invoke this by typing `/tdd`, and the agent won't reach for it on its own. Pass the requirement, optionally naming one phase (`red`, `green`, `refactor`) to run just that phase.

| Your situation | Reach for |
| --- | --- |
| One concrete behaviour to build test-first | `tdd` |
| A whole spec sliced into tickets | Build per ticket, then [code-review](https://aihero.dev/skills-code-review) |
| A design question no test can settle yet | [prototype](https://aihero.dev/skills-prototype) |

## Common questions

**Can it run just one phase?**
Yes. Name `red`, `green`, or `refactor` in the invocation and it runs only that phase against the current state.

## It's working if

- The test fails before the implementation exists, and the failure names the missing behaviour.
- The implementation is the smallest change that turns it green.
- The test file is untouched between red and green.

## Where it fits

`tdd` is the user-invoked front door to [running-tdd-cycles](https://aihero.dev/skills-running-tdd-cycles), which holds the loop, the anti-patterns, and the validation checkpoints it enforces. In the main build chain it lives inside the build step: `grill-with-docs → to-spec → to-tickets → build → code-review`, one cycle per ticket.
