# Optional message patterns

Use these as starting styles. Choose, adapt, combine, or ignore them according to the message. The guidelines in SKILL.md govern every choice. The examples are fictional and demonstrate presentation only.

## Progress

Useful when work continues and a new finding changes what the user knows. A possible shape is finding, implication, then the next unresolved check. Include task context when needed. A milestone can be one sentence.

> The export bug comes from empty date cells. The fix handles those cells; I'm checking mixed date formats next.

There is no need to repeat the original plan or append a request to continue. A delay update can instead explain the obstacle and what the agent is doing about it.

## Completion

Useful when an outcome or a reviewable artifact is ready. A possible shape is outcome, relevant verification and its limits, then an artifact or a real remaining action. Use a paragraph for a small change and grouped detail for a larger one.

> The CSV date fix is ready for review. Tests pass for empty cells and mixed date formats. Opening the export in Excel remains unverified.

Link the actual change or sample when available. Choose language that reflects the scope completed. If a required check remains, say what is ready and what remains.

## Decision

Useful when user input materially affects the next action. A possible shape is the decision needed, the recommendation, and the tradeoff or fact that could change it. Provide enough context to answer without rereading the chat. Use a table only if comparable attributes help the choice.

> Does the search prototype need shared live updates at launch? The local index meets the offline requirement. The hosted service provides shared live updates but needs a network. If both are required, neither option as described is sufficient, so we need another approach.

If the user already authorised the choice, make the routine implementation decision and report it as appropriate. A decision pattern does not itself create an approval gate.

## Explanation or research

Useful when the user wants understanding or a supported recommendation. A possible shape is answer, reasoning or evidence, then the limit that affects its application. Use headings for distinct topics when the answer is long enough to need navigation. Simple questions can receive simple answers.

> Use a table when the reader needs to compare the same attributes across options. Use connected prose to explain why an option fits. A table with paragraphs in most cells is a reason to reconsider the structure.

For research, cite relevant sources and distinguish demonstrated findings from proposed applications. Keep essential qualifications with their claims.

## Mixed or other messages

A progress update can contain a decision; an explanation can be a single analogy, a diagram, a question, or an example. Use one coherent response rather than concatenating several complete patterns. Follow a requested format such as a JSON object, checklist, or concise answer while preserving the shared guidelines.

Treat useful omissions as good judgment. A routine factual answer may need no heading, list, evidence link, or closing action.

## Editing for readability

These examples use invented facts. Preserve the supplied meaning when applying the same edits to real work.

### Keep lead-ins and supporting detail compact

- **Research-informed presentation**\
  Choose *prose, lists, or tables* to fit the reading task. Keep consequential limitations beside the relevant claim.

The lead-in ends with a Markdown hard line break, written as a backslash before the newline. The explanation continues immediately beneath it, indented within the same item. Supporting bullets are another option when the content has several parallel details. Avoid an empty line between a label and its detail. Italics provide lighter emphasis inside prose. A short answer can omit labels entirely.

### Concrete subject, cause, and limitation

Before:

> There is an issue with the processing of dates that has resulted in the occurrence of failed exports, and a modification has been made that should resolve it, although further verification is required.

After, when the facts establish the parser as the cause:

> The parser rejects empty dates, causing exports to fail. I changed the parser to accept empty dates. The change still needs verification.

The revision names the mechanism and preserves the unverified state. It does not upgrade "changed" to "fixed".

### Condition before instruction

Before:

> Refresh the preview index if you changed the sample data; production uses a separate process.

After:

> If you changed the sample data, refresh the preview index. Production uses a separate process.

The condition remains attached to its instruction. A result-first opening elsewhere in the message does not require putting actions before their conditions.

### Clear reference without inventing facts

Before:

> The worker starts the indexer. It stores the records.

If the supplied facts establish that the indexer stores records:

> The worker starts the indexer. The indexer stores the records.

If the referent is unknown and affects the answer, resolve the uncertainty rather than guessing to produce a cleaner sentence.

### Concision with necessary uncertainty

> The logs suggest that the cache causes the stale results. I haven't reproduced the failure yet.

This already communicates useful uncertainty. A style edit should preserve the distinction between a hypothesis and a demonstrated cause.
