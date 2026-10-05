# Agent skills

A collection of reusable skills for Claude Code, Codex, and other coding agents. The repository contains 36 skills:

- 36 promoted skills in the plugin
- No utility skills in `skills/misc/`

The original engineering skills come from [Matt Pocock](https://github.com/mattpocock). The pstack additions come from [Lauren Tan, known as poteto](https://github.com/poteto). This repository maintains and adapts both sets, and includes the custom `copse` issue tracker integration.

## Shared working guidance

Collaboration preferences, engineering defaults, and shell discipline live in [working guidance](./skills/shared/working-guidance.md). This reference replaces the standalone `engineering-philosophy` and `shell-discipline` skills. All workflows link to it; keep `skills/shared/` with the collection when distributing or copying skills. It is a reference folder, not a promoted skill.

For routine Codex use, reference this file from your personal `AGENTS.md` using its installed absolute path. This keeps preferences in one maintained source. Existing symlink installations use changes from the currently checked-out branch. When returning to a version without shared guidance, update any standing pointer and restore its retired skill links as part of the rollback.

The local link helper does not remove retired links. Remove only symlinks that resolve to this repository's retired `engineering-philosophy` and `shell-discipline` folders. Preserve unrelated entries.

Project verification and operations skills should be written against a real project's commands, environments, and required journeys. Use `create-verification-skill` for that project when needed; no additional generic skill pack is required.

## Start here

For most engineering work:

1. Run [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) to settle the problem, terminology, and decisions.
2. Run [`to-spec`](./skills/engineering/to-spec/SKILL.md) for work that needs a durable spec.
3. Run [`to-tickets`](./skills/engineering/to-tickets/SKILL.md) to split the spec into dependency-aware tickets.
4. Build the tickets, then run [`code-review`](./skills/engineering/code-review/SKILL.md) to review the changes against the spec and the repository standards.

For a large effort that spans multiple agent sessions and still has major unknowns, run [`wayfinder`](./skills/engineering/wayfinder/SKILL.md). Set up the repository's tracker and domain-doc conventions first with [`setup-matt-pocock-skills`](./skills/engineering/setup-matt-pocock-skills/SKILL.md).

Skip the spec and ticket steps for a small change.

## Common tasks

| Task | Skill |
| --- | --- |
| Clarify an idea in a repository | [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) |
| Plan a multi-session effort with unknowns | [`wayfinder`](./skills/engineering/wayfinder/SKILL.md) |
| Configure this repo for the engineering skills | [`setup-matt-pocock-skills`](./skills/engineering/setup-matt-pocock-skills/SKILL.md) |
| Understand project terminology | [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md) |
| Understand module shape | [`codebase-design`](./skills/engineering/codebase-design/SKILL.md) |
| Diagnose a hard bug | [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md) |
| Check risks beyond a diff | [`blast-radius`](./skills/engineering/blast-radius/SKILL.md) |
| Review a branch or PR | [`code-review`](./skills/engineering/code-review/SKILL.md) |
| Commit and open a PR | [`commit`](./skills/engineering/commit/SKILL.md) |
| Plan an architecture | [`design`](./skills/engineering/design/SKILL.md) |
| Keep the build minimal | [`ponytail`](./skills/engineering/ponytail/SKILL.md) |
| Explain how something works | [`how`](./skills/engineering/how/SKILL.md) |
| Find out why code looks this way | [`why`](./skills/engineering/why/SKILL.md) |
| Prove app behavior like a user | [`create-verification-skill`](./skills/engineering/create-verification-skill/SKILL.md) |
| Keep a verification skill honest | [`maintain-verification-skill`](./skills/engineering/maintain-verification-skill/SKILL.md) |
| Record decisions during long work | [`show-me-your-work`](./skills/engineering/show-me-your-work/SKILL.md) |
| Write agent-facing documents | [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md) |
| Write technical documentation | [`technical-writing`](./skills/productivity/technical-writing/SKILL.md) |
| Remove AI writing tells | [`unslop`](./skills/productivity/unslop/SKILL.md) |

## Promoted skills

Promoted skills are included in the plugin. User-invoked skills run only when you type their name. Model-invoked skills can also run automatically when the task matches their description.

### Engineering

#### User-invoked

- [`setup-matt-pocock-skills`](./skills/engineering/setup-matt-pocock-skills/SKILL.md): Configures requested tracker and domain conventions, with Git checks only when explicitly requested.
- [`wayfinder`](./skills/engineering/wayfinder/SKILL.md): Plans a large, multi-session effort as a map of decision tickets.
- [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md): Resolves consequential questions and records settled terminology and decisions.
- [`improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md): Finds codebase deepening opportunities and grills through the selected one.
- [`to-spec`](./skills/engineering/to-spec/SKILL.md): Synthesizes agreed behaviour into a proportionate, verifiable spec.
- [`to-tickets`](./skills/engineering/to-tickets/SKILL.md): Splits a plan into tracer-bullet tickets with blocking edges.
- [`show-me-your-work`](./skills/engineering/show-me-your-work/SKILL.md): Records a TSV decision trail for long-running work.
- [`blast-radius`](./skills/engineering/blast-radius/SKILL.md): Finds risks beyond a diff and proves the central safety fact.
- [`commit`](./skills/engineering/commit/SKILL.md): Commits on a feature branch and opens a PR.
- [`design`](./skills/engineering/design/SKILL.md): Produces a pre-implementation architecture plan.
- [`how`](./skills/engineering/how/SKILL.md): Explains how a subsystem works, or critiques its architecture.
- [`why`](./skills/engineering/why/SKILL.md): Investigates why code looks the way it does, with cited evidence.
- [`create-verification-skill`](./skills/engineering/create-verification-skill/SKILL.md): Generates a project-local skill that drives an app like a user.
- [`maintain-verification-skill`](./skills/engineering/maintain-verification-skill/SKILL.md): Audits a verification skill and its feature map.

#### Model-invoked

- [`prototype`](./skills/engineering/prototype/SKILL.md): Answers a design question with throwaway code.
- [`copse`](./skills/engineering/copse/SKILL.md): Uses Copse records and worktree links as the local issue tracker.
- [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md): Diagnoses bugs with evidence and meaningful verification, scaling the investigation to uncertainty and impact.
- [`research`](./skills/engineering/research/SKILL.md): Researches primary sources and writes cited Markdown.
- [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md): Challenges terminology and records domain decisions.
- [`codebase-design`](./skills/engineering/codebase-design/SKILL.md): Designs deep modules with small interfaces and clean seams.
- [`code-review`](./skills/engineering/code-review/SKILL.md): Reviews committed and local changes for defects, regressions, requirements, and documented standards, with findings ordered by severity.
- [`resolving-merge-conflicts`](./skills/engineering/resolving-merge-conflicts/SKILL.md): Resolves merge or rebase conflicts by tracing intent.
- [`wizard`](./skills/engineering/wizard/SKILL.md): Generates scripts for setup steps that require human action.
- [`designing-architecture`](./skills/engineering/designing-architecture/SKILL.md): Designs interfaces, data flow, and migrations at the depth the decision needs.
- [`committing-changes`](./skills/engineering/committing-changes/SKILL.md): Commits and delivers authorized work while preserving existing hooks and CI.
- [`ponytail`](./skills/engineering/ponytail/SKILL.md): Builds the laziest working solution at adjustable intensity.

### Productivity

#### User-invoked

- [`grill-me`](./skills/productivity/grill-me/SKILL.md): Stress-tests a plan through focused questions without writing repository state.
- [`handoff`](./skills/productivity/handoff/SKILL.md): Writes a compact handoff for another session or agent.
- [`wait-what`](./skills/productivity/wait-what/SKILL.md): Re-explains a message that did not land.
- [`automate-me`](./skills/productivity/automate-me/SKILL.md): Captures durable preferences in shared instructions or an optional personal mode.
- [`reflect`](./skills/productivity/reflect/SKILL.md): Turns supported session lessons into focused proposals or authorized corrections.
- [`technical-writing`](./skills/productivity/technical-writing/SKILL.md): Writes and reviews technical documentation.
- [`teach`](./skills/productivity/teach/SKILL.md): Builds a tailored course from your goals, reported background, and demonstrated knowledge.

#### Model-invoked

- [`grilling`](./skills/productivity/grilling/SKILL.md): Resolves consequential questions, with exhaustive questioning available on request.
- [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md): Guides writing for skills and other agent-facing documents.
- [`unslop`](./skills/productivity/unslop/SKILL.md): Removes AI writing tells and keeps prose concrete.

## Custom skills

- [`copse`](./skills/engineering/copse/SKILL.md): The custom Copse issue tracker integration for the engineering skills.

## Adapted skills

Several workflows are adapted from third-party sources (MIT licensed). The `commit`, `design`, `designing-architecture`, and `committing-changes` skills, along with the engineering and shell guidance now consolidated in the shared reference, originate from [swell-agents/coding-skills](https://github.com/swell-agents/coding-skills); `ponytail` comes from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail); and `how`, `why`, `create-verification-skill`, and `maintain-verification-skill` come from the pstack plugin by Lauren Tan (shipped in the Cursor plugins collection).

## Utility skills

No utility skills are currently kept in `skills/misc/`.

## Development

Keep the manifests, bucket READMEs, docs pages, and skill metadata in sync when adding or moving a promoted skill. Run:

```bash
claude plugin validate . --strict
git diff --check
```

Use [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md) when editing a skill or agent-facing document. Apply [`unslop`](./skills/productivity/unslop/SKILL.md) to prose changes.
