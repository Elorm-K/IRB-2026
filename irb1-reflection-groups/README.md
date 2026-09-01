# IRB #1 — Reflection Groups Outside of Classes

**Submitted 2026-08-01. Reviewed and returned with changes. v5 response drafted 2026-08-28,
awaiting PI review.** Backlog item 1. Blocking recruitment for out-of-class groups.

> ## Start here for the current round
>
> | Path | What |
> |---|---|
> | [reports/IRB1_v5_ORA_RESPONSE_REPORT.md](reports/IRB1_v5_ORA_RESPONSE_REPORT.md) | Point-by-point response to the board, the deletions list, the four verification passes, and 5 open PI items |
> | `CURRENT/IRB1_Protocol_v5_ORA_RESPONSE.docx` | **The file to submit** |
> | `CURRENT/IRB1_Protocol_v5_ORA_RESPONSE_MARKED.docx` | Same document, everything new or rewritten in bold red — review this one |
> | `source/protocol_v5_ORA_RESPONSE.md` | **Edit here**, then rebuild with `python3 tools/build_docx.py` |
> | `archive/IRB1_Submitted_2026-08-01_BASE.pdf` | What was actually submitted, and what v5 was written against |
>
> **The structural change this round.** The board ruled that the reflection groups, being a
> service offered regardless of the research, are **not research and are not reviewed**. The
> application is now organized into five parts — research use of reflection-group materials
> (opt-out), member surveys, member interviews, comparison surveys, comparison interviews —
> each with its own recruitment text and its own consent form. Two terms are used throughout
> and must stay distinct in any edit: **members** hold reflection-group status, **participants**
> hold a research role. "Opt in" and "opt out" refer to research participation only, never to
> group membership.

> ## ⚠ Superseded, kept for lineage: the `.docx` candidates are not the live version (noted 2026-08-04)
>
> *Everything in this box is now two versions behind — it describes the gap between the
> repo's `protocol-candidates/` and what Greg submitted on 2026-08-01. That submitted version
> is now in `archive/IRB1_Submitted_2026-08-01_BASE.pdf`, and v5 supersedes it. Read on only
> for lineage.*
>
> Editing continued in a **Google Doc**, and the final IRB #1 differs from
> `CURRENT/protocol-candidates/IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx`.
> Diff anything against the Google Doc, not against these files. What changed in the final version:
>
> - **Research questions 1 and 2** broadened from "reflection groups" to "reflection **activities**,
>   such as reflection groups"; the same broadening in Methods item 2, §5, and Appendix G.
> - **§3 Personnel** — every person now carries a years figure: Cyril **~1 year**, Troy **~2 years**
>   (the repo copy has no Experience line for Cyril at all).
> - **§4 Participant Population** — the 60–100 / ~200 arm-by-arm forecasts are replaced by one
>   ceiling: *"over 5 years we may have up to 1,000 participants."* Methods item 11 keeps the
>   forecasts as the basis. The high-school-visitors sentence is deleted.
> - **Over-specification deleted**: "which uses only the same intake information" (matching tool),
>   "as peer members (not mentors)" (professionals), and the sentence about the consent form
>   indicating whether service data may be analyzed.
> - **Matching** loosened to "based on shared **affinity and other characteristics such as** shared
>   gender, shared disability status, and overlapping availability."
> - **Survey consent** simplified: the form sits at the beginning of the **first** survey and covers
>   consent for the study; the mechanic is dropped from Methods item 9 and stated only in §5.
> - **Appendix A** bullets reordered chronologically; the intake survey folded into the first bullet.
> - Appendix E email templates use `<insert link>` placeholders.
>
> **Three defects to fix in the Google Doc**, found while diffing: `professionals..` (double period,
> Methods item 7); `and Provide your availability` (capital *P* mid-sentence, Appendix A); and
> `comparisons group` → "comparison groups" (§4). Also note that `<insert link>` placeholders are
> silently stripped if markdown is ever re-uploaded to Google Docs — verify them after any upload.
>
> These decisions were ported into IRB #2 on 2026-08-04; see the addendum in
> [../irb2-instructor-collaboration/reports/IRB2_v5_VERIFICATION_REPORT.md](../irb2-instructor-collaboration/reports/IRB2_v5_VERIFICATION_REPORT.md)
> for which were taken, which were deliberately not, and why.

Covers reflection and collaboration activities with **no course involvement at all**:
ongoing groups for current students (outside their coursework), recent graduates and alumni,
working professionals as peers, community members; the matching and behaviour-change tools;
and comparative evaluation including professional comparison samples.

The framing that makes it work: the reflection groups are offered **as a service that would
run regardless of the research**. This protocol governs research *use* of the data that
service generates, plus research-specific activities (surveys, interviews, comparison
groups). Members can take part in a group while declining research use of their data. Keep
that separation intact in any edit — it is also what keeps course, enrollment, and grading
language out of this protocol entirely.

## What's here

| Path | What |
|---|---|
| [IRB1_SUMMARY.md](IRB1_SUMMARY.md) | **The blocker list**: 12 open PI decisions, plus what the draft assumes. Read first |
| [CURRENT/protocol-candidates/](CURRENT/protocol-candidates/) | Three files each claiming to be the final protocol — see [WHICH-IS-LIVE.md](CURRENT/protocol-candidates/WHICH-IS-LIVE.md) |
| [source/](source/) | The v5 markdown, and `source/media/` holding the five Appendix C instrument images |
| [reports/](reports/) | The v5 response and verification report |
| [archive/](archive/) | v1–v3, the tracked-changes views, the pre-split original draft, the 2026-08-01 submission, and the two retired standalone files |

**IRB #1 now has a `source/` directory, as IRB #2 does.** From v5 on, edit
`source/protocol_v5_ORA_RESPONSE.md` and regenerate:

```
python3 tools/build_docx.py irb1-reflection-groups/source/protocol_v5_ORA_RESPONSE.md \
    irb1-reflection-groups/CURRENT/IRB1_Protocol_v5_ORA_RESPONSE_MARKED.docx
```

The clean submission file is built the same way from `..._CLEAN.md`, which is generated by
stripping the `{{…}}` marks. Editing the `.docx` directly reintroduces exactly the drift that
retired the two standalone files.

`IRB1_ConsentForm_Participation.docx` and `IRB1_RecruitmentTexts.docx` moved to `archive/` on
2026-08-28: both dated from 2026-07-23 and now contradict v5 outright — the participation
consent form is replaced by an opt-out form, and the group recruitment texts describe
recruitment the board does not review.

## Two things to settle beyond the summary's 12

*(The v5 report's open-items list supersedes these for the current round.)*

- **Which protocol file is live** (see WHICH-IS-LIVE.md). Evidence is clear; it needs a
  human's yes.
- **Compensation consistency with IRB #2.** IRB #1 §9 pays $25 for interviews; an earlier
  IRB #2 draft paid $10 while claiming to match it. v4 of IRB #2 now uses $25, so IRB #1
  needs no change — but confirm before both go to the board, since a mismatch between two
  simultaneously-submitted protocols is exactly what a reviewer will catch.
