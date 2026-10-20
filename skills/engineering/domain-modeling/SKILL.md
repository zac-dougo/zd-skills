---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.
---

Read [working guidance](../../shared/working-guidance.md) once for this task.

# Domain Modeling

Build and sharpen project terminology when the task calls for developing the domain model. Use concrete scenarios and code evidence to resolve consequential ambiguity. Reading `CONTEXT.md` for established vocabulary does not require this workflow or authorize editing the glossary.

A request to create or maintain a glossary or ADRs includes edits within that scope. A discussion-only request ends with the proposed terms or decisions. An implementation request includes documentation updates needed for that work, following repository conventions; it does not automatically call for a new glossary or ADR system.

## File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Preserve existing glossary and ADR locations and formats. Create files only when documentation work is within scope and there is a settled term or decision worth recording. These layouts are examples, not a required repository structure.

## During the session

### Challenge against the glossary

Surface a conflict with `CONTEXT.md` when it would change the model or requested behavior. For example: "Your glossary defines 'cancellation' as X, but this flow appears to need Y." Resolve harmless conversational synonyms from context without interrupting.

### Sharpen fuzzy language

When an overloaded term would lead to different designs or behavior, propose a precise term and explain the distinction. Ask only if the code and conversation cannot settle it.

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Record terms within scope

When glossary maintenance is authorized, record settled terms in the existing glossary. Use [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) when the project has no established format. A discussion-only session reports proposed entries without writing files. Do not request another confirmation for edits already authorized.

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Write it when recording decisions is already authorized; otherwise propose it. Preserve the project's ADR conventions, using [ADR-FORMAT.md](./ADR-FORMAT.md) only when none exist.
