## What it does

Finds the cause of a reported bug and verifies the correction with evidence tied to the actual symptom. It permits a short path for obvious failures and deeper investigation for uncertain or high-impact problems.

## When to reach for it

Report something broken, failing, or slow, or invoke `$diagnosing-bugs` in Codex or `/diagnosing-bugs` in Claude Code.

## Common questions

**Can it read code before building a reproduction?**

Yes. Source inspection and initial hypotheses can help create the right reproduction. The final claim still needs evidence.

**What if the bug cannot be reproduced locally?**

It continues useful investigation, labels tentative conclusions, and identifies the missing evidence. It does not claim runtime verification it could not perform.

**Does every fix need a new test?**

Meaningful behaviour bugs should gain suitable regression coverage when feasible. A low-impact reversible change may be adequately checked by existing tests or direct observation.

## It's working if

- The check could detect your reported symptom.
- The explanation distinguishes the cause from an unverified hypothesis.
- Temporary instrumentation is removed and remaining verification limits are stated.

## Where it fits

Use this for failures with an unknown cause. code-review examines a defined change, and project verification skills exercise known user journeys. See the [collection guide](https://github.com/zac-dougo/zd-skills/blob/main/README.md) for related workflows.
