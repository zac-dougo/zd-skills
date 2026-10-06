## What it does

Designs the interfaces, data flow, and operational decisions a change needs. The depth follows uncertainty and impact: a small change can receive a short plan, while a migration may need a durable design.

## When to reach for it

Ask for architecture or a consequential design decision, or invoke `$designing-architecture` in Codex or `/designing-architecture` in Claude Code. Use the design shortcut when you want a design-only result.

## Common questions

**Will it survey libraries for every feature?**

No. It starts with the existing project and researches alternatives when a dependency decision is actually open.

**Does it stop after designing?**

A design-only request ends with the plan. When design is part of an authorized implementation task, work continues once consequential decisions are settled.

## It's working if

- The design names the interfaces and contracts that change.
- Tradeoffs and verification match the actual requirement.
- Unresolved consequential choices are visible.

## Where it fits

It prepares work for implementation and subsequent code-review. Shared working guidance supplies engineering defaults. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
