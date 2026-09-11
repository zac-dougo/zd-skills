## What it does

`commit` lands the staged work on a feature branch and opens a PR. It runs the `committing-changes` skill: branch check, lint and format, one logical change per commit, push, PR creation.

It never merges. The human keeps the merge decision; the skill's job ends at a pushed branch with a PR open.

## When to reach for it

You invoke this by typing `/commit`, and the agent won't reach for it on its own. Pass a message or scope hint, or nothing and the message is inferred from the staged diff.

| Your situation | Reach for |
| --- | --- |
| Staged work is ready to land | `commit` |
| The diff itself needs a verdict first | [review](https://aihero.dev/skills-review) or [code-review](https://aihero.dev/skills-code-review) |
| Work is mid-flight and uncommitted | Commit first, then review; neither review skill sees uncommitted work |

## Common questions

**Does it push to main?**
Never. It switches to a feature branch first, and the installed hooks block a direct push to main if one slips through.

## It's working if

- You are on a feature branch, or were moved onto one before anything else.
- The commit subject starts with a capital, stays short, and carries no attribution trailers.
- A PR exists after the first push, and nothing was merged.

## Where it fits

`commit` is the user-invoked front door to [committing-changes](https://aihero.dev/skills-committing-changes), which owns the branch, hook, message, and PR rules it follows. It sits at the tail of any build: after the tickets are built, after [code-review](https://aihero.dev/skills-code-review) passes.
