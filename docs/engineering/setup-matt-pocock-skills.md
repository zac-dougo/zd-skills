## What it does

Configures the repository conventions requested by the user, including trackers and domain docs. Optional hook and CI installation is a separate explicit part of setup and preserves existing configuration.

## When to reach for it

Invoke `$setup-matt-pocock-skills` in Codex or `/setup-matt-pocock-skills` in Claude Code when you want to configure or change project conventions. Ordinary commits do not run setup.

## Common questions

**What if CLAUDE.md exists but I am using Codex?**

The workflow chooses the instruction file the active agent actually loads and preserves a shared source through a pointer when needed.

**Will setup replace custom hooks?**

No. It inspects the hook mechanism and integrates only selected checks. The bundled installers have limited assumptions and must not overwrite different existing files.

**Do I need to answer every setup question again?**

No. It skips choices already established by configuration or the conversation and asks only about unresolved consequential choices.

## It's working if

- Only the requested parts of configuration change.
- The active agent can find the resulting guidance.
- Existing hooks and CI remain intact unless you explicitly requested their replacement.

## Where it fits

This is repository setup for the planning workflows and optional Git checks. committing-changes performs ordinary delivery using those conventions. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
