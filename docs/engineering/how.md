## What it does

`how` answers "how does X work?" by exploring the codebase and producing a senior-engineer-level explanation: overview, key concepts, the flow, where things live, and gotchas. Enough to build a working mental model, not annotated source.

It has two modes. Explain mode explores (with parallel explorer subagents for complex subsystems, directly for simple ones) and synthesizes one coherent picture. Critique mode runs the explain flow first, then judges the architecture against a structural rubric and sorts findings into act-on, consider, noted, and dismissed.

## When to reach for it

You invoke this by typing `/how`, and the agent won't reach for it on its own. Reach for it when you need a mental model of unfamiliar code, or a structural second opinion on a design you now understand.

| Your situation | Reach for |
| --- | --- |
| How does this subsystem work | `how` |
| Why does it look this way | [why](https://aihero.dev/skills-why) |
| One question needs a runnable answer | [prototype](https://aihero.dev/skills-prototype) |

## Explain before critiquing

Critique mode never skips the explanation. The explainer's output stands on its own first; the verdict follows below it. Someone who only wants to understand the system never has to wade through critique, and a critic who hasn't understood the system has nothing worth saying.

## Common questions

**When does it use explorer subagents?**
For complex questions spanning files or services. Simple questions (one module, one function) get a single direct pass. When in doubt it leans simple and fans out only if the explainer hits a wall.

## It's working if

- The explanation references real files and functions you can go look at.
- The flow walks trigger to effect without hand-waving a step.
- Critique findings are structural (layering, coupling, state ownership), not style.

## Where it fits

`how` is a reach-for-it-anytime standalone for understanding code. Its companion is [why](https://aihero.dev/skills-why): `how` covers what the code does, `why` covers what forces shaped it. Its closest neighbours are [prototype](https://aihero.dev/skills-prototype), for questions only a runnable answer settles, and [codebase-design](https://aihero.dev/skills-codebase-design), for designing the module once you understand it.
