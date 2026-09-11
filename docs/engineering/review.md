## What it does

`review` runs a four-pass quality gate over a diff or a PR: code quality, security, architecture, and acceptance. Each pass returns a verdict, and the skill aggregates them into one Quality Gate Summary table with ordered action items.

It never edits the diff. A review that rewrites the code it grades is not a review; this one reports, and the fixes happen elsewhere.

## When to reach for it

You invoke this by typing `/review`, and the agent won't reach for it on its own. Pass a scope (a diff range or PR number), or nothing for `main...HEAD`. Add the `ai-native` keyword only when you want the opt-in fifth pass.

| Your situation | Reach for |
| --- | --- |
| A diff or PR needs a broad quality verdict | `review` |
| A change needs checking against its spec and repo standards | [code-review](https://aihero.dev/skills-code-review) |
| Something is broken and you don't know why | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

## The gate

Four passes, one table. Code hunts over-engineering and duplication; security audits against OWASP; architecture checks boundaries and layering; acceptance asks whether the diff solves the linked issue. The table is the artifact: a verdict per pass plus every Critical and Major finding with rule, location, and fix. Minor findings appear only when the overall verdict is PASS, as polish.

## Common questions

**Should the fifth pass run by default?**
No. The AI-native pass grades the repo against AI-coding practices, and some repos deliberately don't follow them. It runs only on the `ai-native` keyword or an explicit ask.

## It's working if

- The report arrives as one summary table, not four separate essays.
- Every Critical and Major finding names its rule, its `file:line`, and a concrete fix.
- Minor findings stay out unless the verdict is PASS.

## Where it fits

`review` is a reach-for-it-anytime standalone and the user-invoked front door to [reviewing-changes](https://aihero.dev/skills-reviewing-changes), which holds the pass procedures it runs. Its closest neighbour is [code-review](https://aihero.dev/skills-code-review): that one checks a diff against its originating spec and repo standards, this one renders a broad quality verdict.
