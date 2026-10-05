---
name: diagnosing-bugs
description: Diagnose and fix reported bugs or performance regressions using evidence and checks that detect the actual symptom. Scale investigation to the uncertainty.
---

# Diagnosing bugs

Read [working guidance](../../shared/working-guidance.md) once for this task. Establish what failed, find its cause, and verify the requested correction. Read relevant project context and ADRs when present. Redact secrets from commands, logs, and captured artifacts.

## Establish the symptom

Inspect the error, affected code, recent changes, and available tests or logs. Reading code and forming an initial hypothesis are legitimate ways to build a reproduction. An obvious failure with direct evidence can take a short path; uncertain, intermittent, or high-impact failures need deeper investigation.

Seek a feedback signal that can distinguish the reported bug from a successful result. Prefer an existing test, a focused regression test, a CLI fixture, an HTTP request, a UI exercise, or a replay of a redacted trace. For harder cases, consider a temporary harness, bisection, fuzzing, or a differential check. Choose the least costly method that exercises the real failure.

## Investigate uncertainty

Make the reproduction smaller, faster, and more deterministic when that helps distinguish causes. Do not spend time minimizing an already convincing simple reproduction. For intermittent failures, record observed frequency, sample count, environment, and limitations; a low reproduction rate is evidence, not a reason to declare the bug undebuggable.

Use competing hypotheses when the cause is ambiguous. Each should predict an observable result, and the next check should distinguish plausible causes. There is no required hypothesis count. Share consequential findings with the user and continue authorized investigation without waiting for routine confirmation.

Use targeted instrumentation or a debugger. For performance issues, establish a measured baseline before claiming improvement. Change one relevant variable at a time when testing causality. Tag temporary instrumentation so it can be removed reliably.

If reproduction is unavailable, continue useful read-only investigation and label conclusions as tentative. Explain the missing evidence. Request access or a redacted artifact only when needed to proceed; changes to production instrumentation need appropriate authorization. Do not claim a fix is verified when the relevant check could not run.

## Fix and verify

Use the smallest correction supported by the evidence. For a meaningful behaviour bug, add a regression test at a seam that exercises the actual failure when feasible, and demonstrate that it fails before the fix and passes afterward. A shallow test that misses the real interaction is not a substitute. Reversible, low-impact changes may need only existing checks or a direct observation.

Re-run the original scenario and the affected project checks. State any missing regression coverage or environment limitation. Remove temporary instrumentation and keep captured artifacts out of the commit unless intentionally needed as fixtures. Report the cause, correction, and actual evidence; do not repeatedly broaden testing after the relevant checks pass without a new reason.

When only the user can reproduce the behaviour, use [the human-assisted loop template](scripts/hitl-loop.template.sh) if a repeatable capture would help. Prefer available agent tools when they can perform the same check.
