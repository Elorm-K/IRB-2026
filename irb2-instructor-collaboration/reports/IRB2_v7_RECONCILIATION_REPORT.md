# IRB #2 v7 — reconciliation of Cyril's Google Doc with the merged consent forms

**2026-08-06.** v7 takes **your Google Doc ("IRB 2", modified 2026-08-06) as the base text**, applies the
instructor consent-form merge from v6, reletters the appendices, and restores a short list of
board-required items your edit pass removed.

**Everything I changed is bold red in the `.docx`.** 67 marked spans, ~1,780 words. Delete any of them
and the document still reads correctly — that is the point of the marking.

Source of truth is now `source/p2/*.md` → `source/protocol_v7_MERGED.md` →
`CURRENT/IRB2_Protocol_v7_MERGED_SUBMISSION.docx`.

## What your Google Doc changed, and what I did with it

Your doc was v5-lineage (five consent forms, appendices A–P) with a substantial edit pass on top:
~2,300 words cut from the narrative and consent forms, instrument appendices untouched.

| Your edit | Kept? |
|---|---|
| Chris Dufour removed from Personnel | **Kept** — and completed: he was still in the Contact Information line of all five consent forms. Removed there too. |
| Student ceiling 2,000 → 1,000 | Kept |
| Vendors de-named in Methods prose ("online" for Zoom) | Kept in the narrative body |
| Reflection-group meeting structure added (the four-step meeting) | Kept, rendered as bullets — as numbered items 1–4 they collided with Methods items 1–15 |
| Third-party-application risk paragraph added to §7 | Kept |
| Benefits sections rewritten and broadened | Kept |
| `<course name>` / `<course number e.g. COS100>` placeholders | Kept — and verified they survived into the `.docx` |
| Student consent form rewritten toward the approved course-protocol wording | Kept |
| Narrative trimming (§2 cross-protocol paragraph, §4 vulnerable-populations, analysis plan, etc.) | Kept as cut |
| Concise Summaries deleted from Appendices A, B, C | **Restored** — see below |
| Tax-reporting language deleted from A, B, C | **Restored** |
| "CAREER:" dropped from the title | **Restored** |
| Vendors de-named in §6 Confidentiality | **Restored** |
| §9 worked totals and course-credit paragraph deleted | **Restored** |

## The five restorations, and why

Each is red in the document. The first four are rules with a citation; the fifth is judgment.

1. **"CAREER:" in the title** — `institutions/umaine.md` §2, hard gate: *"Title must match the grant
   title if funded."* The award title is *"CAREER: Developing Professional Skills…"*. Without the
   prefix the application can be returned unread. Restored in the document title, in §1's award
   title, and in all four consent-form titles.

2. **Tax-reporting language in Appendices A and B** — umaine.md §7: over **$75** cumulative triggers
   required HR / Purchasing / Form-1099 language, computed against the *maximum cumulative* payment
   one participant can receive. An instructor at $25/interview crosses it on the fourth interview; a
   student completing all eight follow-up surveys reaches **$80**. Your Appendices D and E kept this
   language, so removing it from the others also made the package internally inconsistent.

3. **Vendor names in §6 Confidentiality** — umaine.md §6: *"If data collection will occur online,
   state the program that will be used (e.g., Qualtrics, Skype, etc.)"*, and approved forms in this
   program name Qualtrics, Zoom, and Google Drive. `board-rules.md` §5's de-naming rule applies to the
   **Methods body only** — I left your de-naming there untouched. Restored only in §6 and in the
   consent forms' data-handling text.

4. **§9 worked totals and the course-credit paragraph** — umaine.md §7 requires the worked-total
   pattern (*"that would be $90 in total"*) and, where credit is offered, the alternative-route
   statement. Your Appendix C still offers course credit, so the §9 statement is load-bearing.

5. **Concise Summaries in Appendices A and B** — this one is a judgment call, not a gate. umaine.md §5
   records the trigger as *">1 page **or** federally funded"*, and CAREER meets both; but **zero**
   approved forms in this program contain one, so it is reported as `UNVERIFIED`, not `VIOLATION`.
   You kept the summaries in two forms and dropped them from three, which reads as incidental rather
   than deliberate. Restored for consistency — if you meant to drop them, delete all four.

I also restored the **CITI training sentence** in §3 (one sentence, standard for this application).

## Defects in the Google Doc I fixed

These are not restorations — they are places where the doc contradicted itself.

- **Appendix C carried two different time-commitment paragraphs**, back to back: one saying *"10-15
  minutes for each longitudinal follow-up survey"*, the next saying *"10–15 minutes for each survey,
  plus about 5 minutes for the matching survey."* Kept the second (it matches the procedures); dropped
  the first.
- **The intro sentence ended mid-clause** — *"…and participating in `<course name >`"* with no
  terminator.
- **The data-linkage checkbox had lost its explanation.** The optional second checkbox survived, but
  the Confidentiality paragraph explaining what linkage means was deleted. Restored the paragraph,
  the matching bullet, and the revocation clause.
- **The matching survey vanished from the student form's task list** but was still referenced by the
  time-commitment paragraph and by Appendix K. Restored the bullet.
- **Two student risks were deleted** — peer disclosure in groups, and instructor-proximity pressure —
  while §7 still claims those risks are *"mitigated by the deployment protections in Section 4."*
  Restored both bullets.
- **Chris Dufour** was removed from Personnel but remained in every consent form's Contact Information
  line. Removed.

## The consent-form merge, carried over from v6

| v5 / your doc | v7 | Document |
|---|---|---|
| A + B | **A** | Instructor participation, now including interviews |
| C | **B** | Student participation |
| D | **C** | Student survey (submission indicates consent) |
| E | **D** | Student and alumni interview |
| F–P | **E–O** | Instrument appendices, shifted one letter |

§5 now reads *"four consent forms… four genuinely distinct activity-and-population combinations."*
§9's tax sentence now names Appendices A, B, C, and D, and that is verified true of all four.

## Verification

- Appendices **A–O, contiguous**; **no dangling references**; **no orphan appendices**.
- **703 sentences from your Google Doc checked against v7: 17 have no equivalent**, and all 17 are
  expected merge consequences — the deleted instructor-interview form and its heading, the
  "covered by a separate consent form" pointers, the duplicated time-commitment paragraph, and six
  sentences reworded to fold interviews into Appendix A. Nothing was lost by accident.
- All four consent forms carry a Concise Summary, the tax block, and the CAREER title; none mentions
  Dufour.
- Nine narrative headings present and in the instructed order; page-number footer intact;
  `<course name>` and `<course number e.g. COS100>` both survived the build.
- Reading level (same implementation as the v6 report, **not** comparable to v5's table): Appendix A
  **11.5**, B 11.7, C 11.0, D 10.7. The merge did not make the instructor form harder to read. As
  before, none reaches grade 8; flagged, not fixed.

## Still open

1. **The cover page names Chris Dufour as CO-INVESTIGATOR.** `CURRENT/IRB2_CoverPage_v7.docx` still
   lists him with his email; the protocol no longer does. One of the two has to change before
   submission. Its title line does carry "CAREER:" correctly.
2. **Interview granularity** — merging removed the instructor's ability to consent to the study
   without consenting to interviews. Optional second checkbox available if you want it back:
   *"☐ I am willing to be contacted about a confidential interview (optional)"*.
3. **No student/alumni interview guide exists.** Instructors get a full guide (Appendix G); students
   and alumni get a consent form and no instrument. Every approved protocol documents its interview
   questions. Not a hard gate, but a visible asymmetry.
4. **Appendix C (student survey consent) scope** — still deferred.
5. **Three `{your input needed here}` markers** carried forward: the GenAI self-efficacy items and the
   wider first-year measure set (Appendix L), and the icebreaker question list (Appendix N).
6. **The activity table** in `irb-knowledge-base.md` §2 is stale — it still says "IRB #2 v4" and marks
   the student stream deferred. Pass-2 coverage checks run against it.

## Before submitting

Strip the red. The `{{...}}` markers live in `source/p2/*.md`; removing them and rebuilding produces a
clean document. Everything red is either a restoration you may want to keep or a fix you may want to
review — none of it is meant to reach the board as red text.
