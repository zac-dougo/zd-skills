## What it does

`blast-radius` investigates what a change could break outside its diff. It traces affected contracts, hidden consumers, and the conditions the change's safety depends on.

It keeps independent conditions separate and distinguishes source analysis, observed behavior, and unresolved uncertainty. One passing example does not establish that the entire change is safe.

## When to reach for it

Invoke `/blast-radius` when a small-looking change has unclear downstream effects or hidden consumers. The agent does not invoke it automatically. Use [code-review](https://aihero.dev/skills-code-review) for a broader review of correctness and requirements.

## Evidence suited to the risk

The investigation can use source and contract analysis, type checks, focused tests, or a running-app exercise. It selects checks that could detect the actual failure and states the limits of each result.

## Common questions

**Must every condition have a runtime test?**

No. Some conditions can be supported by source or contract analysis. Interactions and timing may need execution. The report identifies the evidence used and any remaining gaps.

**What if there are several independent risks?**

Each material safety condition stays visible with its own evidence and status. The report does not force them into a single explanation.

## It's working if

- The report names changed behavior and affected consumers.
- Each material safety condition has evidence, a status, and clear limitations.
- Risks identify a trigger and consequence rather than hypothetical callers.
- Remaining checks address concrete gaps in the evidence.

## Where it fits

`blast-radius` complements [code-review](https://aihero.dev/skills-code-review). [domain-modeling](https://aihero.dev/skills-domain-modeling) is relevant when investigating a contract reveals a domain-model question that needs resolving.
