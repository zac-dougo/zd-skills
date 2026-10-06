## What it does

Provides a short explicit command for committing intended work, pushing a feature branch, and opening or updating its PR. It delegates the rules to committing-changes so the two workflows stay consistent.

## When to reach for it

Invoke `$commit` in Codex or `/commit` in Claude Code. Include a message or scope hint if helpful. Specify local-only when you do not want publication.

## Common questions

**Does the shortcut install hooks or merge the PR?**

No. It preserves existing checks and leaves PR merging to you unless you explicitly request otherwise.

## It's working if

- The commit contains the intended changes.
- The branch and PR are reported, or the narrower endpoint you requested is honoured.

## Where it fits

This is the explicit shortcut for committing-changes. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
