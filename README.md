# Agent skills

A collection of reusable skills for Claude Code, Codex, and other coding agents. The repository contains 47 skills:

- 43 promoted skills in the plugin
- 4 utility skills in `skills/misc/`

The original engineering skills come from [Matt Pocock](https://github.com/mattpocock). The pstack additions come from [Lauren Tan, known as poteto](https://github.com/poteto). This repository maintains and adapts both sets, and includes the custom `copse` issue tracker integration.

## Start here

For most engineering work:

1. Run [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) to settle the problem, terminology, and decisions.
2. Run [`to-spec`](./skills/engineering/to-spec/SKILL.md) for work that needs a durable spec.
3. Run [`to-tickets`](./skills/engineering/to-tickets/SKILL.md) to split the spec into dependency-aware tickets.
4. Build the tickets, then run [`code-review`](./skills/engineering/code-review/SKILL.md) to review the changes against the spec and the repository standards.

Skip the spec and ticket steps for a small change.

## Common tasks

| Task | Skill |
| --- | --- |
| Clarify an idea in a repository | [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) |
| Understand project terminology | [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md) |
| Understand module shape | [`codebase-design`](./skills/engineering/codebase-design/SKILL.md) |
| Diagnose a hard bug | [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md) |
| Check risks beyond a diff | [`blast-radius`](./skills/engineering/blast-radius/SKILL.md) |
| Review a branch or PR | [`code-review`](./skills/engineering/code-review/SKILL.md) |
| Run a broad quality gate | [`review`](./skills/engineering/review/SKILL.md) |
| Build test-first | [`tdd`](./skills/engineering/tdd/SKILL.md) |
| Commit and open a PR | [`commit`](./skills/engineering/commit/SKILL.md) |
| Plan an architecture | [`design`](./skills/engineering/design/SKILL.md) |
| Track Spec Kit blocks as issues | [`block-issues`](./skills/engineering/block-issues/SKILL.md) |
| Implement a Spec Kit block | [`block-implement`](./skills/engineering/block-implement/SKILL.md) |
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

- [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md): Builds shared terminology and records decisions while grilling.
- [`improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md): Finds codebase deepening opportunities and grills through the selected one.
- [`to-spec`](./skills/engineering/to-spec/SKILL.md): Publishes a conversation as a tracker-backed spec.
- [`to-tickets`](./skills/engineering/to-tickets/SKILL.md): Splits a plan into tracer-bullet tickets with blocking edges.
- [`show-me-your-work`](./skills/engineering/show-me-your-work/SKILL.md): Records a TSV decision trail for long-running work.
- [`blast-radius`](./skills/engineering/blast-radius/SKILL.md): Finds risks beyond a diff and proves the central safety fact.
- [`review`](./skills/engineering/review/SKILL.md): Runs the four-pass quality gate over a diff or PR.
- [`commit`](./skills/engineering/commit/SKILL.md): Commits on a feature branch and opens a PR.
- [`tdd`](./skills/engineering/tdd/SKILL.md): Drives a red-green-refactor cycle on a requirement.
- [`block-issues`](./skills/engineering/block-issues/SKILL.md): Creates one GitHub issue per Spec Kit tasks.md block.
- [`design`](./skills/engineering/design/SKILL.md): Produces a pre-implementation architecture plan.
- [`block-implement`](./skills/engineering/block-implement/SKILL.md): Implements one Spec Kit tasks.md block end to end.
- [`how`](./skills/engineering/how/SKILL.md): Explains how a subsystem works, or critiques its architecture.
- [`why`](./skills/engineering/why/SKILL.md): Investigates why code looks the way it does, with cited evidence.
- [`create-verification-skill`](./skills/engineering/create-verification-skill/SKILL.md): Generates a project-local skill that drives an app like a user.
- [`maintain-verification-skill`](./skills/engineering/maintain-verification-skill/SKILL.md): Audits a verification skill and its feature map.

#### Model-invoked

- [`prototype`](./skills/engineering/prototype/SKILL.md): Answers a design question with throwaway code.
- [`copse`](./skills/engineering/copse/SKILL.md): Uses Copse records and worktree links as the local issue tracker.
- [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md): Reproduces, instruments, fixes, and regression-tests hard bugs.
- [`research`](./skills/engineering/research/SKILL.md): Researches primary sources and writes cited Markdown.
- [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md): Challenges terminology and records domain decisions.
- [`codebase-design`](./skills/engineering/codebase-design/SKILL.md): Designs deep modules with small interfaces and clean seams.
- [`code-review`](./skills/engineering/code-review/SKILL.md): Reviews changes against repository standards and the originating spec.
- [`resolving-merge-conflicts`](./skills/engineering/resolving-merge-conflicts/SKILL.md): Resolves merge or rebase conflicts by tracing intent.
- [`wizard`](./skills/engineering/wizard/SKILL.md): Generates scripts for setup steps that require human action.
- [`running-tdd-cycles`](./skills/engineering/running-tdd-cycles/SKILL.md): Runs a strict red-green-refactor loop one requirement at a time.
- [`reviewing-changes`](./skills/engineering/reviewing-changes/SKILL.md): Reviews diffs across code, security, architecture, and acceptance.
- [`designing-architecture`](./skills/engineering/designing-architecture/SKILL.md): Designs architecture with a TDD-ready implementation plan.
- [`creating-block-issues`](./skills/engineering/creating-block-issues/SKILL.md): Publishes minimal GitHub issues per tasks.md block.
- [`committing-changes`](./skills/engineering/committing-changes/SKILL.md): Lands work with branch, hook, message, and PR discipline.
- [`implementing-blocks`](./skills/engineering/implementing-blocks/SKILL.md): Builds one tasks.md block with TDD, review, PR, and CI loop.
- [`shell-discipline`](./skills/engineering/shell-discipline/SKILL.md): Keeps shell commands auditable, one intent per call.
- [`engineering-philosophy`](./skills/engineering/engineering-philosophy/SKILL.md): Weights decisions with KISS, YAGNI, DRY, and SOLID.
- [`ponytail`](./skills/engineering/ponytail/SKILL.md): Builds the laziest working solution at adjustable intensity.

### Productivity

#### User-invoked

- [`grill-me`](./skills/productivity/grill-me/SKILL.md): Interviews you about a plan without writing repository state.
- [`handoff`](./skills/productivity/handoff/SKILL.md): Writes a compact handoff for another session or agent.
- [`wait-what`](./skills/productivity/wait-what/SKILL.md): Re-explains a message that did not land.
- [`automate-me`](./skills/productivity/automate-me/SKILL.md): Creates or updates a personal mode skill from repeated preferences.
- [`reflect`](./skills/productivity/reflect/SKILL.md): Turns durable session lessons into approved skill edits.
- [`technical-writing`](./skills/productivity/technical-writing/SKILL.md): Writes and reviews technical documentation.

#### Model-invoked

- [`grilling`](./skills/productivity/grilling/SKILL.md): Provides the reusable interview method behind several workflows.
- [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md): Guides writing for skills and other agent-facing documents.
- [`unslop`](./skills/productivity/unslop/SKILL.md): Removes AI writing tells and keeps prose concrete.

## Custom skills

- [`copse`](./skills/engineering/copse/SKILL.md): The custom Copse issue tracker integration for the engineering skills.

## Adapted skills

Eighteen skills are adapted from third-party sources (MIT licensed) and rewritten for this repo's conventions: the `review`, `commit`, `tdd`, `block-issues`, `design`, `block-implement`, `running-tdd-cycles`, `reviewing-changes`, `designing-architecture`, `creating-block-issues`, `committing-changes`, `implementing-blocks`, `shell-discipline`, and `engineering-philosophy` skills come from [swell-agents/coding-skills](https://github.com/swell-agents/coding-skills); `ponytail` comes from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail); and `how`, `why`, `create-verification-skill`, and `maintain-verification-skill` come from the pstack plugin by Lauren Tan (shipped in the Cursor plugins collection).

## Utility skills

These skills are kept in `skills/misc/` and are not included in the plugin.

- [`git-guardrails-claude-code`](./skills/misc/git-guardrails-claude-code/SKILL.md): Blocks dangerous Git commands with Claude Code hooks.
- [`migrate-to-shoehorn`](./skills/misc/migrate-to-shoehorn/SKILL.md): Replaces test type assertions with `@total-typescript/shoehorn`.
- [`scaffold-exercises`](./skills/misc/scaffold-exercises/SKILL.md): Creates exercise, problem, solution, and explainer directories.
- [`setup-pre-commit`](./skills/misc/setup-pre-commit/SKILL.md): Configures Husky, lint-staged, formatting, type checking, and tests.

## Development

Keep the manifests, bucket READMEs, docs pages, and skill metadata in sync when adding or moving a promoted skill. Run:

```bash
claude plugin validate . --strict
git diff --check
```

Use [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md) when editing a skill or agent-facing document. Apply [`unslop`](./skills/productivity/unslop/SKILL.md) to prose changes.
