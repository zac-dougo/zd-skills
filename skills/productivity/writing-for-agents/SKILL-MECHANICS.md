# Skill mechanics

This reference covers metadata and composition for [writing-for-agents](SKILL.md).

## Invocation policy

Every skill has a concise `name` and `description`. Preserve its existing invocation policy unless the user asks to change it.

- Automatically discoverable skills describe the task that should select them. They remain available for explicit use.
- Explicit-only workflows run when the user invokes them. In Claude Code, set `disable-model-invocation: true` in frontmatter. In Codex, also set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Do not treat a visible file as authorization to launch an explicit-only workflow.

Each skill in this collection includes `agents/openai.yaml` with a display name and short description. Keep its policy consistent with frontmatter. Do not claim that every host loads or hides metadata identically.

## Composition and references

Tell the agent to read and follow the dependency's `SKILL.md`, with a concrete relative link where the collection layout is known. If a host supplies a skill-invocation tool, it can be used; a dedicated tool is not a prerequisite. Resolve installed paths from the actual catalog instead of guessing directories or command syntax.

Use automatically discoverable skills for shared workflows. Keep an explicit-only dependency under the user's invocation control. For read-only rules shared across workflows, link to a plain reference file rather than creating a skill solely to make the text reachable.

Keep linked files available in the installation. This collection's shared guidance lives at `skills/shared/working-guidance.md`; packaging or copying individual skills must preserve their dependencies. Validate relative links after moving or retiring a skill.

## Scope and depth

Put essential decisions in `SKILL.md`; place substantial conditional procedures in references. Describe when each reference is needed. Avoid mandatory pipelines, agent counts, or repeated approval gates without a concrete reason.

Test selection and behaviour on representative requests. Validation of YAML or Markdown alone does not establish that a workflow makes good decisions.
