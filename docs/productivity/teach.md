## What it does

`teach` turns a learning goal into a tailored course, with lessons and checks for understanding. It separates what you say you know from what you demonstrate: **Ask** records your reported education and background in `NOTES.md`, while **Quiz** tests your knowledge, with quiz evidence carrying more weight when the course is placed in your zone of proximal development (ZPD).

The course is grounded in the workspace's mission and resources, not just a topic label. Reported background helps choose a starting point, but it does not stand in for demonstrated mastery.

## When to reach for it

You invoke this by typing `/teach`, and the agent won't reach for it on its own. Reach for it when you want to learn a topic through a course shaped around your goal and current understanding, rather than a generic explanation or one-off answer.

## Prerequisites

`teach` creates a learning workspace with a `MISSION.md`, `RESOURCES.md`, `NOTES.md`, lesson HTML, and learning records. Use a workspace where those course files can persist across sessions.

## Ask and Quiz are different evidence

Ask captures self-reported background, such as education and prior experience. Quiz checks what you can currently explain or apply. A confident self-assessment can guide the conversation, but demonstrated knowledge is stronger evidence for choosing what to teach next.

## Common questions

**Why ask me about my background if there is a quiz?**

Your reported history provides useful context, but it can be incomplete or overestimate familiarity. The quiz checks the knowledge itself, so the course can target gaps instead of assuming that a job title or course history proves mastery.

**Is the quiz just a final test?**

No. It helps establish what you already understand so lessons can start at an appropriate level. Later learning records capture demonstrated mastery as you work through the course.

## It's working if

- The first lessons feel neither like a repeat of what you already know nor a jump over missing fundamentals.
- The lesson focus reflects your answers to knowledge checks, not only the background you reported.
- You can see your stated background in `NOTES.md` and demonstrated progress in the learning records.

## Where it fits

`teach` is a standalone learning workflow, not a step in the engineering planning chain. Reach for it to build and work through a course; use [ask-zac](https://aihero.dev/skills-ask-zac) to find the right skill when you are unsure which workflow fits.
