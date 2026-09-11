## What it does

`create-verification-skill` generates a project-local skill that drives a repo's app the way a user does: launch, doctor, drive, evidence, cleanup, plus a feature map of the top user-facing features. The output is written for the next agent to read cold, mid-task, not for a human.

It interviews the repo before generating: surface, run command, driving harness, observable evidence, isolation. If the checkout doesn't build, that gets fixed first; a skill written against a broken base teaches wrong steps.

## When to reach for it

You invoke this by typing `/create-verification-skill`, and the agent won't reach for it on its own. Reach for it when a project has no scripted way to prove UI, CLI, or service behavior, and every proof is currently a manual session.

| Your situation | Reach for |
| --- | --- |
| No scripted proof exists for the app | `create-verification-skill` |
| A verification skill exists but has rotted | [maintain-verification-skill](https://aihero.dev/skills-maintain-verification-skill) |
| The change is a library with unit tests | The test suite plus [code-review](https://aihero.dev/skills-code-review) is enough |

## A draft is not a deliverable

The generated skill is executed once before handover: launch, doctor, one mapped feature driven, evidence captured, cleanup run, evidence confirmed surviving. Anything that fails gets fixed, including cleanup after failed iterations so broken attempts strand no processes or ports.

## Common questions

**Where does the generated skill live?**
In the target repo's project skill directory (e.g. `.agents/skills/verify-<app>/`), located first. The skill is project-local on purpose: its launch commands, selectors, and seed data only make sense in that repo.

**What goes in the feature map?**
The top user-facing features with four sections each: sub-features, how to reach it, how to drive it, gotchas. The map is the maintained verification source; a proof that drives one convenient entry point is incomplete when the map lists others.

## It's working if

- Every section is grounded in observed repo facts; no placeholders survived.
- The trial run captured evidence that outlived cleanup.
- The map covers the top features, not just the one that was driven.

## Where it fits

`create-verification-skill` is a one-per-repo generator: run it once, then keep the result honest with [maintain-verification-skill](https://aihero.dev/skills-maintain-verification-skill). Downstream, every build that touches user-facing behavior proves itself through the skill it generated.
