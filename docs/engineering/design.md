## What it does

`design` produces a pre-implementation architecture plan through the `designing-architecture` skill: requirements, technology selection with rejected alternatives, patterns, components and data flow, and a TDD-ready step list.

It is read-only. The skill never edits the diff or implements; the plan hands off to `tdd` for execution, and designing stops where building starts.

## When to reach for it

You invoke this by typing `/design`, and the agent won't reach for it on its own. Reach for it when the shape of the solution is still open: which libraries, which patterns, which components.

| Your situation | Reach for |
| --- | --- |
| The architecture is undecided | `design` |
| The plan is settled and needs grilling | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| One design question needs a runnable answer | [prototype](https://aihero.dev/skills-prototype) |

## Common questions

**How is this different from grilling?**
Grilling settles what to build and what words to use for it. This skill settles how to build it: libraries, patterns, components, data flow. A grilled decision is its input, not its output.

## It's working if

- Every recommended library was checked for activity, docs, license, and at least one alternative.
- The plan decomposes into red-green-refactor-sized steps, each independently testable.
- Open questions are listed explicitly instead of decided silently.

## Where it fits

`design` is the user-invoked front door to [designing-architecture](https://aihero.dev/skills-designing-architecture), which owns the research budget, the rubric, and the output shape it follows. Upstream it takes grilled decisions; downstream its step list feeds [running-tdd-cycles](https://aihero.dev/skills-running-tdd-cycles).
