## What it does

Reviews a completed session for lessons that would change future behaviour. It handles small corrections inline and uses independent review only when the lesson warrants it and delegation is permitted.

## When to reach for it

Invoke `$reflect` in Codex or `/reflect` in Claude Code after a correction or workflow problem. A session with no durable lesson needs no edit.

## Common questions

**Does reflection automatically edit skills or create backlog issues?**

No. A proposal-only request produces concrete suggestions. Previously authorized edits can proceed without another confirmation, and backlog publication is not automatic.

**Does it need three reviewers and a synthesizer?**

No. There is no fixed agent count or model requirement. Any returned finding must be checked against the session and the affected skill.

## It's working if

- A proposed change cites evidence and names the behaviour it improves.
- Existing adequate guidance is not duplicated.
- The report distinguishes changes applied from suggestions left unapplied.

## Where it fits

automate-me captures durable working preferences. writing-for-agents guides edits to the actual instruction files. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
