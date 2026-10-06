## What it does

Splits agreed work into independently verifiable tickets with explicit dependencies. Each slice includes the layers its behaviour needs, without inventing changes to unaffected layers.

## When to reach for it

Invoke `$to-tickets` in Codex or `/to-tickets` in Claude Code with a plan, spec, or the current conversation. Ask for a draft when you want to review the breakdown before publication.

## Common questions

**Will it ask me to approve the same breakdown twice?**

No. It resolves consequential slicing choices and honours existing approval or discretion you already granted.

**What about a wide refactor that cannot land one vertical slice at a time?**

It can use an expand, migrate, and contract sequence, with dependencies and integration checks that preserve the required compatibility.

## It's working if

- Each ticket has observable acceptance criteria.
- Blocking edges represent real dependencies.
- Publication respects the requested destination and scope.

## Where it fits

It follows planning or to-spec and supplies work that implementation and code-review can verify. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
