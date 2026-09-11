---
name: commit
description: Commit the staged work on a feature branch and open a PR.
disable-model-invocation: true
---

# Commit

Call the Skill tool with `committing-changes`. If arguments are passed, treat them as the intended commit message or scope hint; otherwise let the skill infer the message from the staged diff.

The skill is the single source of truth for:

- Commit-message rules (capital start, 72 chars or less, no trailing period, no attribution trailers, one logical change per commit).
- Branch protection (never push to main, never force-push, never merge a PR on the user's behalf).
- Hook installation (commit-msg + pre-commit + pre-push) and the optional PR-size CI gate.

Echo any state-changing `git` or `gh` command back to the user before running it.
