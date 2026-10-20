# Productivity

General workflow tools, not code-specific.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; other harnesses: their own equivalent).

- **[handoff](./handoff/SKILL.md)**: Compact the current conversation into a handoff document so another agent can continue the work.
- **[reflect](./reflect/SKILL.md)**: Turns supported session lessons into focused proposals or authorized corrections.
- **[technical-writing](./technical-writing/SKILL.md)**: Write and review clear technical documentation.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[grilling](./grilling/SKILL.md)**: Resolves consequential questions, with exhaustive questioning available on request.
- **[writing-for-agents](./writing-for-agents/SKILL.md)**: Writing documents for agents: skills, AGENTS.md/CLAUDE.md, and any doc an agent reaches by a pointer.
- **[unslop](./unslop/SKILL.md)**: Remove AI writing tells while keeping prose specific and human.

- **[agent-communication](./agent-communication/SKILL.md)**: Shape readable agent chat with research-informed presentation, clear writing, and optional message patterns.
