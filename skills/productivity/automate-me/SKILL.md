---
name: automate-me
description: Capture durable working preferences in shared instructions, or create an optional personal mode when the user wants one.
disable-model-invocation: true
---

# Automate me

Read [working guidance](../../shared/working-guidance.md) once for this task. Turn established preferences into a small maintained source. Avoid repeating instructions already enforced by the host or another maintained reference.

## Gather the preferences

Inspect the user's existing shared instructions and personal mode, if any. Start with the current conversation and explicit preferences. Consult workspace-scoped history only when needed and available; do not search unrelated transcripts. Repeated behaviour can support a preference, while a single unconfirmed inference cannot establish one. An explicit standing preference does not need repeated examples.

Ask only about missing choices that materially affect the result. Use a short round of concrete alternatives and recommendations. Skip questions already answered by the conversation. A small task needs no history-mining agents or prescribed interview rounds.

## Choose the home

- For preferences the user wants applied routinely, update one shared instruction source and reference it from the relevant agent's standing instructions when authorized. Preserve unrelated existing content.
- For an optional style or workflow the user wants to switch on, create or update an explicit-only personal mode skill. Keep platform-specific invocation policy in the platform metadata and the shared instructions portable.
- For project-specific facts or procedures, use the project's instructions or documentation.

Keep communication, autonomy, verification, and Git preferences only when they add a concrete choice. Reference existing workflows instead of copying them. Avoid hardcoded model names, transcript paths, agent counts, or universal rules inferred from one incident.

## Write and verify

Read and follow [writing-for-agents](../writing-for-agents/SKILL.md), then apply [unslop](../unslop/SKILL.md). Show a concrete draft when the user requested a proposal; apply changes already authorized without a redundant approval round. Validate metadata and referenced paths, and inspect example requests for the behaviour the preferences are meant to change.

Preserve the user's requested location and publishing scope. Creating or revising local preferences does not automatically request a commit, push, or PR. When repository delivery is requested, follow [committing-changes](../../engineering/committing-changes/SKILL.md).
