## What it does

`research` answers a question against primary sources and returns findings with citations. It distinguishes established facts, interpretation, and unavailable evidence.

A saved document is required only when the user requests one or an established workflow needs a durable artifact. A focused lookup can end with a cited answer in the conversation.

## When to reach for it

Type `/research`, or the agent reaches for it automatically when a task calls for research. Use it to check documentation, API behavior, specifications, or other facts a decision depends on.

| What you need | Reach for |
| --- | --- |
| Facts supported by sources | `research` |
| A decision explored with you | [grilling](https://aihero.dev/skills-grilling) |
| Project terminology and consequential decisions to record | [domain-modeling](https://aihero.dev/skills-domain-modeling) |
| An experiment with an approach | [prototype](https://aihero.dev/skills-prototype) |

## Delegation and output

Independent searches and source checks can run in parallel when that improves the expected result or completion time. Shared working guidance prefers an available Luna model for bounded fact gathering, with stronger models for questions that need them. A delegated researcher completes its brief directly unless further delegation is explicitly requested.

When a document is needed, it uses the requested location or the project's existing convention. Research does not automatically start implementation or publish findings elsewhere.

## Common questions

**Does every lookup create a file?**

No. A cited answer is sufficient unless a document is requested or required by the workflow.

**Can the research agent keep spawning more researchers?**

Only when the coordinator explicitly requests further delegation. The default is for each delegated researcher to complete its assigned work directly.

**How do I check the answer?**

Follow the citations beside material claims. The source must support the claim for the relevant version and circumstances. Missing evidence remains visible as a limitation.

## It's working if

- The answer addresses the question and links its material claims to supporting sources.
- Versions and dates are checked when they affect the conclusion.
- Independent reading progresses in parallel when useful, without repeated delegation of the same task.
- A file appears only when a durable artifact is needed.

## Where it fits

`research` supplies evidence for [designing-architecture](https://aihero.dev/skills-designing-architecture), [grilling](https://aihero.dev/skills-grilling), and [to-spec](https://aihero.dev/skills-to-spec). It can also answer a standalone factual question.
