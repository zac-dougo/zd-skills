# Productivity

General workflow tools, not code-specific.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; other harnesses: their own equivalent).

- **[grill-me](./grill-me/SKILL.md)**: Stress-tests a plan through focused questions without writing repository state.
- **[handoff](./handoff/SKILL.md)**: Compact the current conversation into a handoff document so another agent can continue the work.
- **[wait-what](./wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you're missing, in plain English, using your `CONTEXT.md` vocabulary.
- **[automate-me](./automate-me/SKILL.md)**: Captures durable preferences in shared instructions or an optional personal mode.
- **[reflect](./reflect/SKILL.md)**: Turns supported session lessons into focused proposals or authorized corrections.
- **[technical-writing](./technical-writing/SKILL.md)**: Write and review clear technical documentation.
- **[teach](./teach/SKILL.md)**: Build a tailored course from your goals, reported background, and demonstrated knowledge.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[grilling](./grilling/SKILL.md)**: Resolves consequential questions, with exhaustive questioning available on request.
- **[writing-for-agents](./writing-for-agents/SKILL.md)**: Writing documents for agents: skills, AGENTS.md/CLAUDE.md, and any doc an agent reaches by a pointer.
- **[unslop](./unslop/SKILL.md)**: Remove AI writing tells while keeping prose specific and human.
