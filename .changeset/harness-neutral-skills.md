---
"mattpocock-skills": patch
---

Make the promoted skills harness-neutral instead of Claude- and Codex-specific.

- Every skill that fans work out to subagents or background agents (`research`, `code-review`, `grilling`, `improve-codebase-architecture`, `codebase-design` / `DESIGN-IT-TWICE.md`, `reflect`, `automate-me`) now carries an inline fallback: run the steps sequentially in-session when the harness has no subagents.
- Transcript lookup (`reflect`, `automate-me`, `show-me-your-work`) now starts from the harness's own transcript location instead of assuming a system-prompt-named `agent-transcripts/` directory, with a digest-or-conversation fallback when the harness exposes no transcript files.
- `reflect` no longer names vendor model codenames: reviewer tables point at the configured judgment/tooling models or the strongest reasoning model the harness offers.
- `reflect` reviewers and `automate-me` say integrations instead of MCP throughout.
- `automate-me` skill-directory paths are framed as the harness's skill directories, with `.agents/skills/` kept as the Agent-Skills-standard example.
- Bucket `README.md`s and `.agents/invocation.md` note that harnesses beyond Claude Code and Codex use their own equivalent of the user-invoked metadata.
