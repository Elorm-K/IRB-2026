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
| Review the draft that's furthest along | [irb2-instructor-collaboration/](irb2-instructor-collaboration/) — start with its v7 reconciliation report |
| Check a draft against the reviewing board's own published rules | [.claude/skills/irb-writing/references/compliance-check.md](.claude/skills/irb-writing/references/compliance-check.md), with rules per institution in [references/institutions/](.claude/skills/irb-writing/references/institutions/) |
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

irb2-instructor-collaboration/   IRB #2 — instructors AND students in collaborating courses
  CURRENT/                         Live v7 merged submission + cover page
  source/p2/                       Markdown v7 is generated from — EDIT HERE
  reports/                         Verification reports, markup, gap analysis, drafting prompt
  archive/                         Superseded versions, incl. all of v4

irb2b-student-stream-held/       Closed. Its README explains why the split was reversed.
course-protocol-mod/             Data-linkage modification to the approved course protocol
tools/                           build_docx.py, docx_text.py — generate and diff submissions
.claude/skills/irb-writing/      The workflow, board rules, backlog, knowledge base,
                                 compliance pass, and per-institution rule files
```

Two rules that aren't obvious from the tree:

- **For IRB #2, edit `source/p2/*.md`, not the `.docx`.** The submission `.docx` is generated
  from those parts with `python3 tools/build_docx.py <merged.md> <out.docx>`. Editing a `.docx` directly reintroduces the drift that made the v1
  standalone consent file stale — it still carried the old protocol title and a live decision
  marker. (`source/*.md` at the top level are v4's parts, kept for lineage.)
- **`archive/` is superseded work, kept for lineage.** Never submit from it. Each archive
  folder has a README explaining what superseded what.

## Status, 2026-08-06

| Protocol | State | Blocked on |
|---|---|---|
| **#1** Reflection groups outside classes | Drafted, not submitted | 12 PI decisions in [IRB1_SUMMARY.md](irb1-reflection-groups/IRB1_SUMMARY.md); plus **which of three candidate files is live** (see below) |
| **#2** Instructor collaboration | **v8 "mid-final" drafted** — Cyril's Google Doc repaired: appendices relettered A–J, 20 broken cross-references fixed, wrong consent form replaced; changes marked in red | PI review. Open items in the [v8 report](irb2-instructor-collaboration/reports/IRB2_v8_MIDFINAL_REPORT.md); strip the red before submitting. **v7 and v8 are separate lineages** — pick one |
| **#2b** Student stream | **Closed** — merged back into #2 | — |
| **Course-protocol mod** (data linkage) | Drafted, not submitted | — |
| **#3–#6, #8** | Not drafted | See the backlog. **#8** (video-assisted GenAI reflection assignment) is the largest confirmed hole |

## Two open items worth knowing about immediately

**1. The grant's assumption that existing approvals cover Task 2 does not hold.**
`inputs/approved-protocols/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` ("Learning with
Generative AI in introductory college courses") was unreadable while IRB #2 v4 was written
and has since been read in full. Two results, opposite in sign:

- *Good:* its January 2026 consent forms are the program's newest board-approved templates,
  and IRB #2's consent forms are now rebuilt from them rather than derived from the grant.
  That closed what the v4 report called the largest unverified item in the draft.
- *Bad:* it does **not** cover the video-assisted GenAI reflection assignment — zero
  occurrences of "replay" or "anonymiz", and screen recordings appear only *during
  interviews*, not as an assignment. The grant asserts at §3, p.6 that *"all preliminary work
  already has IRB approval … it also already covers the proposed work in Task 1 and 2."*
  For that assignment it doesn't. It's now backlog item **8**, it is the largest remaining
  hole, and the grant deploys it in a collaborator's courses that the team's own course
  protocol does not reach.

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
