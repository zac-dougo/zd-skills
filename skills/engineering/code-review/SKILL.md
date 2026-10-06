---
name: code-review
description: Review a PR, branch, commit range, staged changes, or uncommitted work for defects, regressions, spec compliance, and documented standards. A formal spec is optional.
---

# Code review

Read [working guidance](../../shared/working-guidance.md) once for this task. Review the requested scope without modifying it unless the user also asks for fixes.

## Select and record the comparison

Inspect `git status --short`, the current branch, and any PR context. Honour the user's scope. Infer the base from the PR or repository default branch when unambiguous; ask only when plausible scopes would review materially different work.

| Requested scope | Comparison |
| --- | --- |
| PR or committed branch | Resolve the base and head to commit IDs. Compute their merge-base, then compare that commit to the captured head. |
| Since an exact commit, tag, or revision | Compare the resolved revision directly with the captured head. Use merge-base only if the user asks for branch divergence. |
| Staged only | `git diff --cached` |
| Unstaged only | `git diff`, plus relevant untracked files |
| Uncommitted work | `git diff HEAD`, plus relevant untracked files |
| Branch including local work | Compare the resolved branch merge-base with the working tree, plus relevant untracked files. |

Use `git ls-files --others --exclude-standard` to discover untracked files, then read only relevant files. Do not stage files to review them. On an unborn branch, compare staged files against the empty tree with `git diff --cached` and inspect working and untracked files directly. If a remote PR lacks a local checkout, review its fetched diff and file contents and state any limits on runtime checks.

Record which commits and local layers are included. Validate refs before proceeding. An empty committed diff does not imply an empty working tree. When the requested scope is empty, say so. If local files change during review, reconcile the findings with the current diff before reporting them.

## Establish the requirements

Read supplied requirements, the current task, the PR description and linked issues, and relevant repository standards. Follow the configured tracker if present. A missing tracker config or formal spec does not block correctness review. State which requirement sources were available; do not invent a spec.

Read affected callers, tests, and contracts as needed to establish impact beyond the changed lines.

## Review the change

- **Correctness:** concrete failures, regressions, data loss, incorrect state transitions, error paths, concurrency, authorization, and compatibility where relevant.
- **Spec:** missing or incorrect agreed behaviour, unsupported assumptions, and changes outside the requested scope.
- **Standards:** violations of documented project requirements that matter to correctness or maintenance. Treat design smells as leads to investigate, not findings by themselves. Suppress style preferences and checks already enforced by tooling.

A small review can run inline. For a substantial change, use bounded independent reviewers when delegation is available and authorized. Give each the captured scope, relevant requirements, and a distinct concern. Tell reviewers to perform their review directly without invoking this skill again or spawning more reviewers. Verify every returned finding against the code before reporting it.

## Report actionable findings

Deduplicate findings and order them by severity across all concerns. Retain labels such as Correctness, Spec, and Standards so the reason remains clear. For each finding, provide the affected file and precise lines, the trigger, the consequence, and supporting evidence. Distinguish confirmed defects from material uncertainties. Do not manufacture findings or require a finding count.

Use the host's inline review format when available. Finish with a brief account of scope, checks performed, and remaining gaps. Say when no actionable findings were found, without claiming that untested behaviour is proven safe. Re-review after meaningful fixes or new evidence, not indefinitely to chase a perfectly empty report.
