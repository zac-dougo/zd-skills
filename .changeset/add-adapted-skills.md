---
"mattpocock-skills": patch
---

Add fifteen adapted third-party skills (MIT): six user-invoked wrappers (`review`, `commit`, `tdd`, `block-issues`, `design`, `block-implement`) and nine model-invoked skills (`running-tdd-cycles`, `reviewing-changes`, `designing-architecture`, `creating-block-issues`, `committing-changes`, `implementing-blocks`, `shell-discipline`, `engineering-philosophy`, `ponytail`). Fourteen come from swell-agents/coding-skills, `ponytail` from DietrichGebert/ponytail; sources are credited in the README.

- Vendored with their reference, script, and template assets, minus the upstream Claude-Code-only pieces: `allowed-tools` / `argument-hint` / `alwaysApply` frontmatter, the `agents/` subagent shims, and the verbatim Claude-Code archival references.
- De-claudeified for any harness: subagent/background steps carry inline fallbacks, transcript lookup starts from the harness's own location, model references are vendor-neutral, MCP wording is integrations, and cross-skill links follow this repo's Skill-tool convention.
- The plugin now ships 39 skills. Each new skill has a bucket README entry, a top-level README entry, and a docs page.
