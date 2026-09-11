---
"mattpocock-skills": patch
---

Add four user-invoked skills adapted from the pstack plugin by Lauren Tan (MIT): `how`, `why`, `create-verification-skill`, and `maintain-verification-skill`. The requested pstack `reflect` was resolved without adding: this repo's `productivity/reflect` is already an adapted superset of it (same three-reviewer pipeline and synthesizer, plus richer triggers, harness-neutral transcripts and models, and a structure-preference pass), confirmed with the repo owner.

- De-cursor-fied for any harness: Cursor MCP discovery reads as harness integrations, `Task`/`subagent_type`/`readonly` params read as generic subagent calls with inline fallbacks, model-panel pins (grok/fable/opus/sol) read as the strongest model the harness offers, `.cursor/skills/` output paths read as the target repo's project skill directory, and MCP wording is integrations throughout.
- `how` critique mode references two prompt files missing from the source snapshot, so the rubric ships inline in SKILL.md instead.
- The plugin now ships 43 skills. Each new skill has a bucket README entry, a top-level README entry, and a docs page.
