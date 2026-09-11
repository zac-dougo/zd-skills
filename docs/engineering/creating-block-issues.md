## What it does

`creating-block-issues` generates one minimal GitHub issue per Spec Kit `tasks.md` block: pointer, heading, a one-or-two-sentence summary, and task IDs, with a dispatch label and native Blocked-by relations.

The minimal body is the contract. Constitution, acceptance criteria, and conventions stay in `tasks.md`; the issue is a tracking hook, and anything duplicated into it drifts.

## When to reach for it

Type `/creating-block-issues`, or the agent reaches for it automatically when a task fits: it is model-invoked, and fires on Spec Kit projects needing per-block tracking issues. The [block-issues](https://aihero.dev/skills-block-issues) skill is its user-invoked front door.

| Your situation | Reach for |
| --- | --- |
| A Spec Kit feature needs per-block issues | `creating-block-issues` |
| Only an arbitrary task subset needs one issue | Subset mode: explicit task IDs plus a title |
| No block structure exists in `tasks.md` | Fix `tasks.md` first, or create issues manually |

## Common questions

**What if some tasks fall outside every block?**
That is an error, not a silent skip. Uncovered tasks would never get an issue and the feature would ship without its closeout. The skill reports the orphaned IDs and asks whether to fix `tasks.md` first or proceed with the gap explicit.

**Which labels go on?**
Exactly one: the dispatch label (default `swa-impl-block`, overridable). Priority, milestone, and readiness labels are the project's concern and go on afterward.

## It's working if

- Every issue body matches the template: five lines at most, no recaps, no boilerplate.
- Dependencies live in GitHub's native Blocked-by graph, not in body text.
- Nothing was created in a repo whose remote wasn't echoed first.

## Where it fits

`creating-block-issues` is the planning-side companion to [implementing-blocks](https://aihero.dev/skills-implementing-blocks), which consumes exactly the issues (and the dispatch signal) this skill creates. Both live or die by the same `tasks.md`.
