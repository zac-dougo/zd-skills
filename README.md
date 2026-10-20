# Agent skills

A collection of reusable skills for Claude Code, Codex, and other coding agents. The repository contains 16 skills:

- 16 promoted skills in the plugin
- No utility skills in `skills/misc/`

The original engineering skills come from [Matt Pocock](https://github.com/mattpocock). The pstack additions come from [Lauren Tan, known as poteto](https://github.com/poteto). This repository maintains and adapts both sets.

## Shared working guidance

Collaboration preferences, engineering defaults, and shell discipline live in [working guidance](./skills/shared/working-guidance.md). This reference replaces the standalone `engineering-philosophy` and `shell-discipline` skills. All workflows link to it; keep `skills/shared/` with the collection when distributing or copying skills. It is a reference folder, not a promoted skill. Its delegation policy encourages useful parallel work, prefers GPT-6 Luna for bounded tasks, and reserves stronger models for work that needs them.

For routine Codex use, reference this file from your personal `AGENTS.md` using its installed absolute path. This keeps preferences in one maintained source. Existing symlink installations use changes from the currently checked-out branch. When returning to a version without shared guidance, update any standing pointer and restore its retired skill links as part of the rollback.

The local link helper does not remove retired links. After removing a skill, remove only verified symlinks into that retired folder in this repository. Preserve unrelated entries.

Use the project's existing commands and harnesses for verification, matching the checks to the requested change.

## Start here

Use the skills that fit the task:

1. Run [`grilling`](./skills/productivity/grilling/SKILL.md) when consequential questions need to be settled. Use [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md) when the discussion should also maintain project terminology and decisions.
2. Run [`to-spec`](./skills/engineering/to-spec/SKILL.md) when the agreed outcome needs a durable, verifiable spec.
3. Implement the requested work, then run [`code-review`](./skills/engineering/code-review/SKILL.md) to review the changes against the requirements and repository standards.

Small changes can go directly to implementation and verification.

## Common tasks

| Task | Skill |
| --- | --- |
| Clarify an idea in a repository | [`grilling`](./skills/productivity/grilling/SKILL.md) |
| Understand project terminology | [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md) |
| Diagnose a hard bug | [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md) |
| Check risks beyond a diff | [`blast-radius`](./skills/engineering/blast-radius/SKILL.md) |
| Review a branch or PR | [`code-review`](./skills/engineering/code-review/SKILL.md) |
| Commit and open a PR | [`committing-changes`](./skills/engineering/committing-changes/SKILL.md) |
| Plan an architecture | [`designing-architecture`](./skills/engineering/designing-architecture/SKILL.md) |
| Make agent chat easier to read | [`agent-communication`](./skills/productivity/agent-communication/SKILL.md) |
| Write agent-facing documents | [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md) |
| Write technical documentation | [`technical-writing`](./skills/productivity/technical-writing/SKILL.md) |
| Remove AI writing tells | [`unslop`](./skills/productivity/unslop/SKILL.md) |

## Promoted skills

Promoted skills are included in the plugin. User-invoked skills run only when you type their name. Model-invoked skills can also run automatically when the task matches their description.

### Engineering

#### User-invoked

- [`to-spec`](./skills/engineering/to-spec/SKILL.md): Synthesizes agreed behaviour into a proportionate, verifiable spec.
- [`blast-radius`](./skills/engineering/blast-radius/SKILL.md): Finds risks beyond a diff and checks the conditions its safety depends on.

#### Model-invoked

- [`prototype`](./skills/engineering/prototype/SKILL.md): Answers a design question with throwaway code.
- [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md): Diagnoses bugs with evidence and meaningful verification, scaling the investigation to uncertainty and impact.
- [`research`](./skills/engineering/research/SKILL.md): Researches primary sources and returns cited findings, saving a document when needed.
- [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md): Challenges terminology and records domain decisions.
- [`code-review`](./skills/engineering/code-review/SKILL.md): Reviews committed and local changes for defects, regressions, requirements, and documented standards, with findings ordered by severity.
- [`designing-architecture`](./skills/engineering/designing-architecture/SKILL.md): Designs interfaces, data flow, and migrations at the depth the decision needs.
- [`committing-changes`](./skills/engineering/committing-changes/SKILL.md): Commits and delivers authorized work while preserving existing hooks and CI.

### Productivity

#### User-invoked

- [`handoff`](./skills/productivity/handoff/SKILL.md): Writes a compact handoff for another session or agent.
- [`reflect`](./skills/productivity/reflect/SKILL.md): Turns supported session lessons into focused proposals or authorized corrections.
- [`technical-writing`](./skills/productivity/technical-writing/SKILL.md): Writes and reviews technical documentation.

#### Model-invoked

- [`grilling`](./skills/productivity/grilling/SKILL.md): Resolves consequential questions, with exhaustive questioning available on request.
- [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md): Guides writing for skills and other agent-facing documents.
- [`agent-communication`](./skills/productivity/agent-communication/SKILL.md): Shapes readable agent chat with flexible structures, clear writing, and compact formatting.
- [`unslop`](./skills/productivity/unslop/SKILL.md): Removes AI writing tells and keeps prose concrete.

## Adapted skills

Several workflows are adapted from third-party sources (MIT licensed). The `designing-architecture` and `committing-changes` skills, along with the engineering and shell guidance now consolidated in the shared reference, originate from [swell-agents/coding-skills](https://github.com/swell-agents/coding-skills).

## Utility skills

No utility skills are currently kept in `skills/misc/`.

## Development

Keep the manifests, bucket READMEs, docs pages, and skill metadata in sync when adding or moving a promoted skill. Run:

```bash
claude plugin validate . --strict
git diff --check
```

Use [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md) when editing a skill or agent-facing document. Apply [`unslop`](./skills/productivity/unslop/SKILL.md) to prose changes.
