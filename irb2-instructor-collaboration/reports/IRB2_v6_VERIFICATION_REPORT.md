# IRB #2 v6 — verification report

**Drafted 2026-08-06. One change from v5: the two instructor consent forms are merged into one.**
Everything else is a consequence of that — appendix relettering and the narrative sentences that
counted or named the forms. No procedure, population, instrument, compensation amount, or data
flow changed.

Read this instead of re-reading v5's report for the parts it covers; v5's findings on coverage,
structure, and open decisions still stand except where noted below.

## What changed and why

v5 carried **five** consent forms. IRB #1, as submitted, carries three. The gap is structural —
IRB #1 has one population crossed with three activities, IRB #2 has two — but two of the five were
genuinely mergeable. Cyril's call was to consolidate the **instructor** pair.

| v5 | v6 | Document |
|---|---|---|
| A + B | **A** | Instructor participation, now including interviews |
| C | **B** | Student participation |
| D | **C** | Student survey (submission indicates consent) |
| E | **D** | Student and alumni interview |
| F–P | **E–O** | Non-consent appendices, shifted one letter |

Instructors now consent once for everything they might do. Students keep a separate interview form,
which preserves the grade-pressure protections that form carries.

**Size:** consent forms 7,776 → 6,722 words (−1,054). Whole document 17,223 → 16,178 words.
Merged Appendix A is 2,140 words, against 1,731 + 1,450 = 3,181 for the two it replaces.

## Pass 1 — alignment diff against v5

The failure mode of a merge like this is a silently dropped clause from the absorbed form. Checked
directly: of 28 substantive paragraphs and bullets in v5's Appendix B, **28 survive** in v6 — 27
verbatim, one (the "talking through your teaching decisions" benefit) folded into an existing
Appendix A bullet with "in an interview" added for clarity.

Seventeen named KEEP passages verified present in merged Appendix A:

| Present | Passage |
|---|---|
| ✓ | The **>$75 tax-reporting block** — HR for employees, Purchasing for non-employees, Form 1099 at $600 |
| ✓ | $25 per interview, gift card within 48 hours |
| ✓ | Worked total — *"two interviews and $50 in total"* |
| ✓ | Stopping partway forfeits the gift card |
| ✓ | *"transcribed by the named researchers, not by an outside transcription service"* |
| ✓ | Handheld-recorder deletion within 72 hours for in-person interviews |
| ✓ | Zoom recordings removed within 72 hours |
| ✓ | 30–60 minute interview length; audio only, no video; notes if the participant declines recording |
| ✓ | Recording retention tied to the key file, five years, with the December 2031 example |
| ✓ | Follow-up interview in a later semester, free to decline |
| ✓ | Advocacy-pressure risk (reworded to cover interviews as well as workshops) |
| ✓ | De-identified transcripts may be shared or deposited |

Of the 105 changed lines, **45 differ only by appendix letter**.

Three deliberate departures from verbatim carry-over, all in merged Appendix A:

1. Appendix B's revocation clause *"you would need to agree again to this consent form before any
   further interview"* was **dropped** — incoherent once the form is signed once for everything.
   The general revocation right (five years, key-file-tied) is unchanged.
2. The archival / key-file paragraph was **verbatim identical** in both forms; one copy kept, per
   the skill's no-duplication rule.
3. The time-commitment total moved from *"about two to six hours"* to *"about three to seven
   hours"*, to account for an interview now being inside this form's scope.

## Pass 2 — source coverage against the CAREER grant

Unchanged from v5. The merge moved consent language between documents; it did not add or remove a
planned activity. Instructor interviews are still described in §2 item 2, §5, §9, and Appendix G
(the interview guide). v5's finding that the **video-assisted comparative reflection assignment**
is covered by no protocol still stands — backlog item 8.

## Pass 3 — internal consistency

- Appendix headings **A–O, contiguous, no gaps**.
- **No dangling references** — every `Appendix X` mention resolves to a heading that exists.
- **No orphan appendices** — every appendix is referenced from the narrative at least once.
- §5 now reads *"four consent forms… four genuinely distinct activity-and-population
  combinations"* (was five/five).
- §9's tax sentence now reads **"Appendices A, B, C, and D"** and is verified true: all four forms
  are compensated, and all four carry the tax-reporting language. This is a **substantive change** —
  v5's Appendix A had no compensation and no tax language; the merged form has both.
- Repeated figures agree throughout: $25 interview, $10 survey, $75 trigger, $600 threshold, eight
  follow-up surveys over four years, 72 hours, 14 days, 30–60 minutes, 10–15 minutes, December 2031.
- Appendix I's interview-invitation email no longer promises a separate *"interview consent form"*;
  it now uses the same *"if you have not already, you will see our consent form"* phrasing the
  workshop invitation already used.

## Pass 4 — institutional compliance (UMaine)

Flagged, not fixed. Checked against `institutions/umaine.md`, on the files that will actually be
attached.

**Hard gates — all pass:**

- Two attachments: cover page separate, narrative + all appendices as one Word document.
- `.docx`, not PDF; no Google Docs round-trip.
- Page numbering — the `Page X of Y` footer field is present in the rebuilt document.
- Nine narrative headings, present and in the instructed order.
- Title matches the grant title.
- Years of human-subjects experience given as a number for all four personnel.
- Consent forms follow the **board-approved** heading order (Confidentiality before Compensation),
  with the checkbox-plus-email affirmation and no investigator signature line.

**Merged Appendix A, against §5/§6 disclosure requirements — all present:** Qualtrics and Zoom named;
IP addresses not collected; transcription by named researchers stated; 72-hour Zoom deletion; key
electronic and encrypted; destruction stated as a month and year; time-burden estimate; ORC contact
and phone.

**Concise Summary** present in all four forms. Still `UNVERIFIED` rather than `VIOLATION`, per
umaine.md §5 — no approved form in this program has one, but CAREER is the first federally funded
protocol and so the first to hit the checklist trigger.

**Reading level.** Measured with a Flesch-Kincaid implementation written for this pass, so the
absolute numbers are **not comparable** to the table in v5's report, which used a different one.
The comparable claim is relative, measured the same way on both:

| Document | Grade |
|---|---|
| v5 Appendix A (instructor participation) | 11.7 |
| v5 Appendix B (instructor interview) | 11.7 |
| **v6 Appendix A (merged)** | **11.6** |

The merge did not make the instructor form harder to read. As in v5, **no form reaches grade 8**,
and getting there would mean rewriting board-approved retention and confidentiality wording. Flagged,
not fixed — same call as v5.

**Nothing in this pass is blocking.**

## Decisions for the PI

1. **Interview granularity — new, created by this merge.** An instructor can no longer consent to
   the study without consenting to interviews. In practice an interview is still opt-in twice over:
   Appendix E's survey carries *"an option to volunteer for a follow-up interview"*, and the
   interview itself is scheduled by the participant. If you want the granularity back explicitly,
   add a second checkbox to Appendix A, mirroring the optional-checkbox pattern already approved in
   the student form:

   > ☐ I am willing to be contacted about a confidential interview (optional; you may take part
   > without agreeing to this)

   **Recommended.** Cheap, and it restores what the separate form provided.

2. **Consent timing.** §5 now says Appendix A is signed *"before any research activity, including…
   before any interview begins."* An instructor may sign it at recruitment and be interviewed a year
   later. That satisfies consent-before-activity, but confirm you are comfortable with the gap.

3. **Appendix C (student survey consent) scope** — deferred by your instruction, not examined in this
   pass. `board-rules.md` §3 says no separate survey consent is needed where participants have
   already consented, and Appendix B already covers students' follow-up surveys explicitly. Its only
   irreplaceable role is comparison-course students. Worth a pass of its own.

**Carried forward from v5, unchanged:** the three `{your input needed here}` markers (GenAI
self-efficacy items and the wider first-year measure set in Appendix L, adapted icebreaker questions
in Appendix N); the cover page's human-subjects start date; and the **Dufour dual-role conflict**,
which remains open — §4 excludes courses taught by research-team members, Chris Dufour is listed as
personnel, and the funded plan names his seminar as a deployment site.

## Tooling note

The v5 `.docx` was hand-built OOXML with no build script in the repo, which made every revision a
from-scratch job. Two scripts now exist:

- `tools/build_docx.py` — assembles the six-part OOXML package from the merged markdown, including
  the page-number footer.
- `tools/docx_text.py` — extracts paragraph text, for diffing one submission against the next.

**Both were validated before use.** Rebuilding v5 from its own unmodified source produced a document
text-identical to the delivered v5 submission (one stray blank paragraph aside), with every
paragraph and run format class matching by count. The assembly recipe was separately verified
byte-exact against the committed `protocol_v5_MERGED.md`.
