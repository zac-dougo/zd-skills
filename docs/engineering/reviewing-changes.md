## What it does

`reviewing-changes` reviews a diff in four passes: code quality, security, architecture, and acceptance. Findings flow into one combined verdict with a Quality Gate Summary table and ordered action items.

It is read-only. The skill reports; it never edits the diff it grades.

## When to reach for it

Type `/reviewing-changes`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires on reviewing a branch, a PR, or anything "since X". The [review](https://aihero.dev/skills-review) skill is its user-invoked front door and adds the opt-in AI-native pass.

| Your situation | Reach for |
| --- | --- |
| A diff needs a broad quality verdict | `reviewing-changes` |
| A change needs checking against its spec and repo standards | [code-review](https://aihero.dev/skills-code-review) |
| A Spec Kit block needs the full loop, not just review | [block-implement](https://aihero.dev/skills-block-implement) |

## The four passes

Code hunts over-engineering, duplication, and SOLID drift. Security audits against OWASP with attack vectors attached. Architecture checks layering, boundaries, and whether a library should have been used instead. Acceptance asks whether the diff solves the contract: the linked issue, the PR description, or the Spec Kit block. Severity matches reality: Critical ships a bug or a CVE today, Major hurts within six months, Minor is style.

## Common questions

**Does it fix what it finds?**
No. Fixes happen where the work happens (a TDD cycle, a fix commit), then review re-runs against the new HEAD. A reviewer that edits is an author with extra steps.

## It's working if

- The report is one table plus Critical and Major findings, each with rule, `file:line`, and fix.
- Severity tracks impact, not confidence: theoretical attacks land Minor.
- The repo's own conventions outrank the skill's defaults everywhere they disagree.

## Where it fits

`reviewing-changes` is a reach-for-it-anytime standalone and the review engine behind [review](https://aihero.dev/skills-review) and the review loop in [implementing-blocks](https://aihero.dev/skills-implementing-blocks). Its closest neighbours are [engineering-philosophy](https://aihero.dev/skills-engineering-philosophy), which weights its code-quality pass, and [committing-changes](https://aihero.dev/skills-committing-changes), whose hygiene it checks.
