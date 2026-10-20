## What it does

`technical-writing` helps you write and review technical documents that readers can understand on the first read. It uses Diátaxis modes and sentence-level guidance to clarify purpose and wording, while treating style rules as tools rather than ends in themselves. A tutorial can include a useful reference table, uncertainty can remain when the evidence is incomplete, and code examples follow the target project's conventions.

## When to reach for it

You invoke this by typing `/technical-writing`, and the agent won't reach for it on its own. Reach for it when writing or reviewing technical documentation. For agent instructions such as skills and `AGENTS.md`, use [writing-for-agents](https://aihero.dev/skills-writing-for-agents) as the primary guide.

## Common questions

**Does every document need to stay in one Diátaxis mode?**

No. Keep the main purpose clear, and combine modes when the added material helps readers do the task. Split the material when it has a separate purpose or audience.

**Should reference documentation remove all uncertainty?**

No. State supported facts plainly, and say when evidence is incomplete. Do not turn a guess into a fact for the sake of a confident tone.

**Do code examples always use tabs?**

No. Follow the conventions of the target repository and language.

## It's working if

- Readers can tell what the document helps them do or understand.
- Mixed material, such as a reference table in a tutorial, supports the main purpose.
- Sentences make conditions, actors, and uncertainty clear without forcing a style rule that makes the wording harder to read.
- Code examples look familiar in the target project.

## Where it fits

`technical-writing` is a reach-for-it-anytime productivity standalone. It complements [writing-for-agents](https://aihero.dev/skills-writing-for-agents) for agent-facing documents and [unslop](https://aihero.dev/skills-unslop) for prose cleanup.
