# Engineering

Skills I use daily for code work.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; other harnesses: their own equivalent).

- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)**: Configures requested tracker and domain conventions, with Git checks only when explicitly requested.
- **[wayfinder](./wayfinder/SKILL.md)**: Plan a multi-session effort as a shared map of decision tickets.
- **[grill-with-docs](./grill-with-docs/SKILL.md)**: Resolves consequential questions and records settled terminology and decisions.
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[to-spec](./to-spec/SKILL.md)**: Synthesizes agreed behaviour into a proportionate, verifiable spec.
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
- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)**: Diagnoses bugs with evidence and meaningful verification, scaling the investigation to uncertainty and impact.
- **[research](./research/SKILL.md)**: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.
- **[domain-modeling](./domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model by challenging terms, stress-testing with scenarios, and updating `CONTEXT.md` and ADRs inline.
- **[codebase-design](./codebase-design/SKILL.md)**: Shared discipline and vocabulary for designing deep modules: small interfaces, clean seams, testable through the interface.
- **[code-review](./code-review/SKILL.md)**: Reviews committed and local changes for defects, regressions, requirements, and documented standards, with findings ordered by severity.
- **[resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md)**: Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation, never `--abort`.
- **[wizard](./wizard/SKILL.md)**: Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.
- **[designing-architecture](./designing-architecture/SKILL.md)**: Designs interfaces, data flow, and migrations at the depth the decision needs.
- **[committing-changes](./committing-changes/SKILL.md)**: Commits and delivers authorized work while preserving existing hooks and CI.
- **[ponytail](./ponytail/SKILL.md)**: Laziest working solution: YAGNI, stdlib first, shortest diff.
