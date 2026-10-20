---
name: writing-for-agents
description: Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

Read [working guidance](../../shared/working-guidance.md) once for this task.

Use this reference when writing or revising a document an agent reads, including skills, `AGENTS.md` or `CLAUDE.md`, project docs, specs, tickets, and prompts. Focus on clear instructions that preserve the intended behaviour without carrying unnecessary explanation.

When the document is a skill, read [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for frontmatter, invocation choice, and router skills. For human-facing documentation, use the relevant authoring guidance directly; suggest `technical-writing` when a dedicated workflow would help. After editing prose, read and follow [unslop](../unslop/SKILL.md).

## Define the scope

Start with the document's audience, purpose, and the decisions it needs to guide. Keep the main file focused on what applies to most uses. Include enough context to explain non-obvious choices, but avoid teaching background knowledge the reader already has.

For procedural documents, give actions in a useful order and make important completion conditions clear. Scale the detail to the task: exhaustive criteria help when omissions are costly, but add overhead to routine work.

## Structure and references

Group related rules and caveats together. Keep the same meaning in one authoritative place, and point to that source when other documents need it.

Keep essential steps and decisions in the main document. Move substantial details to a reference when only some cases need them, and add a clear pointer that says what the reference contains and when to read it. Inline details that every path needs. Split a document when it gives distinct audiences or task branches clearer instructions, and make sure each part has a reliable pointer.

Write pointers with specific triggers. Describe the cases that need the material, using the words a reader is likely to use for those cases. Check that paths and referenced files exist and remain available when the document is copied or packaged.

## Preserve behavior

When editing, identify the existing instructions and behaviour that must remain. Remove repetition and stale details without dropping a constraint, decision, or necessary context. Prefer direct instructions that say what to do; keep prohibitions when they define a real boundary or prevent a known failure.

Avoid duplicating facts that are easy to check in the repository or tool itself. Keep rationale, conventions, and important gotchas that cannot be found there. Update references when behavior or file locations change.

## Check the result

Use a representative request to see whether the document guides the intended behaviour. For changes to an existing document, compare the result against the behaviour that must be preserved. Validate frontmatter, links, and packaging details when relevant, but treat those checks as support: valid formatting alone does not show that the instructions work.
