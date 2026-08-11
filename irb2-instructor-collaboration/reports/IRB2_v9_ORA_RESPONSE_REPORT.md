# IRB #2 v9 — response to ORA review, verification report

**2026-08-10.** Base: `source/protocol_v8_MIDFINAL.md`, with the instrument appendices
restored from `source/protocol_v7_MERGED.md`. Plan approved by Cyril; see
`IRB2_v9_PLAN.md` for what was agreed and why.

- `source/protocol_v9_ORA_RESPONSE.md` — the source
- `CURRENT/IRB2_Protocol_v9_ORA_RESPONSE.docx` — 16,605 words, 1,023 paragraphs,
  page-numbered footer
- `archive/IRB2_Protocol_v8_SUPERSEDED_2026-08-10.docx`
- `archive/IRB2_Protocol_v7_SUPERSEDED_2026-08-10.docx`

**Everything changed this round is bold red — 82 marked spans.** That covers both the edits
threaded through the existing narrative and consent forms (24 spans) and the entire body of
the five new appendices K–O (58 blocks), so no new material is unmarked. v8's own 91 marks
were resolved to plain text first, so the red in this document means "new since the version
Aubrey commented on," not an accumulation of two rounds.

Two lines in Appendix I used `***bold-italic***`, which the .docx builder does not support
and which rendered a literal asterisk. Inherited from v8; converted to plain bold.

**Lineage.** v7 and v8 are both retired. There is now one live IRB #2 lineage.
`source/p2/*.md` still holds the v7 part-files and was not touched; it is now history.

---

## 1. What the review consisted of

Seven open comments, all from Aubrey Rogowski, left on the Google Doc "IRB 2" on
2026-08-07 between 20:57 and 21:09. The doc's `modifiedTime` is identical to the last
comment's timestamp, which establishes that its body text had not changed since the
2026-08-06 19:37 snapshot v8 was built from. Aubrey therefore read the *unrepaired* text,
including three broken appendix cross-references that v8 had already fixed (§2 item 6
pointed at a nonexistent Appendix M, item 16 at a nonexistent Appendix P, and data item
1.3 at Appendix H, which by then held the student intake survey and so read as correct).

The Drive API returns comment threads and anchor spans separately; they were matched by
document order against comment chronology. All seven pairings are semantically
unambiguous.

## 2. Response, comment by comment

| # | Comment | Response in v9 |
|---|---|---|
| 1 | "How many?" (design workshops, fall 2026) | §2 Methods now states approximately one to three instructor design workshops per design cycle and approximately one cycle per year. §2 item 3 states approximately 5 to 15 instructors per workshop. **See open item 1 — the per-workshop figure needs Greg's confirmation.** |
| 2 | "How many classrooms and students will be impacted?" | §2 Methods now states roughly 10 courses per year once the design has stabilized and points to Section 4, which already carried class sizes of 30–50, up to ~1,000 students, and up to ~200 instructors. No new numbers were invented. |
| 3 | "Include Appendix with survey questions." | New **Appendix K** (instructor interest and barriers survey, 11 items) and **Appendix L** (instructor follow-up survey, 6 items), restored verbatim from v7. Pointers added at §2 items 1 and 5 and at data item 1.1. Student survey instruments were already at Appendices H and I. |
| 4 | "Include Appendix with interview protocol." | New **Appendix M** (instructor interview guide, 10 topics), restored verbatim from v7 with a recording-consent opening added. New **Appendix N** (student and alumni interview guide, 14 topics), newly drafted — no such guide existed in any prior version. Pointers added at §2 items 2 and 13 and at data items 1.2 and 1.9. |
| 5 | "Will these be recorded?" (group meetings) | §2 item 8 now answers at the anchor: meetings are not recorded, no audio and no video is captured, no researcher attends, and what the research collects is written by participants themselves — the group's agenda notes and each member's individual written reflection. |
| 6 | Separate Qualtrics payment form; UMaine employees ineligible | New **Appendix O** (compensation information form), administered through Qualtrics as a standalone instrument. §9 and §6 state the mechanism and the separation; new data item 1.10 classes it as an administrative record rather than research data. §9 and Appendix A state that instructors employed by the University of Maine are not offered a gift card. §9 also states that no individual gift card exceeds $50. |
| 7 | "Students will also have to provide required information" | The Appendix O mechanism covers both populations. The Compensation section of Appendices B, C, and D each gained a plain-language paragraph. |

### The one thing deliberately not changed

§9 carries worked cumulative totals — "$50 in total" across two instructor interviews,
"$80 in total" across eight student follow-up surveys — and the >$75 tax-reporting
language. Against ORA's $50 cap these can look like a violation at a glance. They are not:
the cap is per card, and the largest single card is $25. `institutions/umaine.md` §7
records that this board *requires* worked totals ("that would be $90 in total"), so
removing them would be a regression. Flagged here so it is not mistaken for an oversight.

## 3. Verification passes

### Pass 1 — alignment against v8

459 source blocks in v8, 530 in v9. Eleven blocks were rewritten, every one of them a
deliberate edit above; 82 blocks added. **Nothing marked KEEP was dropped.** The only
content removed rather than expanded is the pair of example interview questions in §2
item 2, which v8 had added inline precisely because no appendix existed — they are now
redundant with Appendix M. The citations they sat next to (Damschroder et al.; Shadle,
Marker, & Earl) were retained.

### Pass 2 — coverage against the CAREER grant

The grant's §3.1.2 faculty-adoption plan is what comments 1 and 2 bear on, and v9's new
figures come from it: "a yearly design cycle for adoption with faculty… and a design
workshop," with co-design workshops running "until the design stabilizes, which we expect
by end of Year 2 or 3."

**The grant is silent on compensation.** All 27 pages were searched for gift cards,
incentives, compensation, stipends, honoraria, and dollar amounts. The only hits are a
"small grade incentive" idea for a future design (p. 9) and an unrelated citation. The
PDF contains the project description only — no budget justification. The $25/$10 figures
trace to prior YES Lab board precedent and to Greg's 2026-07-27 instruction, not to a
funded commitment, so excluding UMaine employees breaks nothing promised to NSF.

No grant-planned activity is uncovered by the protocol. No protocol activity lacks a
grant basis.

### Pass 3 — internal consistency

Mechanical check across the protocol, all four consent forms, both recruitment appendices,
and all five new appendices:

| Fact | Occurrences | Result |
|---|---|---|
| $25 per interview | 5 | identical |
| $10 per follow-up survey | 7 | identical |
| $75 tax-reporting trigger | 5 | identical |
| 8 follow-up surveys over four years | 4 | identical |
| 30–60 minute interviews | 6 | identical |
| 10–15 minute surveys | 16 | identical |
| December 2031 key deletion | 9 | identical |
| 72-hour recording removal | 7 | identical |
| 48-hour gift card delivery | 9 | identical |
| 14-day archiving | 7 | identical |

Appendix cross-references: **15 appendices, lettered contiguously A–O; 54 mentions; zero
dangling references, zero appendices defined but never referenced**, checked in both
singular ("Appendix K") and plural ("Appendices K and L") forms. The 20-broken-reference
failure of the last round does not recur — existing letters A–J were left untouched and
the five new appendices were appended.

### Pass 3b — .docx fidelity

The built document was unzipped, stripped to text, and diffed against the source:
**530 source blocks, 530 document paragraphs, zero content differences.** 82 bold-red runs,
and zero literal brace or asterisk artifacts in the rendered text.

### Pass 4 — institutional compliance (`institutions/umaine.md`, fetched 2026-07-28)

This pass flags; nothing here has been fixed.

**Clean:** Word format not PDF; whole document page-numbered; nine narrative headings
present and in order; title matches the grant title; years of human-subjects experience
given as a number for every person in §3; consent forms follow the board-approved heading
order (Confidentiality before Compensation) and the approved checkbox-plus-email closing;
gift card value and vendor both stated; withdrawal handling stated; extra-credit
alternatives stated; tax-reporting language present with the HR/Purchasing split and the
$600 Form 1099 threshold; Qualtrics named as the online collection program for Appendix O,
as §6 of the institution file requires vendors to be named in data-handling text.

**Reading level.** The board requires consent forms "written no higher than an 8th grade
reading level." The new consent-form paragraphs were drafted, measured, and rewritten: they
now grade **2.6 to 7.1** (Flesch–Kincaid). The document as a whole grades 10.9, which is a
pre-existing property of the inherited forms and unchanged this round.

**Findings — blocking:**

1. **The cover page names a fourth investigator the protocol does not.**
   `CURRENT/IRB2_CoverPage_v7.docx` lists **Chris Dufour** as a co-investigator. §3
   Personnel and all four consent forms name only Nelson, Agbewali-Koku, and Schotter. The
   board's hard gate is "include the years of human subjects research experience for ALL
   personnel listed." Either add Dufour to §3 with a years figure and to the consent forms'
   researcher lists, or remove him from the cover page. **PI decision — I have changed
   nothing.**
2. **The cover page START DATE is still an unfilled placeholder.** It carries a bracketed
   "your input needed here" note. The application is returned incomplete without it.

**Findings — not blocking:**

3. **No concise summary.** Required by the checklist for forms over one page *or* federally
   funded studies; this protocol is both. Zero approved forms in this program contain one,
   and every prior protocol was unfunded, so there is no in-program evidence the board
   enforces it. Recorded as `UNVERIFIED` in the institution file and still unresolved.
   Cheap insurance if you want it.
4. **"Students and employees of the University" are not named as an undue-influence
   population in so many words.** §4's Coercion considerations covers both groups
   substantively, but the instructions ask that the category be named. This is more visible
   now that §9 turns on University employment. One clause in §4 would close it.
5. **Appendix H carries an open drafting note** asking for the exact items of the critical
   and reflective generative AI use measure — the four-question self-efficacy measure and
   whether the ChatGPT Literacy scale is used in full, in part, or not at all. Inherited
   from v8, unresolved.
6. **Exempt category 2(ii) is unavailable to this protocol.** §7 asserts a
   professional-reputation risk to instructors from disclosure, which contradicts 2(ii)'s
   condition. Any exemption claim must go to 2(iii) or higher. Pre-existing; noted because
   the cover page's review-category selection has to be consistent with it.

## 4. Open items for Greg

1. **Instructors per design workshop.** v9 says "approximately 5 to 15," derived to be
   consistent with §4's ~200-instructor ceiling. It is red-marked in the document. The
   grant gives no figure. Confirm or replace.
2. **Chris Dufour** — on the protocol or off it (blocking finding 1).
3. **Cover page start date** (blocking finding 2).
4. **The UMaine-employee exclusion** — Cyril approved the drafting approach; the
   recruitment consequence is real, since early-cycle instructors are disproportionately
   UMaine colleagues.
5. **Appendix H's missing AI measure items** (finding 5).

## 5. Response text for Aubrey

Suggested reply against each comment, for pasting into the Doc or an email:

1. Added to §2: approximately one to three design workshops per cycle, approximately one
   cycle per year, and approximately 5 to 15 instructors per workshop (§2 item 3).
2. Added to §2: roughly 10 courses per year once the design has stabilized, with the full
   participant numbers in §4 — class sizes of 30–50, up to ~1,000 students and ~200
   instructors over the award.
3. Added Appendix K (instructor interest and barriers survey) and Appendix L (instructor
   follow-up survey). Student survey instruments are at Appendices H and I.
4. Added Appendix M (instructor interview guide) and Appendix N (student and alumni
   interview guide).
5. No. Reflection group meetings are not recorded — no audio, no video, and no researcher
   attends. The research collects only what participants write themselves: the group's
   agenda notes and each member's individual written reflection. Stated at §2 item 8.
6. Added Appendix O, a standalone Qualtrics compensation information form administered
   outside every research instrument and never linked to responses (§6, §9, data item
   1.10). §9 and Appendix A now state that instructors employed by the University of Maine
   are not offered a gift card, per the policy you linked. §9 also confirms no individual
   gift card exceeds $50.
7. The same Appendix O mechanism applies to students; the Compensation section of each
   student consent form (Appendices B, C, D) now says so in plain language.

## 6. Skill revisions made this round

- `board-rules.md` — the board requires actual instruments as appendices for surveys and
  interview guides.
- `institutions/umaine.md` §5 — the "topical description plus one or two examples covers
  both" allowance is contradicted by this review. It drove v8's inline approach and cost a
  round.
- `institutions/umaine.md` §7 — gift card rules added: employees ineligible, $50 per-card
  cap, separate unlinked payment form required, W-9 where applicable, with the ORA policy
  URL.
