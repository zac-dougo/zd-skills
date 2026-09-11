## What it does

`why` investigates the motivation behind code: design rationale, trade-offs, motivating incidents, thresholds nobody documented. It anchors in the code (blame, history, PRs), fans out parallel investigators across every evidence source with an integration (tickets, docs, chat, observability, errors, analytics), and synthesizes into confidence-weighted findings.

Its defining constraint is the epistemics framework. Every claim lands in a tier (Direct, Supported, Inferred, Speculative, Unknown) with matching phrasing, and gaps are reported as findings, not papered over.

## When to reach for it

You invoke this by typing `/why`, and the agent won't reach for it on its own. Reach for it when the question is about forces, not mechanics: why this shape, why this threshold, why this workaround.

| Your situation | Reach for |
| --- | --- |
| Why does the code look this way | `why` |
| How does it work at runtime | [how](https://aihero.dev/skills-how) |
| Something is broken and you don't know why | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

## The coverage map

Seven evidence categories, one investigator each, plus a written justification for anything skipped. Source control always runs (git and `gh` are guaranteed); the other six run wherever an integration exists and are recorded as explicit gaps where none does. A null result with its queries listed beats a skipped category every time.

## Common questions

**What if the evidence contradicts itself?**
Both sides ship. The PR says cleanup, the ticket says compliance: the output presents both with citations and lets the reader decide. Picking the tidier narrative is the exact failure mode the skill exists to prevent.

**Can it answer from one PR description?**
Only after confirming the other searches would be redundant, and only rarely. A single-commit answer that skips the coverage map is a guess with a citation attached.

## It's working if

- Every Direct claim has an adjacent citation; every Inferred claim is hedged.
- Sources Consulted lists one line per investigator, including empty and skipped ones with reasons.
- The output names what it doesn't know, specifically.

## Where it fits

`why` is a reach-for-it-anytime standalone for design archaeology. Its companion is [how](https://aihero.dev/skills-how): mechanics there, motivation here. When its findings precede a change, they convert into a Preserve / Change / Avoid / Risk constraint set for planning, which feeds [grill-with-docs](https://aihero.dev/skills-grill-with-docs) or [to-spec](https://aihero.dev/skills-to-spec).
