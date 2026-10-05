## What it does

Captures established working preferences in one maintained source. Routine preferences belong in shared instructions; an optional personal mode is created only when that is what the user wants.

## When to reach for it

Invoke `$automate-me` in Codex or `/automate-me` in Claude Code when you want to establish or revise how an agent works with you.

## Common questions

**Do I need another mode skill for everyday preferences?**

No. A shared instruction file can hold standing preferences. A mode skill is useful for behaviour you want to switch on explicitly.

**Will one conversation become a universal rule?**

An explicit standing preference can be recorded immediately. An inferred pattern needs stronger evidence, and an isolated incident should not become a blanket rule.

**Does changing preferences automatically publish a PR?**

No. Publication follows the scope you requested. Existing authorization is respected without an extra approval round.

## It's working if

- The result records concrete preferences without duplicating other rules.
- Unrelated existing instructions are preserved.
- You can tell whether the preferences apply routinely or only when invoked.

## Where it fits

reflect finds lessons in completed work; this workflow establishes where durable preferences belong. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
