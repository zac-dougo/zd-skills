---
name: to-spec
description: Synthesize the current conversation into a proportionate spec and publish it to the configured tracker when requested.
disable-model-invocation: true
---

# To spec

Read [working guidance](../../shared/working-guidance.md) once for this task. Synthesize the agreed outcome from the conversation and relevant code. Do not start a new interview or reopen settled decisions.

Read relevant project vocabulary, contracts, and ADRs. Distinguish agreed requirements from assumptions and unresolved decisions. Prefer existing verification seams. Ask only when a missing decision materially changes the promised behaviour, scope, compatibility, or acceptance criteria; do not pause merely to obtain approval of a routine test seam.

Write the shortest spec that makes the work implementable and verifiable:

- The user's problem and the intended observable behaviour.
- Acceptance criteria covering the actual requirements and relevant failure cases. Use user stories when helpful; no minimum count or exhaustive template is required.
- Consequential implementation decisions and contracts already agreed.
- Verification that could detect unmet requirements, including relevant existing checks.
- Out-of-scope work and any unresolved consequential decisions.

Keep implementation detail only when it records a decision or helps locate the work. A precise state model, schema, contract, or current source path can be useful; distinguish it from a requirement that must remain true after code moves.

Honour the requested destination. Invoking this workflow normally includes publishing to an already configured project tracker, unless the user requests a draft or local document. If no destination is established, prepare the complete spec first and ask where to publish while preserving the draft. Use the tracker's workflow and label vocabulary. Apply a readiness label only when no unresolved decision blocks implementation.

Report the spec location and any remaining decision. Creating the spec does not itself authorize implementation.
