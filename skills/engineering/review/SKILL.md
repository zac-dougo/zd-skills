---
name: review
description: Run the four-pass quality gate (code, security, architecture, acceptance) over a diff or PR.
disable-model-invocation: true
---

# Review

Run the `reviewing-changes` skill over a scope. If arguments are passed, they are the scope; if empty, default to `git diff main...HEAD`. If the scope looks like a PR number, resolve it with `gh pr diff <N>`; otherwise pass it through verbatim as the diff range (after stripping the `ai-native` keyword, see below).

Call the Skill tool with `reviewing-changes` on the scope. Run its four default passes (code quality, security audit, architecture consistency, and acceptance: does the diff solve the linked issue?) in parallel subagents when the harness supports them, sequentially inline otherwise. The trade-off is no parallelism, but the procedure is identical.

**Opt-in fifth pass**: only when the arguments contain the keyword `ai-native` (or the user explicitly asks for it), also run the AI-native-coding pass against `reviewing-changes/reference/ai-native-rubric.md`. Do not run it by default: some repos are deliberately not AI-native and should not be graded against that rubric.

Each pass returns a verdict (`PASS / NEEDS WORK / FAIL`) plus findings. Aggregate into one Quality Gate Summary table:

```
## Quality Gate Summary

| Review             | Verdict        | Critical | Major | Minor |
|--------------------|----------------|----------|-------|-------|
| Code               | pass/warn/fail | N        | N     | N     |
| Security           | pass/warn/fail | N        | N     | N     |
| Architecture       | pass/warn/fail | N        | N     | N     |
| Acceptance         | pass/warn/fail | N        | N     | N     |

**Overall**: PASS / NEEDS WORK / FAIL

### Action items
1. <Critical/Major items, ordered>
```

Append an `AI-Native Practices` row only when the opt-in pass ran. Then list every Critical and Major finding with `Rule / Severity / Location / Issue / Fix`. Skip Minor unless the overall verdict is PASS (then include them as polish).
