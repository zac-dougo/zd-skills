## What it does

Sharpens a plan through focused questions while recording settled terminology and consequential decisions. It composes grilling with domain-modeling, loading their actual instructions through portable file references.

## When to reach for it

Invoke `$grill-with-docs` in Codex or `/grill-with-docs` in Claude Code in the project whose domain docs you want maintained.

## Common questions

**Will it require a special Skill tool?**

No. The agent can read and follow the referenced files directly. It uses a dedicated invocation tool only when one is available.

**Does every answer become an ADR?**

No. The domain-modeling workflow decides which settled decisions deserve durable records; routine discussion is not a decision diary.

## It's working if

- The questions focus on decisions that matter.
- Settled terminology and significant decisions appear in the appropriate project docs.

## Where it fits

Use grill-me for a discussion without file changes, and to-spec to capture an agreed outcome as implementation requirements. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
