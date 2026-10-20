## What it does

`domain-modeling` develops project terminology using concrete scenarios and code evidence. It resolves ambiguities that would change behavior or a design, and records settled terms and consequential decisions when documentation work is within scope.

Reading a glossary or using a conversational synonym does not require editing project documents. Discussion-only requests end with proposed terms or decisions.

## When to reach for it

Type `/domain-modeling`, or the agent reaches for it automatically when a task involves developing terminology, a glossary, or architectural decision records.

| The situation | The move |
| --- | --- |
| An overloaded term would lead to different behavior | Clarify the distinction using code and examples |
| You want an existing glossary maintained | Record settled terms within the requested scope |
| You want to discuss terms without writing files | Request discussion or proposals only |
| Interfaces or responsibilities need a design | Use [designing-architecture](https://aihero.dev/skills-designing-architecture) |
| You only need an established definition | Read the project's glossary |

## Documentation scope

A request to create or maintain a glossary or ADRs authorizes those edits. Implementation includes documentation updates needed for that work, following repository conventions; it does not automatically require a new documentation system.

The skill preserves existing locations and formats. It creates a glossary or ADR only when that work is authorized and there is a settled term or consequential decision worth recording. ADRs are reserved for choices that are hard to reverse, surprising without context, and based on a real tradeoff.

## Common questions

**Will every terminology discussion write to my repository?**

No. Discussion-only requests return proposals. Already authorized documentation work proceeds without another confirmation round.

**Can I use my own glossary and ADR conventions?**

Yes. Existing project locations and formats take precedence over the examples supplied by the skill.

**What belongs in the glossary?**

Definitions and relationships between domain concepts. Implementation notes, plans, and a diary of the conversation belong elsewhere.

## It's working if

- Questions concern ambiguities that would materially change the work.
- Harmless conversational synonyms do not interrupt progress.
- Definitions agree with the intended behavior and relevant code evidence.
- File changes stay within the authorized scope and preserve project conventions.

## Where it fits

Pair `domain-modeling` with [grilling](https://aihero.dev/skills-grilling) when assumptions need examination, or [designing-architecture](https://aihero.dev/skills-designing-architecture) when terminology affects a design. It also works directly on a glossary or ADR request.
