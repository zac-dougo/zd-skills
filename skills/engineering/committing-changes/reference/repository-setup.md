# Optional Git checks

Use only when the user asks to configure repository hooks or CI. Installing this skill or committing a change is not a setup request.

Inspect the existing hook manager, `core.hooksPath`, actual Git hooks directory, CI workflows, and contribution rules. Preserve existing checks and project conventions. If the requested setup leaves a material choice unresolved, show the proposed configuration and ask about that choice before changing it.

The bundled scripts are examples with limited assumptions:

- `scripts/install-hooks.sh` copies `commit-msg` and `pre-push`; it does not install `pre-commit`. It derives its destination from `git rev-parse --git-dir` and does not account for every hook-manager or linked-worktree layout.
- `scripts/install-pr-size-workflow.sh` copies the bundled workflow and appends `.gitattributes` exclusions. Its template applies a 1000-line gate excluding selected file categories. Use that threshold only when explicitly selected for this repository.

Both installers can replace existing files. Do not run either over different existing files or a custom hooks setup. Prefer integrating the selected checks into the existing mechanism. Run a bundled installer only after verifying its destinations are appropriate, absent or identical, and within the requested setup scope. In a linked worktree or custom hook configuration, install through the repository's actual hook mechanism instead.

Review the resulting diff and validate the chosen checks. Report exactly which checks were installed. Keep setup changes independently reviewable from application work.
