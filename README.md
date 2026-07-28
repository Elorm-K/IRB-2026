# IRB Writing — YES Lab

Human-subjects protocols for the reflection-groups and generative-AI research program
(NSF CAREER Award 2544192, PI Dr. Gregory L. Nelson, University of Maine).

**Getting a protocol submitted is the critical path for recruiting** — a protocol sitting
in draft costs a semester of data. Everything here is organized around that.

---

## Start here

| If you want to… | Read |
|---|---|
| Know what still needs writing and what it's blocking | [.claude/skills/irb-writing/references/irb-backlog.md](.claude/skills/irb-writing/references/irb-backlog.md) — the single source of truth for status |
| Understand *how* the lab writes IRBs (the workflow, the board's rules) | [.claude/skills/irb-writing/SKILL.md](.claude/skills/irb-writing/SKILL.md) |
| Review the draft that's furthest along | [irb2-instructor-collaboration/](irb2-instructor-collaboration/) — start with its verification report |
| See what the board has already approved, and copy from it | [inputs/approved-protocols/](inputs/approved-protocols/) |
| Know what this study committed to doing | [inputs/grant/](inputs/grant/) |

## Layout

```
inputs/                          Sources the drafts derive FROM. Read-only.
  grant/                           The governing document: NSF CAREER proposal
  approved-protocols/              Board-APPROVED protocols — the language to reuse
  meetings/                        Advisor meeting transcripts (PI instructions)
  literature/                      Background paper

irb1-reflection-groups/          IRB #1 — reflection groups outside of any course
  CURRENT/                         Live drafts
  archive/                         Superseded versions
  IRB1_SUMMARY.md                  12 open PI decisions — blocks submission

irb2-instructor-collaboration/   IRB #2 — instructor co-design workshops, surveys, interviews
  CURRENT/                         Live v4 drafts (the .docx you'd submit)
  source/                          Markdown the .docx are generated from — EDIT HERE
  reports/                         Verification, markup, gap analysis, drafting prompt
  archive/                         Superseded versions

irb2b-student-stream-held/       IRB #2's student/classroom half. Deliberately NOT submitted yet.
course-protocol-mod/             Data-linkage modification to the approved course protocol
.claude/skills/irb-writing/      The workflow, board rules, backlog, and knowledge base
```

Two rules that aren't obvious from the tree:

- **For IRB #2, edit `source/*.md`, not the `.docx`.** The consent-form and recruitment
  `.docx` are generated from the same source parts as the protocol appendices, and were
  verified byte-identical. Editing a `.docx` directly reintroduces the drift that made the
  v1 standalone consent file stale (it still carried the old protocol title and a live
  decision marker).
- **`archive/` is superseded work, kept for lineage.** Never submit from it. Each archive
  folder has a README explaining what superseded what.

## Status, 2026-07-28

| Protocol | State | Blocked on |
|---|---|---|
| **#1** Reflection groups outside classes | Drafted, not submitted | 12 PI decisions in [IRB1_SUMMARY.md](irb1-reflection-groups/IRB1_SUMMARY.md); plus **which of three candidate files is live** (see below) |
| **#2** Instructor collaboration | v4 drafted, staged narrow to instructor-facing research only | PI review. 4 inputs listed at the end of the [verification report](irb2-instructor-collaboration/reports/IRB2_v4_VERIFICATION_REPORT.md) |
| **#2b** Student stream | Drafted, submission-ready, **held** | Submit after #2 clears and the first co-design cycle fixes the design |
| **Course-protocol mod** (data linkage) | Drafted, not submitted | — |
| **#3–#6** | Not drafted | See the backlog |

## Two open items worth knowing about immediately

**1. Approved AI consent language became available and hasn't been used yet.**
`inputs/approved-protocols/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` was unreadable when
IRB #2 v4 was written (it sat in `~/Downloads`, which tools can't access), so v4's
generative-AI wording was *derived from the grant rather than copied from the approved
form* — the verification report calls this "the largest unverified item in the draft."
That file is now in the repo. It is the AI protocol (298 mentions of generative AI) and
carries three board-approved consent forms as of its Jan-2026 mod: Appendix **P**
(participation without interviews), **Q** (bi-weekly interview), **R** (follow-up
interview). Replacing v4's derived AI passages with this approved language is the highest-value
revision available. Separately, whether that protocol's *scope* reaches the grant's
Task 1/2 work is still unread, and the grant leans on it heavily — see the backlog's
"Verify, do not assume".

**2. Three files claim to be the final IRB #1 protocol.**
They're in [irb1-reflection-groups/CURRENT/protocol-candidates/](irb1-reflection-groups/CURRENT/protocol-candidates/)
with the diff written up in
[WHICH-IS-LIVE.md](irb1-reflection-groups/CURRENT/protocol-candidates/WHICH-IS-LIVE.md).
Evidence points clearly at one of them; it needs a human's confirmation, then the other two
move to `archive/`.

## Before pushing this to GitHub

**Use a private repository.** This project contains, in participant- and
personnel-identifying form:

- approved protocols with researcher names, email addresses, and course rosters by number
- consent forms with named contacts and compensation terms
- four transcripts of internal advisor meetings, which discuss unpublished study design
  and personnel candidly

None of it is participant data, but none of it is meant to be public either. Protocols
under review are also ordinarily not published.

`.gitignore` already excludes `.DS_Store`, Office lock files, and
`.claude/settings.local.json`. The shared skill (`.claude/skills/irb-writing/`) and
`.claude/settings.json` are intentionally tracked — the skill is the lab's reusable
workflow and belongs in the shared lab skills repository, per its own closing note.

## History

The commit before the reorganization is a faithful snapshot of the project as it stood on
2026-07-28, so any file's original location is recoverable with `git log --follow <path>`.
