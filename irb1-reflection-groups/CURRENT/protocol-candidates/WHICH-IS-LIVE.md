# Which of these three is the live IRB #1 protocol?

Three files in the old project root all presented as the final IRB #1 protocol. None is
archived yet — that call is the PI's or Cyril's. Below is what the text actually shows.

## Recommendation

**`IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx`** — this is what
`.claude/skills/irb-writing/references/irb-backlog.md` already points at, and the content
confirms it is the newest lineage. Once confirmed, move the other two to `../../archive/`.

## The evidence

| File | Modified | Words | What the text shows |
|---|---|---|---|
| `IRB1_Protocol_ReflectionGroups_OutsideClasses_FINALCOPY.docx` | Jul 27, 17:40 | 7,159 | **Older state.** Numbered method items are broken — they run `2. 2. 2. 2. 3. 4.` with consent appearing twice (as item 2 and again as item 7). Only 4 data types (1.1–1.4) instead of 6. No optional data-linkage consent paragraph. Attributes enrollment figures to "the funded evaluation plan" and gives the comparison group as ~100 professionals |
| `FINAL IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx` | Jul 27, 18:52 | 6,741 | Same document as the one below, plus two extra references |
| `IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx` | Jul 27, 18:56 | 6,693 | **Newest lineage.** Method items renumbered cleanly 1–12, consent stated once; data types expanded to 1.1–1.6 (adds reflection-group materials and co-design session notes); optional cross-study data-linkage consent paragraph added; enrollment figures no longer falsely attributed to the grant; comparison group ~200; survey consent split into its own form ("CONSENT FORM (Surveys)"); Appendix B retitled "Intake / initiation survey" |

**`FINALCOPY` is an ancestor of `FINAL_structured`, not a rival version.** The renumbering,
the two added data types, and the removed false attribution all run one direction.

## The `FINAL `-prefixed duplicate

It differs from `IRB1_..._FINAL_structured.docx` by **exactly two lines** — two references
in the bibliography:

- Aron, A., Melinat, E., Aron, E. N., Vallone, R. D., & Bator, R. J. (1997). *The experimental generation of interpersonal closeness.* Personality and Social Psychology Bulletin, 23(4), 363–377.
- Flanagan, J. C. (1954). *The critical incident technique.* Psychological Bulletin, 51(4), 327–358.

**Neither is cited anywhere in the body of either file** — verified by searching both for
the author names and for "critical incident" / "interpersonal closeness". So the shorter
file most likely had two uncited references cleaned out, and nothing of substance is lost
by preferring it. If either work is meant to support the icebreaker procedure (Aron) or the
interview method (Flanagan), the fix is to cite it in the body, not to switch files.

This file was a hardlink to a copy in `~/Downloads`, which explains the byte-size
discrepancy that
[../../../irb2-instructor-collaboration/reports/IRB2_GapAnalysis_vs_CAREER_grant.md](../../../irb2-instructor-collaboration/reports/IRB2_GapAnalysis_vs_CAREER_grant.md)
flagged and could not resolve (673,241 vs 672,640 bytes). The hardlink is broken now that
the file has been moved into the repo; edits here no longer touch the Downloads copy.

## Also in this folder's sibling

`../IRB1_ConsentForm_Participation.docx` and `../IRB1_RecruitmentTexts.docx` date from
2026-07-23, **before** all three protocol candidates. If the protocol's consent appendices
changed after that date — and `FINAL_structured` did split the survey consent into its own
form — these standalone files may have drifted. Worth a consistency check against whichever
protocol file is confirmed live.
