## What it does

Synthesizes the agreed conversation into a proportionate, verifiable spec. It preserves settled choices and asks only when a missing decision changes the promised behaviour or acceptance criteria.

## When to reach for it

Invoke `$to-spec` in Codex or `/to-spec` in Claude Code after discussing the outcome. Specify a draft or local document when you do not want the configured tracker destination.

## Common questions

**Will it interview me again about the test boundaries?**

Not for routine choices already supported by the project and conversation. Consequential unresolved requirements still need an answer.

**Does every spec need a long list of user stories?**

No. Acceptance criteria cover the actual requirements and relevant failure cases. User stories are used when they clarify those requirements.

**What if no tracker is configured?**

It prepares the complete draft and asks where to publish. It does not guess a destination or mark blocked work ready.

## It's working if

- The spec distinguishes requirements, assumptions, and open decisions.
- Acceptance criteria can be verified.
- The result is published only to the requested or established destination.

## Where it fits

to-tickets can split the spec into deliverable work. code-review checks the implementation against the agreed requirements. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
