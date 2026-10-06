## What it does

Reviews the requested committed or local changes for defects, regressions, requirements, and documented standards. Findings are checked against the code and ordered by severity, with their Correctness, Spec, or Standards labels retained.

## When to reach for it

Ask for a review or invoke `$code-review` in Codex or `/code-review` in Claude Code. State whether you mean a PR, a commit range, staged changes, or working-tree changes when that distinction matters. A missing formal spec does not block correctness review.

## Common questions

**Does it review uncommitted work?**

Yes. It distinguishes staged, unstaged, and combined local changes and reads relevant untracked files. It reports the selected scope instead of silently reviewing only HEAD.

**Does every review need multiple agents?**

No. Small reviews run inline. Substantial reviews may use bounded independent reviewers when permitted, and their findings are verified before reporting.

**Will it keep finding style preferences?**

The report focuses on actionable defects and meaningful documented requirements. Generic smells are investigation leads, and checks already enforced by tooling are omitted.

## It's working if

- The report states which committed and local changes it includes.
- Each finding explains a concrete trigger and consequence at precise source lines.
- An absent spec or unrun check appears as a limitation, not an invented pass.

## Where it fits

Use it after implementation or independently on existing changes. A focused bug investigation uses diagnosing-bugs; a deeper search for hidden consumers uses blast-radius. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
