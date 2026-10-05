---
name: committing-changes
description: Commit intended changes on a feature branch and open or update a PR, preserving existing hooks and CI. Use when the user asks to commit, push, or prepare a PR.
---

# Committing changes

Read [working guidance](../../shared/working-guidance.md) once for this task.

## Establish the scope

Inspect status, the staged and unstaged diffs, the current branch, remotes, and the repository's contribution instructions. Preserve unrelated user changes. Use the user's requested commit scope or infer it from the completed task; ask only if mixed changes make ownership ambiguous.

Keep the requested endpoint: a request for a local commit does not automatically request a push or PR. A request to deliver through a PR includes the necessary branch, commit, push, and PR work. Check for an existing PR before creating one.

## Commit and deliver

1. Identify the repository's default branch from its remote or project configuration. If on that branch, create a descriptive feature branch. Respect an existing task branch.
2. Run the repository's applicable formatter, linter, and required checks. Scope automatic fixes to intended files. Preserve and run existing hooks; investigate failures rather than bypassing them.
3. Stage specific intended paths and inspect the staged diff. Commit one logical change with the repo's message convention. If none is documented, use an imperative subject of at most 72 characters, starting with a capital and without a trailing period. Do not add attribution trailers unless required by the project or requested by the user.
4. If publishing is authorized, push the feature branch without force. Open or update its PR with the concrete problem, changed behaviour, and actual verification results. Attach the PR to the current task when the host offers that capability.
5. Report the commit or PR and any checks that could not be completed. Leave PR merging to the user unless they explicitly request it.

Sync with the default branch only when needed for conflicts, required checks, or repository policy. Fetch it and use the repo's preferred integration method. Merging the default branch into the feature branch is allowed; merging the feature branch into the default branch or merging its PR is a separate user-controlled action. Preserve published history and do not force-push. Re-run affected checks after resolving conflicts.

## Repository setup is separate

Routine commits do not install hooks, add workflows, change `.gitattributes`, or delete branches. Use [setup-matt-pocock-skills](../setup-matt-pocock-skills/SKILL.md) when the user explicitly requests repository setup. Its optional Git checks refer to [repository setup](reference/repository-setup.md).

There is no universal PR line limit. Follow a configured limit; otherwise split changes when it improves independent review and verification.
