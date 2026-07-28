# Inputs — what the drafts are derived from

Treat everything here as **read-only source material**. Nothing in this folder is a draft,
and nothing in it should be edited to match a draft.

## `grant/`

`FINAL NSF_CAREER_25_Nelson.pdf` — NSF CAREER Award 2544192. **The governing document.**
Every substantive claim in a protocol has to trace to this, to a prior approved protocol, or
to an explicit PI instruction. Confirmed authoritative by the PI and by the 2026-07-22
advisor meeting: *"just basically everything that's in the grant already. You don't have to
figure it out. It's already all planned."*

Its activity table — every planned human-subjects activity as a row, with which protocol
covers it — is maintained at
[../.claude/skills/irb-writing/references/irb-knowledge-base.md](../.claude/skills/irb-writing/references/irb-knowledge-base.md) §2.
That table, not the PDF, is what coverage checks run against.

## `approved-protocols/`

Board-**approved** protocols. These are the highest-weight input to any new draft: the board
has already said what it accepts in this exact program, and that is not knowledge a model
has. Copy from these rather than writing fresh; divergence in format from approved language
is a signal the approved version wasn't used.

| File | Covers | Copy from it |
|---|---|---|
| `2024_08_09 Nelson_MOD_2_Jan_2026_FINAL.pdf` | The team's own courses; reflection-group assignments; pre/post + 8 longitudinal surveys | Consent skeleton (**Appendix P** is the most recent), Section 6 data-management framing, Section 9 compensation, recruitment script |
| `2024_08_09 Nelson_MOD_Sept_2025_FINAL.pdf` | Same protocol, earlier mod: adds Fall-25 courses and $10/longitudinal-survey compensation | Career-event survey items (Appendices K, L) |
| `2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` | **A different protocol** — generative-AI integration in coursework, by named course cohort. Weekly reflections, weekly and follow-up qualitative interviews | **The approved AI consent language**: Appendices **P**, **Q**, **R** MOD Jan/26 (participation-without-interviews, bi-weekly interview, follow-up interview). Also weekly reflection questions, interview guides, AI recruitment script |

The third file was unreadable when IRB #2 v4 was drafted, so v4's AI wording was derived from
the grant instead of copied from the approved form — see the root
[README](../README.md#two-open-items-worth-knowing-about-immediately). It's readable now.

Finding the newest version of a consent form in these documents: appendices accumulate
chronologically, so search the term from the top and jump to the **last** match.

## `meetings/`

Four transcripts of the 2026-07-22 advisor meeting (overlapping recordings of the same
session, at different lengths). PI instructions here count as a governing source — several
figures in the drafts, like the instructor recruitment funnel, come from this meeting and
**not** from the grant. That distinction matters: an earlier draft attributed those numbers
to the grant, and the audit caught it.

Internal and candid. See the note on repository visibility in the root README.

## `literature/`

`Reflection Groups for Learning Professional Skills.pdf` — background on the intervention
itself. Not a governing document; useful for the evidence-base paragraph that opens a
protocol narrative.
