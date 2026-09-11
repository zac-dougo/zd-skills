---
name: block-issues
description: Create one GitHub issue per Spec Kit tasks.md block.
disable-model-invocation: true
---

# Block Issues

Call the Skill tool with `creating-block-issues`, passing the arguments through. Two modes:

**All-blocks (default):** one issue per Block heading in `tasks.md`. Arguments:

- **Empty** → use the active Spec Kit feature.
- **`<feature-dir>`** (e.g. `001-uptime-settlement`) → override active-feature resolution.
- **`--dry-run`** → parse `tasks.md` and render the would-be issue bodies without calling `gh`.
- **`--label <name>`** → override the default dispatch label name.
- **`--no-label`** → create issues bare (no dispatch label attached).

**Subset (single issue, custom scope):** triggered by `--tasks`. Required args:

- **`--tasks <ids>`** → comma list with range support (`T008,T025-T027,T048`), validated against `tasks.md`.
- **`--title <text>`** → issue title.

Optional: `--notes <text>`, plus the same `--dry-run` / `--label` / `--no-label` flags.

The skill attaches a dispatch label to every issue it creates and auto-writes Blocked-by relations from the `tasks.md` dependency graph. Additional project-specific labels are not applied here; add them after with `gh issue edit`.

Echo the resolved `<owner>/<repo>` back before any state-changing `gh` call. Never create issues in a repo whose `origin` URL was not just echoed.

Counterpart: the `block-implement` skill implements one Block end to end from the issues this skill creates.
