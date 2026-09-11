## What it does

`shell-discipline` keeps agent-run shell commands auditable: one command per call, no chains, no inline environment variables, explicit auth tools instead of pasted secrets.

Its defining constraint is one intent per tool call. A chained command is opaque to the permission layer; split commands give one auditable call per intent.

## When to reach for it

The agent reaches for it automatically when running shell commands: it is model-invoked, and fires on any multi-step shell work. There is nothing to type; it is a standing rule, not a procedure.

| Your situation | Reach for |
| --- | --- |
| About to chain commands with `&&` | Split them: `cd` first, then the command |
| About to prefix `VAR=value` or a token | Set it separately or use the auth tool |
| About to `sudo` inline | Set up the privilege out of band instead |

## Common questions

**Does this slow everything down?**
One extra call per step, and each call is checkable on its own. The cost is a few round trips; the payoff is that every command in the transcript shows exactly what ran.

## It's working if

- No shell call in the transcript contains `&&`, `;`, or an inline `VAR=value`.
- Credentials appear in keyrings and auth tools, never on command lines or in history.
- Aliases are spelled out as the real commands they hide.

## Where it fits

`shell-discipline` is a standing rule underneath every skill that shells out, most visibly [committing-changes](https://aihero.dev/skills-committing-changes), whose git sequences it keeps auditable. It pairs with [engineering-philosophy](https://aihero.dev/skills-engineering-philosophy): explicit over implicit, everywhere.
