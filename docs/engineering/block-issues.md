## What it does

`block-issues` creates one GitHub issue per Spec Kit `tasks.md` block through the `creating-block-issues` skill: a minimal body (pointer, heading, one-line summary, task IDs) with a dispatch label, plus native Blocked-by relations.

The bodies stay minimal on purpose. The issue points at `tasks.md` as the source of truth; anything copied into the body drifts the moment the file moves.

## When to reach for it

You invoke this by typing `/block-issues`, and the agent won't reach for it on its own. It applies only to Spec Kit projects (a `.specify/` directory and block-structured `tasks.md`) with a GitHub remote.

| Your situation | Reach for |
| --- | --- |
| A Spec Kit feature needs per-block tracking issues | `block-issues` |
| Only part of the work needs an issue | Pass `--tasks` and `--title` for a single subset issue |
| No Spec Kit structure exists | Create issues manually with `gh issue create` |

## Common questions

**Why not one issue per task?**
Granularity. A feature's tasks would swamp the board fifty-to-one, and the assignee would thread them back into per-block PRs anyway. One block maps cleanly to one PR.

## It's working if

- Each issue body matches the template exactly: pointer, block, summary, task IDs, nothing else.
- Every issue carries the dispatch label, and Blocked-by relations mirror the `tasks.md` graph.
- The resolved `<owner>/<repo>` was echoed before anything was created.

## Where it fits

`block-issues` is the user-invoked front door to [creating-block-issues](https://aihero.dev/skills-creating-block-issues), which owns the template, the modes, and the safety rules it follows. Downstream, [block-implement](https://aihero.dev/skills-block-implement) consumes exactly the issues this skill creates.
