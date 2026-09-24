# Engineering

Skills I use daily for code work.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; other harnesses: their own equivalent).

- **[grill-with-docs](./grill-with-docs/SKILL.md)**: Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs inline.
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[to-spec](./to-spec/SKILL.md)**: Turn the current conversation into a spec and publish it to the issue tracker.
- **[to-tickets](./to-tickets/SKILL.md)**: Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, whether as text in a local file or as native blocking links on a real tracker.
- **[show-me-your-work](./show-me-your-work/SKILL.md)**: Keep a reviewable TSV decision trail for long-running or unattended work.
- **[blast-radius](./blast-radius/SKILL.md)**: Find what a change could break beyond its diff and prove the central safety fact.
- **[commit](./commit/SKILL.md)**: Commit on a feature branch and open a PR.
- **[design](./design/SKILL.md)**: Produce a pre-implementation architecture plan.
- **[how](./how/SKILL.md)**: Explain how a subsystem works, or critique its architecture once you understand it.
- **[why](./why/SKILL.md)**: Investigate why code looks the way it does, with cited evidence and calibrated confidence.
- **[create-verification-skill](./create-verification-skill/SKILL.md)**: Generate a project-local skill that drives an app the way a user does, to prove behavior.
- **[maintain-verification-skill](./maintain-verification-skill/SKILL.md)**: Audit a project's verification skill and feature map, shipping at most one PR of proven corrections.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[prototype](./prototype/SKILL.md)**: Build a throwaway prototype to answer a design question: a single shareable HTML file for state/logic, or several toggleable UI variations.
- **[copse](./copse/SKILL.md)**: Use Copse records and worktree links as the local issue tracker for the engineering skills.
- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)**: Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- **[research](./research/SKILL.md)**: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.
- **[domain-modeling](./domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model by challenging terms, stress-testing with scenarios, and updating `CONTEXT.md` and ADRs inline.
- **[codebase-design](./codebase-design/SKILL.md)**: Shared discipline and vocabulary for designing deep modules: small interfaces, clean seams, testable through the interface.
- **[code-review](./code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: **Standards** (does it follow the repo's coding standards, plus a Fowler smell baseline?) and **Spec** (does it faithfully implement the originating issue/spec?), run as parallel sub-agents.
- **[resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md)**: Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation, never `--abort`.
- **[wizard](./wizard/SKILL.md)**: Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.
- **[designing-architecture](./designing-architecture/SKILL.md)**: Pre-implementation architecture with an implementation-ready plan.
- **[committing-changes](./committing-changes/SKILL.md)**: Branch, hooks, commit rules, and PR discipline.
- **[shell-discipline](./shell-discipline/SKILL.md)**: One command per call, no inline env vars, explicit auth.
- **[engineering-philosophy](./engineering-philosophy/SKILL.md)**: KISS, YAGNI, DRY, SOLID judgment weights.
- **[ponytail](./ponytail/SKILL.md)**: Laziest working solution: YAGNI, stdlib first, shortest diff.
