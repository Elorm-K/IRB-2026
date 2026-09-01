# IRB #1 v5 — response to the board's review, verification report

**2026-08-28.** Base: the package submitted to the board on **2026-08-01**
(`archive/IRB1_Submitted_2026-08-01_BASE.pdf`), not any file in
`CURRENT/protocol-candidates/` — the submitted version is a revision ahead of all three of
those, so building on them would have silently reverted Greg's pre-submission edits.

- `source/protocol_v5_ORA_RESPONSE.md` — the source; edit here, not the `.docx`
- `source/protocol_v5_ORA_RESPONSE_CLEAN.md` — generated, `{{…}}` marks resolved
- `CURRENT/IRB1_Protocol_v5_ORA_RESPONSE_MARKED.docx` — everything new or rewritten in
  **bold red**, for review
- `CURRENT/IRB1_Protocol_v5_ORA_RESPONSE.docx` — the same document with the marks
  resolved. **This is the file to submit.**
- `source/media/` — the five instrument images from Appendix C, carried over intact

Rebuild either with `python3 tools/build_docx.py <source.md> <out.docx>`. `tools/build_docx.py`
gained inline-image support this round (`![alt](media/x.png)`), which is what makes it
possible to keep the survey-instrument screenshots in a document generated from markdown.

---

## 1. The reorganization the review asked for

Nearly every point traces back to one structural correction: **the reflection groups are
not research, so the board does not review them.** What it reviews is (a) the research use
of the materials those groups generate, and (b) the research activities run outside them.
The review then asked for the whole application — narrative *and* appendices — to be
organized into five parts:

| # | Part | Population | Consent mechanism |
|---|---|---|---|
| 1 | Research use of reflection-group materials | Members | **Opt-out** (Appendix A) |
| 2 | Longitudinal follow-up surveys | Members | Submission indicates consent (Appendix B) |
| 3 | Interviews | Members | Taking part indicates consent (Appendix D) |
| 4 | Comparison-population surveys | Professionals | Deferred to a modification |
| 5 | Comparison-population interviews | Professionals | Deferred to a modification |

That framework now drives Methods, Recruitment, Informed Consent, Confidentiality, and the
appendix lettering.

**One wording note for the board.** The review's comments say "coursework" throughout
(*"asking to use their course work for research purposes"*). This protocol covers reflection
groups held **outside any course**, so there is no coursework; the equivalent category is
the material the groups themselves generate. v5 therefore says **"reflection-group
materials"** wherever the comments say "coursework". The mechanism the review asked for —
opt-out, verbal script at the first session, no instrument appendices — is unchanged.

## 2. Response, point by point

### General

| # | Point | Response |
|---|---|---|
| G1 | Use "members" for reflection-group status, "participants" for research role, throughout including appendices | Done, and the distinction is now defined once in §2 and used consistently. RQs 2 and 4, §4's group-size sentence, and the Summary's "offered as an ongoing service to members" all changed. Verified by grep: no remaining use of "participant" for group status |
| G2 | No "opt-in"/"opt-out" for reflection-group membership; only for research | Done. Every surviving "opt out" refers to research use of data. "People who opt in take an initiation survey" is gone with the abbreviated service section; the professionals-in-groups and group-remedy items that used "opt in" were cut entirely |

### Methods

| # | Point | Response |
|---|---|---|
| M1 | Items 1 & 2 belong in Recruitment and Informed Consent; recruitment into the groups is not reviewable; use a verbal script at the first session; use an opt-out for the materials | Both items deleted from Methods. §4 now opens by saying how members come to join a group is not part of the application, then gives the five recruitment sections. The verbal first-session script is **Appendix F.1**; the opt-out form is **Appendix A**. §5 (1) states the opt-out mechanism |
| M2 | Abbreviate the reflection-group service section to one sentence per data item; drop instrument appendices for it; state up front that no coursework data is sensitive | Section retitled *"Reflection-group materials collected as part of normal reflection-group activities"* and cut from eight numbered procedures to six one-sentence items, each naming what is collected and the format (Qualtrics, the group's shared online workspace, exported from the tool). The old Appendix B is deleted, so the service now has no instrument appendix. The sensitivity statement is in §2 — see the caveat in §4 below |
| M3 | Rename "For the research" | Now *"Research data collected outside of normal reflection group activities"* |
| M4 | Don't reference recruitment materials here, only instruments | The pointer to the old Appendix E is deleted. Methods now points only to Appendix C (survey questions), Appendix E (interview guide), and the two consent forms |
| M5 | State whether surveys are anonymous or confidential | *"confidential rather than anonymous: each response carries the participant's email address as an identifier"* — in §2 item 7 and again in Appendix B |
| M6 | More detail on what determines when interviews take place | New paragraph after item 8 with six worked examples — on joining, cycle midpoint, after the retrospective, after leaving a group, after a survey response indicates a large change or a described barrier, and on the member's own request |
| M7 | State the length of interviews | 30–60 minutes, in §2, Appendix D, and Appendix F.3 |
| M8 | State the format of interviews | One-to-one; online on Zoom or in person by participant preference. §2 also states explicitly that **there are no group interviews** — see G-review point below |
| M9 | State how interviews will be audio recorded | Zoom's audio-only recording online; a password-protected handheld recorder in person; no video; agreeing to be recorded is **not** required, written notes are the fallback; transcribed by the named investigators, no outside service |
| M10 | Comparative group: timing, instruments, mode, length, confidentiality — or the modification statement | The modification statement, verbatim from the review, in §2 item 9, plus a sentence listing what the modification will carry |
| M11 | Delete the enrolment/recruitment-channel sentence from Methods | Deleted from Methods; the anticipated figures (60–100 intervention, ~200 comparison) and the channels moved into §4 (4)&(5), as the review permitted |

### Recruitment

| # | Point | Response |
|---|---|---|
| R1 | Keep the first paragraph; replace the rest with five recruitment sections | Both population paragraphs kept (only "3–5 members" changed). Everything after is rewritten as sections (1)–(3) and a combined (4)&(5). The information-session and study-webpage sentences are deleted — both described recruitment into the groups |
| R2 | Include and reference all recruitment appendices | **Appendix F** holds F.1 (verbal first-session script), F.2 (survey invitation email), F.3 (interview invitation email), and F.4/F.5 reserved for the comparison population. Each is referenced from its own recruitment section. Every script states it is research in its opening lines, names a researcher with contact information, and — for the interview — describes the recording and the notes fallback |
| R3 | Modification statement for comparison-group recruitment | Present verbatim in §4 (4)&(5) |

### Informed consent

| # | Point | Response |
|---|---|---|
| C1 | Five consent forms | Three are written: **A** (opt-out, materials), **B** (surveys), **D** (interviews). The two comparison-population forms are deferred with the modification statement, and §5 (4)&(5) describes exactly what they will be — Appendices B and D with the purpose sentence replaced and reflection-group references removed. **See open item 1** |
| C2 | For each, say how the form is received and what indicates consent; for the opt-out, say by when, how, and to whom | §5 is rewritten as five subsections. Opt-out: emailed to every member on the day of the first session, decision requested **within two weeks**, by email to any listed researcher, subject line "Opt out of reflection research", reversible at any later time, no reason required. Surveys: form is the first page, submission indicates consent. Interviews: form emailed with the scheduling link, reviewed at the start, taking part indicates consent. §5 also states that no form is signed |

### Confidentiality

| # | Point | Response |
|---|---|---|
| F1 | Delete the first paragraph | Deleted |
| F2 | The delete-on-request paragraph is optional | **Kept.** It is board-approved language carried in every protocol in this program, and dropping it would be a regression against §1 of the recorded board rules. Flagged here so it reads as a choice, not an oversight |
| F3 | Re-organize around the five sections | §6 now runs: storage and access → reflection-group materials → surveys → interviews → compensation information → archiving and opt-out filtering → key file → retention → recordings → withdrawal |
| F4 | Audio-recording details, month/year, no indefinite retention | Off the recording device within **72 hours** (Zoom recordings removed from Zoom, handheld recordings removed from the device). Each recording deleted when the participant's key entry is deleted, five years after their participation ends — *"for a participant whose participation ends in Fall 2026, by the end of December 2031"* — and a hard outer bound: **no audio recording retained beyond December 2036** |

### Risks / Benefits / Compensation

| # | Point | Response |
|---|---|---|
| K1 | Delete the peer-disclosure risk | Deleted from §7 and from every consent form |
| B1 | Delete the participant-benefit clause | Deleted. §8 now reads "There are no direct benefits to participants." |
| B2 | Frame broader benefits as potential | Rewritten with "may … may … may", closing *"These are potential benefits to others rather than promised outcomes."* |
| P1 | Delete the first sentence | Deleted. Replaced with *"There is no compensation for the research use of reflection-group materials"* — the board separately requires compensation or its absence stated for **every** method, and this states it for the method rather than for group membership |
| P2 | Delete "(the initiation survey is not compensated)" | Deleted, and the problem behind it is gone: the initiation survey is now service data under part 1, not a research survey, so there is nothing to exempt |
| P3 | Same $25 for comparative interviews? | **Yes** — stated in §9: comparison-group participants are offered $10 per follow-up survey submitted and $25 per interview completed |
| P4 | Final distribution dates (MON/YR) per type | *"Gift cards are sent as each survey is submitted and as each interview is completed. The final gift cards under this protocol will be distributed no later than December 2035"* — the end of the four-year follow-up window for the last participation cycle the protocol anticipates. **See open item 2** |

### Appendices

| # | Point | Response |
|---|---|---|
| A1 | Appendix A should be the opt-out form only | Rewritten as **Appendix A: Opt-out form for research use of reflection group materials**, in the board's approved heading order, covering only the six material types. It ends with opt-out instructions and *"You do not need to sign or return this form"* — no checkbox, no signature |
| A2 | Co-design sessions were a sixth undescribed method | Rolled into the use-of-materials method as the review recommended. They are one of the six material types in §2 and in Appendix A, and are no longer a separate activity anywhere |
| A3 | Cross-study data-linkage consent is unnecessary | Deleted from Appendix A and from the survey consent form. No linkage language remains anywhere in the package |
| A4 | Each section relevant only to use of coursework | Every section of Appendix A is scoped to the materials. Surveys, interviews, and compensation for them appear only in Appendices B and D |
| B1 | Delete Appendix B (intake/invitation) | Deleted. Its two instrument images went with it; the five images Appendix C needs are preserved |
| C1 | Delete the Appendix C intro paragraph | Deleted — the consent form is the survey's first page. Also fixed while in there: two questions asked about *"weekly reflections from the course"* and *"the course in general"*, course language that does not belong in an out-of-course protocol; they now read "your individual reflections" and "the reflection groups" |
| D1 | Five recruitment scripts, not group-recruitment texts | Appendix D is now the interview consent form; the recruitment texts are Appendix F, rewritten as the five the review asked for. The general / alumni / organization-listserv invitations are deleted |
| E1 | Delete the other-scripts appendix | Deleted. The survey-invitation email survives as F.2; the compensation-sending email is gone, since Appendix G now carries the compensation mechanism |
| F1 | Survey consent should not describe the intake survey; use the given wording | Appendix B's *What Will You Be Asked to Do?* now opens with the review's own sentence: *"Take a confidential, online follow-up survey that will take 10–15 minutes. You may be invited…"* |
| G1 | The interview consent form should not read as group interviews, and should discuss only interviews | Rewritten in the singular — *"Take part in a one-to-one interview"* — with §2 stating explicitly that there are no group interviews. The Benefits, Confidentiality, and Compensation sections now speak only about interviews |

## 3. Changes made without being asked

Three, each traceable to a rule this board has already stated on a sibling protocol.

1. **Gift-card mechanics (Appendix G, §6, §9, and the Compensation section of Appendices B
   and D).** On 2026-08-07 the reviewer required, on IRB #2: payment details on a separate
   instrument never joined to responses; no gift card to University employees; no card over
   $50. IRB #1 was submitted on 08-01, before that ruling, so it carries none of it. The
   accepted IRB #2 v9 language is reused verbatim. Also added: the >$75 tax-reporting
   block, which is now reachable because nine follow-up surveys at $10 totals $90.
2. **An interview guide (Appendix E).** The board's *"Include Appendix with interview
   protocol"* on IRB #2 is a general requirement. The submitted IRB #1 named an interview
   protocol outline in the Appendix G title but contained none.
3. **Confidentiality disclosures the institution's instructions require and the submitted
   version omitted**: IP addresses are not collected; the key file is electronic and
   encrypted; survey data are deleted from Qualtrics within 14 days; transcription is by the
   named investigators with no outside service; identifiable data are accessible only to the
   personnel in §3.

## 4. Deletions

Red markup cannot show what was removed. In full:

- §2 Methods items 1 and 2 (recruitment and consent), items 3–8 as procedures (the intake,
  icebreaker, meeting, video, whole-cohort, professionals, and group-remedy paragraphs — the
  data they generate survives as one-line items), and item 12 (co-design sessions as a
  separate method)
- The comparative-enrolment sentence from Methods item 11 (moved to §4)
- §4: the information-session sentence, the study-webpage sentence, and the group
  recruitment-channel list (the comparison-group channels survive in §4 (4)&(5))
- §5: the whole section, replaced
- §6: the opening reflection-group confidentiality paragraph
- §7: the peer-disclosure risk sentence
- §8: *"but participants may learn and reflect critically … professional networks formed
  through the groups"*
- §9: *"No payments or extra credit are made for participating in reflection groups"* and
  *"(the initiation survey is not compensated)"*
- Appendix A: the co-design bullet, the cross-study linkage paragraph, the group-disclosure
  risk bullet, the group-confidentiality paragraph, and the entire survey / interview /
  meeting content that belongs to other methods
- Appendix B (intake / initiation survey) — the whole appendix, and its two images
- Appendix C: the introductory paragraph
- Appendix D: the general, alumni, and organization-listserv invitations
- Appendix E (other scripts): the whole appendix
- Appendix F: the comparison-participant adaptation note (now handled by the modification)
- Old Appendix G (the interview consent form, now Appendix D): the plural-interview framing,
  and every passage describing surveys, reflection-group activities, or any method other than
  the interview itself
- Two now-stale standalone files moved to `archive/`: `IRB1_ConsentForm_Participation.docx`
  and `IRB1_RecruitmentTexts.docx`, both from 2026-07-23. They contradicted v5 outright

## 5. Verification passes

### Pass 1 — alignment against the submitted version

Every section of the 2026-08-01 package was accounted for as kept, adapted, or deleted;
the deletions are listed above and each traces to a numbered review point. Nothing marked
KEEP in the workflow's sense was dropped: the approved data-management framing (14-day
archiving, key file, five-year deletion, the Fall 2026 → December 2031 example, indefinite
de-identified retention), the approved consent heading order, the approved
checkbox-plus-email affirmation on the survey form, the approved interview-consent skeleton,
and the board-required example statements are all present.

v5 is **8,861 words against 6,617** in the submitted version. It is longer despite three
appendices being deleted, because of what §3 below adds: the gift-card mechanics and
tax-reporting blocks in three places, the interview guide, and five recruitment texts where
there had been three group invitations. The narrative itself is shorter — the service
section went from eight numbered procedures to six one-line items.

### Pass 2 — source coverage

IRB #1 is unfunded (§1 is "N/A"), so the governing source is the study design captured in
`IRB1_SUMMARY.md` and the 2026-07-27 PI meeting. Every activity in that design is still
covered: reflection groups as a service, the materials they generate, longitudinal surveys,
interviews, the comparison group, and the supporting tools. Nothing was added that has no
basis there — the interview-timing examples derive from RQ3 (barriers and enablers) and RQ1
(change over time), and the interview guide's topics map one-to-one onto RQs 1–5.

The comparison group is now *less* covered than in the submitted version, deliberately: its
details are deferred to a modification, at the reviewer's explicit invitation. Nothing can be
recruited for that group until the modification is approved.

### Pass 3 — internal consistency

Checked across the narrative, the three consent forms, the recruitment texts, and the
compensation form:

| Fact | Value | Appears in |
|---|---|---|
| Follow-up surveys | up to nine, over four years, at ~3 and ~6 months then ~every 6 months | §2, §9, Appendix B, F.2 |
| Survey length | 10–15 minutes | §2, Appendix B, F.2 |
| Interview length | 30–60 minutes | §2, Appendix D, E, F.3 |
| Survey compensation | $10 per submitted survey, within 48 hours, $90 maximum | §9, Appendix B, F.2 |
| Interview compensation | $25 per interview, within 48 hours, $50 worked example | §9, Appendix D, F.3 |
| Archiving | within 14 days | §2, §6, Appendices A, B, D |
| Recordings off device | within 72 hours | §6, Appendix D |
| Key deletion | five years after participation ends; Fall 2026 → end of December 2031 | §6, Appendices A, B, D |
| Opt-out window | two weeks from the first session, reversible later | §4, §5, Appendix A, F.1 |
| Group meetings | never recorded, no researcher attends | §2, §6, Appendix A, F.1 |

No mismatches found. The one place a number was newly computed is the $90 nine-survey
total, which is what triggers the tax-reporting block.

### Pass 4 — institutional compliance (findings only; nothing fixed here)

Run against `.claude/skills/irb-writing/references/institutions/umaine.md`.

**Blocking** — the application is returned if these are not right:

1. **The cover page is a separate Word document, and it is not in this repository.** The
   board requires two attachments: the cover page alone, and the narrative plus all
   appendices as one Word document. v5 is the second of those. Whatever cover page went with
   the 08-01 submission needs to go with this one.
2. **Submit the `.docx`, not a PDF.** `CURRENT/IRB1_Protocol_v5_ORA_RESPONSE.docx`, with the
   red resolved. The `_MARKED` file is for review only.

**Non-blocking, but worth a decision:**

3. **The secure cloud platform is named "Google Drive" in §6.** The institution's
   instructions require the vendor named, and the sibling protocol under review at this
   board names Google Drive, Qualtrics, and Zoom in exactly this way. It was carried across
   on that basis. If IRB #1 in fact uses something else, §6 and Appendix D need the real
   name. This is open item 2a in `IRB1_SUMMARY.md`, still open.
4. **No concise summary.** Required by the checklist for consent forms over one page. No
   approved form in this program has ever carried one, and IRB #1 is unfunded, so only the
   length trigger applies. Reported as unverified, not as a violation.
5. **Reading level.** Consent forms must read at or below 8th grade. Appendix A and the
   plain-language compensation paragraphs are written to that; the retention paragraphs
   inherited from approved language are denser. They are approved language, so they were
   left alone.
6. **Students and employees of the University are an undue-influence population** the
   instructions ask to be named and justified. §4 carries the grades sentence for
   course-recruited participants; the protocol does not otherwise discuss the
   supervisor–supervisee case that `IRB1_SUMMARY.md` open item 8 raises.
7. **Conflict, recorded rather than resolved.** The board's own §5b rule says group sessions
   need the cannot-guarantee-confidentiality statement in both the narrative and the consent
   form; this review ordered exactly that statement deleted from IRB #1, because these groups
   are not research. The review wins for this protocol. IRB #2 and IRB #3 keep the statement,
   and should — their group sessions *are* research.

## 6. Open items for the PI

1. **Comparison-population consent forms and details.** v5 defers all of it to a
   modification, which the reviewer explicitly offered. If the mode, length, timing, and
   instruments already exist, saying so now avoids a second review cycle later. Deferring is
   the faster path to approval on this round.
2. **December 2035 as the final gift-card date, and December 2036 for the last audio
   recording.** Both are derived: roughly five years of recruitment from 2026, plus the
   four-year follow-up window, plus the five-year key-file life for the recordings. Given
   dates must be adhered to once stated — confirm or replace them.
3. **Transcription by the named investigators.** Stated as fact in §6 and Appendix D. If a
   transcription service is ever wanted, it has to be in the protocol before it is used.
4. **The two-week opt-out window.** A drafting choice, not something the review specified.
   Longer is friendlier; shorter archives sooner.
5. **The three files in `CURRENT/protocol-candidates/`** are now two versions behind and
   still unarchived. `WHICH-IS-LIVE.md` says the call is yours.
