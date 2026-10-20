---
name: blast-radius
description: Find what a change could break beyond its diff and check the conditions its safety depends on.
disable-model-invocation: true
---

Read [working guidance](../../shared/working-guidance.md) once for this task.

# Blast radius

Find consequential breakage outside the changed lines. Use for "what could this break", hidden consumers, or a small diff whose downstream effects are unclear.

Read affected interfaces and callers to understand the change. Consult project vocabulary and decisions when relevant. Read and follow [domain-modeling](../domain-modeling/SKILL.md) only when the task calls for developing the model, rather than merely consuming its terminology.

## Trace the actual change

Establish the requested diff and intent. Identify changed behavior, contracts, and assumptions, including behavior omitted from the diff. Follow hidden consumers where relevant: serialized data, database readers, feature flags, library versions and patches, teardown timing, and downstream systems.

Prioritize concrete exposure and consequences. Do not invent callers or assign numerical probabilities without evidence. A negative search narrows what was found; it does not prove no consumer exists outside the search scope.

## Check the safety conditions

Identify the conditions the change depends on. There may be one or several independent conditions; keep each material condition visible instead of forcing all risks into one explanation.

For each condition, use evidence suited to the claim:

- Source references and contract analysis for behavior that can be established from code or a specification.
- Type checks, existing tests, or a focused regression check for executable behavior.
- An integration exercise or running-app reproduction when timing, external state, or interactions matter.

Prefer the least costly check that could distinguish the claimed safe behavior from the failure. Write a temporary script or test when it adds evidence the existing checks cannot provide. Running code is useful evidence for the cases exercised, not universal proof of safety.

State what was observed, what follows from source analysis, and what remains uncertain. Mark a condition as supported, contradicted, or unverified with its evidence and limits. Do not call the whole change safe merely because one condition held or one example passed.

## Report the result

- **Changed behavior.** What changes and which consumers may be affected.
- **Safety conditions.** Each material condition, its status, evidence, and remaining limitations.
- **Risks.** The trigger, consequence, affected code or contract, and a useful check. Separate confirmed defects from consequential uncertainty.
- **Cleared concerns.** What was investigated and why the available evidence addresses it.
- **Remaining checks.** The smallest unresolved verification step, if any.

Keep the report proportionate. Use real source locations, follow [unslop](../../productivity/unslop/SKILL.md) for prose, and redact private material before public sharing. This investigation does not itself authorize a merge or publication.
