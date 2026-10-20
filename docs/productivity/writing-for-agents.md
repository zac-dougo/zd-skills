## What it does

`writing-for-agents` helps you write and revise instructions an agent reads, from skills and `AGENTS.md` files to project docs, specs, tickets, and prompts. It focuses each document on the decisions it needs to guide, keeps related instructions together, and moves details behind clear references when only some tasks need them.

The goal is reliable behaviour with enough context to explain important choices. Shorter is useful when it removes repetition or stale detail; cutting a constraint or needed context makes the document worse.

## When to reach for it

Type `/writing-for-agents`, or the agent reaches for it on its own when you're creating or editing a skill, or modifying `AGENTS.md` or `CLAUDE.md`.

Reach for it by hand for other documents an agent reads, including docs, specs, [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket), and system or [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) prompts. Use [technical-writing](https://aihero.dev/skills-technical-writing) for human-facing documentation, and call [unslop](https://aihero.dev/skills-unslop) after editing prose. Inspect relevant code and project records before describing what a codebase contains; this reference guides how the resulting document reads.

## Common questions

**Where did `/writing-great-skills` go?**

It was renamed to `writing-for-agents` in v1.1 because the guidance applies to any document an agent reads. There is no alias; install the current skill name.

**Can I ask an agent to write the document for me?**

Yes. Review the draft for scope, missing constraints, repeated or stale details, and references that do not say when to follow them. A generated draft is a starting point, not evidence that the instructions work.

**How do I trim a document without losing behavior?**

List the decisions and constraints the document must preserve, then remove repetition and material that does not help the agent act. Try a representative request and compare the result with the behaviour you need.

**What belongs in a separate reference?**

Move substantial detail out when only some task branches need it. Keep shared steps and decisions in the main document, and make the pointer state which cases should load the reference.

**Should this live in `CLAUDE.md` or somewhere else?**

Keep always-needed guidance in `CLAUDE.md`. Put conditional detail in a referenced file when the pointer can clearly tell the agent when to read it.

## It's working if

- A representative request follows the intended steps and respects the important constraints.
- The main document is easy to scan, with related guidance together and conditional details easy to find.
- Repeated instructions have one clear source, and each reference says when it applies.

## Where it fits

This is a standalone reference for agent-facing documents. For a skill, also use its [skill mechanics](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md); for human-facing docs, use [technical-writing](https://aihero.dev/skills-technical-writing).
