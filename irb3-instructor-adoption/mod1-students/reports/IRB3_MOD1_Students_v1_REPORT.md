# IRB #3 Modification 1 (students) — v1 drafting + verification report

Drafted 2026-08-25. The modification adds student participants in collaborating
instructors' courses to the **approved** instructor-adoption protocol. Every addition is
wrapped in `{{...}}` in `source/mod1_students_v1.md` and renders **bold red** in
`CURRENT/IRB3_MOD1_Students_v1.docx` — which is also the markup UMaine's modification
instructions require ("edit all applicable sections … in a different font colour").
**No approved text was removed**; the mod is additions only, plus two cosmetic fixes noted
under Deletions/normalizations.

## ⚠ Blocking flag — modification vs. new study

UMaine's modification rule (`references/institutions/umaine.md` §10, from the published
[modification request instructions](https://umaine.edu/research-compliance/human-subjects/request-modification-previously-approved-study/)):
a modification that changes **two or more** of {study population, study procedures, study
purpose} *"becomes a new study."* Adding the student arm changes **population and
procedures** — two criteria. This is the exact rule that killed the IRB #2a/#2b split in
July (see `irb2b-student-stream-held/README.md`).

Mitigating context: the ORA reviewer (Aubrey Rogowski) has already been commenting
directly on the student sections of the working Google Doc (2026-08-07 through 08-13), so
ORA has seen and engaged with this content. **Recommendation: Greg confirms with ORA by
email whether this enters as a modification or as a new application before submission.**
The document works either way — as a mod it is the approved application with red
additions; as a new application the same document is submitted with a cover page and the
mod-header line removed.

## Inputs used (provenance)

- **Base protocol (KEEP, verbatim):** `2026_08_09_Nelson_IRB_FINAL_1.pdf` — the approved
  IRB #3 as uploaded by Cyril, 2026-08-25. This is the authority wherever it differs from
  the repo's `source/protocol_v2_ORA_RESPONSE.md` (it does: UMaine employees ARE
  compensated via the University's regular payment process; "2 business days"; consultations
  on Zoom and recorded; no Appendix F; §5 submission-indicates-consent wording).
- **Students content (ADAPT):** Google Doc `1evcxa_HrsjqH7PlaSCmaED_CoEMaDp9wz6oBimoR8Pg`
  ("students part"), including its 13 comment threads from Greg Nelson and Aubrey
  Rogowski (ORA).
- **Governing document:** NSF CAREER grant (Award 2544192) — student arm activities per
  the activity table (classroom use, student surveys, reflections, longitudinal follow-up,
  student/alumni interviews, comparison courses).
- **Accepted-language sources:** `references/board-rules.md` (incl. §5b, the 2026-08-14
  ORA review of IRB #3), `references/institutions/umaine.md`, and Appendix R MOD Jan/26 of
  the approved GenAI protocol (`inputs/approved-protocols/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx`)
  for the student/alumni interview consent form, per Greg's comment.

## How each Google-Doc comment was handled

| Comment (author, date) | Handling |
|---|---|
| "UMaine IRB … aren't allowing student opt-out consent … need opt-in" (Greg, 08-11) | All opt-out consent language replaced with **opt-in**: narrative items 9/§5, recruitment script, student consent form intro, Voluntary section, site-approval letter. The opt-in record is the board's approved **checkbox-plus-email** block, not a signature (the reviewer deleted a signature line from this exempt study on 08-14, so Cyril's planned "will sign a consent form" wording was NOT used). |
| "Remove the consent form from … the longitudinal follow-up in general" (Greg, 08-11) | The student course consent form (Appendix F) now covers the follow-up surveys explicitly ("This form covers those surveys, and submitting one indicates your continued consent"); Appendix K's intro says the same. No consent form gates follow-ups. The former standalone longitudinal consent form survives only as the **comparison-course** form (Appendix G), where it is genuinely needed (those students never see Appendix F). |
| "We will use a secure automated transcription service" (Greg, 08-11) | Stated in narrative §6 and in the student/alumni interview consent form (Appendix H). The "transcribed by the named researchers; no outside transcription service" sentences from the old draft were dropped. |
| Student/alumni interview consent "should match Appendix R MOD Jan/26 … allow screen recording" (Greg, 08-11) | Appendix H rebuilt on Appendix R's structure: Zoom or in person by preference and researcher availability; audio + screen-share recording (no face), notes fallback; 14-day archival; key file with 5-year example; per-interview compensation with worked total; checkbox-plus-email closing. |
| Surveys "missing … Self-reflection and Insight scale, 7-item psychological safety scale" (+ SDL scale) (Greg, 08-11) | SRIS 20 items included (already pasted by Cyril in the gdoc). **Psychological safety: the 7 Edmondson (1999) items added, adapted to the reflection group — confirm wording.** SDL scale items were images in the gdoc and could not be read — left as a `[PI DECISION NEEDED]` paste-from-2024_08-IRB marker. |
| "Students will also have to provide required information to receive a gift card" (Aubrey) | Compensation information form included as Appendix N, referenced from §6, §9, data item 1.9, and the gift-card paragraphs of every compensated consent form. |
| Gift-card policy: separate form; UMaine employees ineligible (Aubrey) | Separate-form process is in the approved base already; extended to students. Employee handling follows the **approved final** (compensation via the University's regular payment process), not the gdoc's older "not offered" wording. |
| "How many classrooms and students will be impacted?" (Aubrey) | ~10–20 collaborating courses per year (Methods intro); up to ~2,000 students over the study (Population). |
| "Will these be recorded?" (Aubrey) | Group meetings: stated **not recorded** — "the research collects only what is written by consenting participants" (narrative item 8, Appendix F, §6). |
| Hanging "comparison-course adaptation" header (Greg) | The comparison-course form is now its own clean Appendix G with an italic usage note. |
| "Include Appendix with survey questions / interview protocol" (Aubrey, resolved) | Student instruments are Appendices J, K, L; every student-facing method names its instrument appendix. |

## Wording/structure rules applied to the student text (from the board file)

The gdoc student text predates the 2026-08-14 ORA review, so every accepted fix was
carried into it (`board-rules.md` §5b, §4, §4b; `umaine.md` §4–§7):

1. **No signature lines**; opt-in via the approved checkbox-plus-email block; "You do not
   need to sign this form."
2. **Every Methods item states mode + named platform + recording terms + compensation or
   its absence** (Qualtrics for all student surveys; Zoom or in person for interviews;
   groups not recorded; design sessions not recorded, not compensated).
3. **Follow-ups fully specified**: cadence (~every 6 months, up to 4 years, up to 8
   surveys), same procedures, own instrument appendix (K), own invitation script.
4. **Every recorded activity has its own recruitment script** — a student/alumni
   interview invitation was missing from the gdoc and was added (Appendix I).
5. **Recruitment scripts** say "research"/"University of Maine research study" in the
   opening sentence and carry researcher contact info.
6. **"Respond to"/"submit," not "complete"**; "one gift card per survey invitation."
7. **"48 hours" → "2 business days"** everywhere (matches the approved base).
8. **No bare calendar dates** in consent forms ("until Dec 15, 2031" → key-file phrasing
   with a cohort-example date, the format that survived review).
9. **Second person throughout** the consent forms.
10. **Group cannot-guarantee-confidentiality sentence** (the accepted IRB #2 v9 wording)
    extended to reflection groups in narrative §6, §7, and Appendix F's Risks and
    Confidentiality.
11. **Extra-credit rule**: credit is for submission, available to all students, other ways
    to earn it, and **all instructors must agree** where several classes are involved
    (`umaine.md` §7).
12. **Worked compensation totals** ($40/$80 follow-ups; $50 two interviews; $130 combined)
    and the **>$75 tax-reporting sentence** in §9 and every compensated consent form —
    eight $10 surveys alone cross the $75 threshold, so this is now required, and it was
    missing from the gdoc.
13. **Ceiling-not-forecast population numbers** ("up to approximately 2,000"), course
    counts kept in Methods.
14. **Duplication removed**: student protections stated once in §4 and referenced from §7;
    consent mechanics once in §5.

## Deletions / normalizations from the gdoc student text (invisible in red — review here)

1. Opt-out consent procedure ("Students opt out by emailing…") → opt-in (Greg's comment).
2. "Recordings are transcribed by the named researchers; no outside transcription service
   is used" → secure automated transcription service (Greg's comment).
3. The consent form gating longitudinal follow-up surveys (Greg's comment).
4. "48 hours" → "2 business days"; "$X sent within 48 hours" phrasing normalized.
5. "until Dec 15, 2031" → key-file phrasing with example (board ordered this deleted on
   the instructor form 08-14).
6. The "matching survey" term and data item — the demographics live in the pre-course
   survey (Appendix J); one instrument, one name. Flag if a separate matching survey is
   actually planned.
7. "Have your assignments and other work for the class analyzed" → reflection-group
   materials and reflection assignments only, matching the narrative's "no grades,
   academic records, or other student-records data" commitment.
8. The third-party-apps risk paragraph (Facebook/Instagram/…): this protocol names no
   student-facing application, so the paragraph asserted a risk from a mechanism the
   protocol doesn't have. Restore only if a tool/app is actually deployed to students.
9. The instructor professional-reputation risk paragraph was NOT added to §7: the
   approved §7 doesn't assert it, and asserting it can conflict with an exempt 2(ii)
   determination (`umaine.md` §8, "the 2(ii) trap").
10. Duplicate/contradictory time-commitment paragraphs in the student consent form merged.
11. Old draft's consultation-not-recorded and workshop-recording-optional variants —
    superseded by the approved final's recorded versions (base text untouched).
12. Two cosmetic fixes to the base text (added the missing period in "Appendix E.
    Participants", capitalized "Appendix A" in Methods item 4) — not marked red.

## Verification

- **Pass 1 — alignment vs. the approved PDF:** all 373 sentence-chunks of the approved
  document are present verbatim in the mod except (a) PDF text-extraction artifacts
  (bullet glyphs, line-break hyphens) and (b) the marked insertions listed above.
  Nothing approved was dropped or reworded.
- **Pass 2 — source coverage:** grant student-arm activities covered: classroom use,
  reflection materials, pre/post surveys, longitudinal follow-up, student & alumni
  interviews (incl. work examples), design input, comparison courses, external sites.
  NOT covered here (unchanged scope decisions): the video-reflection assignment (backlog
  item 8), GenAI usage logs, data linkage beyond the optional linkage checkbox.
- **Pass 3 — internal consistency:** $10/$25 amounts, "2 business days," 14-day archival,
  5-year key deletion with December 2031 example, up-to-eight surveys / four years,
  10–15 minute estimates, ~2,000 students, 10–20 courses — identical at every occurrence
  (grep-verified; zero "48 hours", zero bare "Dec 15, 2031").
- **Pass 4 — institutional compliance (flags, not fixes):**
  - `VIOLATION if unfixed at submission`: the four `[PI DECISION NEEDED]` instrument
    placeholders in Appendices J/K — the board requires the actual instruments, and the
    scale items were images in the gdoc that could not be extracted. Paste from the
    2024_08 reflection-groups protocol before submitting.
  - `UNVERIFIED`: no concise summary — matches every approved form in the program,
    including the approved base; the published checklist suggests funded studies need one
    (`umaine.md` §5).
  - Submission mechanics: one Word document, page-numbered (the build includes the
    Page X of Y footer), emailed to umric@maine.edu **referencing the approved title and
    number** — fill the `[PI DECISION NEEDED: approved protocol number]` in the header.
  - Reading level: student forms drafted to ~8th grade; PI judgment on the remaining long
    confidentiality sentences (they mirror approved language).

## [PI DECISION NEEDED] — all open items

1. Approved protocol number + approval date for the mod header (and Greg's ORA email on
   mod-vs-new-study, per the blocking flag).
2. Appendices J/K: paste the four image-based scale blocks (gender/race demographics,
   programming self-efficacy, professional/STEM identity + professional/reflection skills,
   SDL scale) from the 2024_08 approved protocol.
3. Psychological safety scale: added as the 7 Edmondson items adapted to "this group,"
   with a pre/post referent note — confirm the wording matches the 2026 pre/post surveys.
4. Appendix N (compensation information form) is included although the approved base was
   approved without one; board-rules §4 requires it and ORA drafted the requirement.
   Delete it (and its cross-references in §6/§9/1.9) if Greg prefers the approved-base
   minimal pattern.
5. The optional prior-research data-linkage checkbox is kept on Appendices F and H —
   confirm, since the separate data-linkage mod (backlog item 7) is unsubmitted.
6. Population ceiling kept at "up to approximately 2,000 students" and the gdoc's
   "(could be higher)" hedge dropped — raise the ceiling instead if 2,000 is not
   comfortably generous.
7. Comparison-course pre/post surveys: drafted as not compensated and with no extra-credit
   arrangement stated. If comparison instructors will offer credit, the all-instructors-
   must-agree language extends to them.
