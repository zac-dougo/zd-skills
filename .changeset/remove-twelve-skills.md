---
"mattpocock-skills": patch
---

Remove twelve skills and retire two buckets: `ask-zac`, `triage`, `setup-matt-pocock-skills`, `implement`, `wayfinder`, `arena`, `swarm`, `tdd`, `version-control`, `to-questionnaire`, `teach`, and `study-course` are deleted, along with their docs pages. The `teaching/`, `in-progress/`, and `deprecated/` buckets are gone: the plugin now ships 24 skills (15 engineering, 9 productivity) plus 4 utility skills in `misc/`.

- The main flow is now `grill-with-docs → to-spec → to-tickets → build → code-review`, with no setup step and no router.
- `to-spec`, `to-tickets`, `code-review`, `blast-radius`, and `copse` no longer point at the setup skill; they ask for the repo's tracker configuration instead. The `ready-for-agent` label keeps its name without the triage vocabulary.
- Every surviving docs page is re-synced: neighbours that no longer exist are removed from the routing tables and "Where it fits" sections, and the router footers are gone.
- `CONTEXT.md` drops the wayfinder and triage domain terms, and `.agents/install-block.md` no longer names the setup skill in the skills.sh whole-set form.
