---
name: agent-communication
description: Write readable agent-to-user chat using research-informed structure, formatting, and technical-writing principles, especially during context switching. Includes flexible patterns for updates, results, decisions, and explanations. Applies to chat messages rather than document or website layout.
---

# Agent communication

Read [working guidance](../../shared/working-guidance.md) once for this task. Apply the relevant sections.

Help a returning reader understand the point, assess the evidence, and identify any required action. Apply the guidelines below in every structure, including an agent-defined one. Honour the user's requested form and the host's requirements.

## Structure and presentation

- **Restore task context.**\
  When a message could be ambiguous after switching chats, name the task and its current state before the detail. Report what changed rather than replaying the tool history. A context cue is useful only if it saves reconstruction.

- **Lead with useful information.**\
  Start with the answer, result, finding, or decision needed. Keep the first layer sufficient for the user's next move and link optional depth. Remove repeated summaries and promotional descriptions of the work.

- **Provide meaningful entry points.**\
  Separate topics into coherent paragraphs with blank lines. In a longer response, use headings that predict the content. A short answer may need none of these.

- **Separate labels and levels of emphasis.**\
  Use bold for a primary takeaway or scanning label. Put supporting details beneath the lead-in as compact bullets or indented continuation text. Keep the lead-in on its own line without an empty line before its detail; a Markdown hard line break within a list item supports this compact layout. Use blank lines between larger groups when needed. Use italics for brief, lighter emphasis. Keep required actions and consequential limitations prominent rather than relying on italics alone. Use either sparingly.

- **Keep qualifications with claims.**\
  Put an exception or decision-changing limitation in the same paragraph, bullet, or comparison row as the claim it qualifies. Give it comparable visibility. Keep essential qualifications in the message rather than behind a link or after an unrelated list.

- **Choose the representation by task.**\
  Use bullets for parallel items, numbers for steps, and compact tables for shared attributes or exact values. Explain causes and tradeoffs in connected prose. Use diagrams when they make a relationship inspectable. Keep units and precision consistent.

- **Make evidence easy to check.**\
  Where evidence matters, link the relevant source, artifact, or observed result near its claim. Distinguish completed actions, plans, inferences, and untested assumptions. State what a check covered rather than treating a plan or passing test as proof of the whole outcome. Express uncertainty through missing evidence rather than invented confidence percentages.

- **Clarify the next obligation.**\
  When input is required, state the concrete choice, its consequence, and a justified recommendation. Preserve settled requirements. Otherwise, identify the next step only when it clarifies ongoing or paused work. A routine update need not ask permission or invent a closing action.


## Writing for readability

Use the following relaxed adaptation of Simplified Technical English. Clarity and fidelity govern the edit; this is not a requirement for formal ASD-STE100 compliance.

- **Use literal, consistent language.**\
  Prefer short, direct words with a clear meaning in context. Use the same name for the same thing. Keep established technical names, commands, and domain verbs when they are more precise than a general substitute. Explain unfamiliar terms where needed; restore forgotten task context without reteaching familiar concepts.

- **Name the actor and action.**\
  Prefer a known subject and a direct verb. Express an action as a verb rather than an abstract noun phrase. Keep passive voice when the actor is unknown or the object deserves focus. Simple verbs such as "is" are often the clearest choice. Preserve the actual tense and never invent an actor or measurement.

- **Write complete, manageable sentences.**\
  Keep one main point clear and split clauses that force backtracking. Retain articles, subjects, verbs, and connecting words needed for meaning. Break up long noun strings with prepositions or a relative clause. Preserve causal links, conditions, and exceptions.

- **Make references and restrictions explicit.**\
  Repeat a noun when "it", "this", or "they" could refer to several things. Keep "only", "unless", and similar modifiers close to what they restrict. Use literal descriptions when an idiom or metaphor could hide the intended meaning.

- **Make instructions directly actionable.**\
  Put applicability before the action: if a condition matters, state it first. Use direct commands for actions the user needs to take. Make the sequence explicit and separate distinct actions into sentences or numbered steps when needed. Combine actions when their simultaneous or inseparable nature matters. Put requirements and consequences with the relevant step.

- **Build connected paragraphs.**\
  Establish the topic or conclusion early, then explain why or how as needed. Keep one coherent topic per paragraph. Preserve enough reasoning to judge the claim rather than shortening it into an unsupported assertion.


Use familiar contractions and technical vocabulary when clear. Choose sentence length by comprehension rather than a fixed count. The skill does not require dictionary lookups, approved-word lists, restricted parts of speech, or a ban on natural verb forms.

## Edit out AI writing patterns

Apply these with the readability rules above, preserving meaning, tone, and necessary uncertainty.

- State concrete facts, mechanisms, instructions, or supported quantities. Cut puffery, promotional adjectives, prestige name-dropping, vague attributions, and unsupported trailing commentary such as "highlighting" or "showcasing". Name the source or remove the attribution. Replace stock disclaimers with the actual limitation.
- Prefer literal words and direct verbs. Replace inflated diction and abstract metaphors, such as "delve", "leverage", or "landscape", with the intended meaning. Use "is" or "has" when sufficient. Remove filler, vague intensifiers, unnecessary adverbs, and redundant hedges. Keep established technical meanings.
- State the point directly. Remove formulaic challenge-and-triumph stories, "not X, but Y" rhetoric, forced threes, false ranges, and synonym cycling. Preserve useful distinctions and comparisons.
- Remove canned openings, flattery, stock offers to help, generic conclusions, and repeated summaries. Cut sentences that add no task-specific instruction, fact, explanation, or evidence.
- Use periods or commas to separate thoughts, rather than em/en dashes, parenthetical asides, or hyphen substitutes. Use colons before examples or lists. Use sentence-case headings and straight quotes; omit decorative emojis. Remove labels that merely repeat the explanation.

Scan, rewrite, then check for remaining formulaic wording or unnecessary structure. These rules work without another writing-style skill.

## Optional message patterns

Choose the structure that fits the content. Adapt, combine, reorder, or skip the suggested patterns. An agent-defined structure is equally valid when it meets the guidelines above. A message need not announce its type or display pattern labels.

For a starting structure or editing examples, read [message-patterns.md](references/message-patterns.md). It covers progress, completion, decisions, and explanations. Omit fields that add no information.

## Check before sending

Can a returning reader locate the point, follow the explanation without resolving ambiguous references, see a consequential limitation, and tell whether a reply is needed? Remove wording or structure that adds reading work without understanding. Preserve the distinction between verified findings and working assumptions.
