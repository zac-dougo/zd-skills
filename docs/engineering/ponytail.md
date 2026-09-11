## What it does

`ponytail` makes the agent think like the laziest senior dev in the room: the best code is the code never written. Every task climbs a ladder that stops at the first rung that holds: does it need to exist, does the codebase already have it, does the stdlib, does the platform, does an installed dependency, can it be one line.

Its defining constraint is that laziness shortens the solution, never the reading. The ladder runs after the problem is fully understood, not instead of understanding it; the smallest change in the wrong place is a second bug.

## When to reach for it

Type `/ponytail`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires on any coding task (writing, fixing, refactoring, reviewing, designing, choosing dependencies) or when the user asks for the simplest path. It stays active every response until stopped, at intensity `full` unless told otherwise.

| Your situation | Reach for |
| --- | --- |
| Code is ballooning past the need | `ponytail` at `full` |
| A proposal just needs a second opinion | `lite`: build it, name the lazier path |
| Everything looks speculative | `ultra`: delete first, defend the rest |

## The ladder

Existence, reuse, stdlib, platform, installed dependency, one line, and only then new code. Bug fixes climb it too: the lazy fix is the root-cause fix, one guard where all callers route through instead of a guard per caller. Deliberate simplifications that cut a real corner get a `ponytail:` comment naming the ceiling and the upgrade path.

## Common questions

**Does lazy mean no tests?**
No. Non-trivial logic leaves one runnable check behind, the smallest thing that fails if the logic breaks. Trivial one-liners need nothing; YAGNI applies to tests too.

**What stays non-negotiable?**
Validation at trust boundaries, error handling that prevents data loss, security, accessibility, and anything explicitly requested. The user insisting on the full version ends the discussion.

## It's working if

- The diff is shorter than the first instinct, and every removed line has a rung that removed it.
- Explanations stay under three lines unless explicitly asked for.
- Corners cut on purpose carry a `ponytail:` comment; corners cut by accident don't happen, because the reading came first.

## Where it fits

`ponytail` is a lens that rides along on any coding work rather than a step in any chain. Its closest neighbours are [engineering-philosophy](https://aihero.dev/skills-engineering-philosophy), whose YAGNI and simplicity weights it sharpens into a procedure, and [reviewing-changes](https://aihero.dev/skills-reviewing-changes), which catches the over-building this skill is meant to prevent.
