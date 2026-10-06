## What it does

Commits intended changes and completes the requested delivery endpoint. Routine commits preserve existing hooks, CI, and repository configuration; installing new checks is a separate setup task.

## When to reach for it

Ask to commit, push, or open a PR, or explicitly invoke `$committing-changes` in Codex or `/committing-changes` in Claude Code. A local-commit request ends with a local commit; PR delivery includes publishing the feature branch.

## Common questions

**Will it replace my hooks?**

No. It uses existing checks and investigates failures. Optional hook or CI installation belongs to an explicit repository-setup request.

**Can it sync the default branch without merging my PR?**

Yes. Integrating the default branch into a feature branch follows repository policy. Merging the feature branch into the default branch or merging its PR is a separate action controlled by the user.

**Is every PR limited to 1000 lines?**

Only when the repository configures that gate. The skill no longer installs a universal size policy.

## It's working if

- Only intended files appear in the commit.
- Existing hooks and CI remain intact.
- The result reports the requested commit or PR and the checks actually completed.

## Where it fits

The commit shortcut requests this delivery workflow. setup-matt-pocock-skills handles explicitly requested repository configuration. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
