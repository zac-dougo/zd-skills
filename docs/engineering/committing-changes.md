## What it does

`committing-changes` lands work the boring way: feature branch, hooks, lint and format, one logical change per commit, push, PR. It ships the hook scripts and the PR-size gate that enforce the rules, so discipline is installed, not remembered.

Its defining constraint is that the human keeps every irreversible decision. The agent never pushes to main, never force-pushes, and never merges; it opens the PR and stops.

## When to reach for it

Type `/committing-changes`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires whenever work is ready to land. The [commit](https://aihero.dev/skills-commit) skill is its user-invoked front door.

| Your situation | Reach for |
| --- | --- |
| Finished work needs landing | `committing-changes` |
| The repo has no hooks installed yet | Step one of this skill installs them |
| The diff needs a verdict before landing | [review](https://aihero.dev/skills-review) or [code-review](https://aihero.dev/skills-code-review) first |

## Hooks, not memory

The `commit-msg` hook enforces the subject rules (capital start, short, no trailing period, no attribution trailers) and the `pre-push` hook blocks direct pushes to main. The optional PR-size workflow fails PRs over a thousand changed lines. Run the installers once per repo; from then on the rules hold without anyone reciting them.

## Common questions

**Why one logical change per commit?**
Bisect and revert. A commit that does one thing can be blamed, bisected, and reverted surgically; a bundled one can do none of those.

## It's working if

- The branch name carries its type prefix, and main was never pushed to directly.
- Each commit message reads as one imperative sentence.
- Oversized PRs fail in CI before a human ever sees them.

## Where it fits

`committing-changes` closes every build by landing the implementation on a feature branch and opening a reviewable PR. Its closest neighbour is [shell-discipline](https://aihero.dev/skills-shell-discipline): one auditable tool call per git command, no chains.
