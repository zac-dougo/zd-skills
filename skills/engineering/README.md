# Engineering

Skills I use daily for code work.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; other harnesses: their own equivalent).

- **[to-spec](./to-spec/SKILL.md)**: Synthesizes agreed behaviour into a proportionate, verifiable spec.
- **[blast-radius](./blast-radius/SKILL.md)**: Find what a change could break beyond its diff and check the conditions its safety depends on.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[prototype](./prototype/SKILL.md)**: Build a throwaway prototype to answer a design question: a single shareable HTML file for state/logic, or several toggleable UI variations.
- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)**: Diagnoses bugs with evidence and meaningful verification, scaling the investigation to uncertainty and impact.
- **[research](./research/SKILL.md)**: Investigate a question against primary sources and return cited findings, delegating useful independent work and saving a document when needed.
- **[domain-modeling](./domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model by challenging terms, stress-testing with scenarios, and updating `CONTEXT.md` and ADRs inline.
- **[code-review](./code-review/SKILL.md)**: Reviews committed and local changes for defects, regressions, requirements, and documented standards, with findings ordered by severity.
- **[designing-architecture](./designing-architecture/SKILL.md)**: Designs interfaces, data flow, and migrations at the depth the decision needs.
- **[committing-changes](./committing-changes/SKILL.md)**: Commits and delivers authorized work while preserving existing hooks and CI.
