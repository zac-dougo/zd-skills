## What it does

`prototype` creates throwaway code to answer a design question. It makes the relevant state or UI choices visible so you can react to a concrete experiment.

A prototype request ends with the runnable experiment, observed findings, and remaining uncertainty. It does not automatically promote code into production, create commits, update issues, or archive the experiment.

## When to reach for it

Type `/prototype`, or the agent reaches for it automatically when a design question benefits from an experiment.

| The question | The artifact |
| --- | --- |
| Does this logic or state model handle the cases we care about? | A shareable HTML demo with visible state and guided scenarios |
| What should this screen look like? | Distinct UI variants using the project's conventions |
| Why is an existing feature broken? | Use [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

## Review the experiment

The prototype stays small and runnable. Logic demos expose state transitions; UI variants differ in layout and information hierarchy. Persistence is isolated unless it is part of the question.

When production implementation is already authorized, the agent can continue with the chosen approach using normal project checks and conventions. Prototype shortcuts are not a substitute for production quality.

## Common questions

**Will choosing a variant automatically change production code?**

Only when implementation is already within the requested scope. Otherwise the result records the selection and findings for a later decision.

**Must every prototype be committed on its own branch?**

No. Preservation, commits, issue updates, and cleanup follow the user's requested scope. The runnable artifact remains available for review.

## It's working if

- The prototype states the question it is exploring.
- You can run it and observe the relevant state or compare distinct UI choices.
- Findings distinguish observed behavior from untested cases.
- Subsequent implementation or repository changes happen only within the agreed scope.

## Where it fits

[grilling](https://aihero.dev/skills-grilling) can identify a question that needs a prototype. The findings can inform [designing-architecture](https://aihero.dev/skills-designing-architecture) or become settled input for [to-spec](https://aihero.dev/skills-to-spec).
