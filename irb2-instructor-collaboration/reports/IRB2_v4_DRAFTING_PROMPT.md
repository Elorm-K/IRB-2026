# Drafting prompt — IRB #2 v4 (Instructor Collaboration + GenAI co-design)

Paste this as the task prompt in a fresh session. It is self-contained except for the file paths, which must be readable.

---

## TASK

Produce **`IRB2_Protocol_InstructorCollaboration_v4.docx`** — a complete, submission-ready UMaine IRB application narrative (Sections 1–9) plus all appendices, superseding v3_aligned.

Also produce:
- `IRB2_ConsentForms_v4.docx` — standalone copies of every consent form appendix (the existing standalone file is stale v1 text; regenerate it, do not edit it)
- `IRB2_RecruitmentTexts_v4.docx` — standalone copies of the recruitment appendices
- `IRB2_v4_CHANGELOG.md` — every change, one line each, in the form: `§/Appendix | what changed | why (source + citation)`

Write the full document. Do not produce a diff, a summary, or a list of suggested edits.

---

## SOURCES, IN PRIORITY ORDER

When two sources conflict, the higher one wins. State in the changelog whenever you resolve a conflict.

1. **The Google Doc comments** (three open threads, transcribed verbatim in §C below) — these are the PI's and Cyril's most recent explicit instructions.
2. **The live Google Doc hand edits** — `https://docs.google.com/document/d/1RtTxaxVy70cO8ss9HY1C8d_iYZ29XFA2gOveEET16a0/edit`. Read it with the Google Drive tool using `includeComments: true`. **This doc is a fork of v2, not a descendant of v3** — see §B for the exact merge rule. Do not blindly diff-and-overwrite.
3. **The grant — the authority on scope.** `inputs/grant/FINAL NSF_CAREER_25_Nelson.pdf`. Per the 2026-07-22 advisor meeting: *"So just basically everything that's in the grant already. You don't have to figure it out. It's already all planned. Just doing that."* **Every activity, population, measure, and timeline in v4 must be traceable to a grant section, and the changelog must cite it** (e.g. "grant §3.1.4, p.8"). If you cannot find grant support for something already in the draft, flag it rather than silently keeping it.
4. **v3_aligned** — `irb2-instructor-collaboration/archive/IRB2_Protocol_v3_aligned_2026-07-25.docx`. The richest base text. Start here.
5. **IRB #1** — `irb1-reflection-groups/CURRENT/protocol-candidates/IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx` (project root). Source for generic wording to port across; see §D.
6. **The approved course protocol + mods** — `inputs/approved-protocols/2024_08_09 Nelson_MOD_2_Jan_2026_FINAL.pdf` (see Appendix P for the board-accepted consent skeleton) and `course-protocol-mod/CourseProtocol_AppendixA_DataLinkage_MARKED.docx` (board-facing data-linkage language). **House style and consent-form format come from these. Do not invent a new consent format.**
7. **The gap analysis** — `irb2-instructor-collaboration/reports/IRB2_GapAnalysis_vs_CAREER_grant.md`. Findings to fix, not instructions to follow literally; the sources above override it.
8. **Advisor meeting transcripts** — `inputs/meetings/Advisor Meetings transcript_2026-07-22*.txt`. The IRB-relevant content is extracted in §E; the four files are near-duplicate recordings of one meeting, so §E is sufficient and you need not re-read them.

---

## A. THE ONE DECISION THAT CHANGES EVERYTHING — RESOLVE FIRST

Google Doc comment 1 (Cyril, anchored on the §2 Summary phrase *"alongside evaluation of reflection groups deployed in collaborating instructors' courses"*) says:

> "Beyond participating in the design workshops will not like obligate the instructors to use reflection groups in their classes. It also won't obligate them. Instructors might use reflection groups in their classes without participating, without having their course and their students participate in research on reflection groups. We will offer in the future to instructors an option to participate to, you know, invite their students to participate in research for the reflection groups, **but we will submit a modification or a separate IRB before doing that.**"

Read literally, this **removes the entire student / classroom-deployment stream from IRB #2** — v3's §2 items 7–12, the student population in §4, and Appendices F, G, H, I, J, and K — deferring all of it to a later modification. That would reduce IRB #2 to instructor-facing research only: survey, interviews, co-design workshops, consultation notes, longitudinal instructor follow-up.

**Do not choose for the user.** Open the draft with this block and build the rest to match whichever option is selected:

```
{your input needed here — SCOPE DECISION, must be resolved before submission:

 Option A (narrow — what Cyril's comment says literally): IRB #2 covers instructor-facing
 research only. Sections 2 items 7-12 and Appendices F-K are removed and deferred to a
 modification or separate IRB submitted before any student data are collected in a
 collaborating instructor's course. Fastest to approve; unblocks the fall 2026 co-design
 workshops immediately; requires a second submission before any fall classroom deployment.

 Option B (broad — what v3_aligned currently does): IRB #2 covers instructor research AND
 classroom deployment in collaborating courses, with the student protections already drafted.
 One submission covers fall 2026 deployment, but is a larger review and the board may hold
 the whole thing over questions about the student stream.

 Option C (staged in one document): submit the instructor stream as active, and include the
 student stream explicitly marked as not yet activated, to be enabled by modification once
 the first co-design cycle defines the design. Requires the board to accept a conditional
 section.

 Recommendation: Option A, because it matches the comment, matches the advisor meeting
 priority ("do that IRB thing, it's blocking everything else"), and the grant does not
 require student deployment data until the fall 2026 courses begin. If Option A is chosen,
 write the deferral sentence into Section 2 so the board sees the boundary explicitly.}
```

Then **draft the full document under Option A**, and supply the removed student stream as a clearly labelled appendix at the end of the file — `HELD FOR MODIFICATION: student / classroom-deployment stream (v3 Appendices F–K, revised)` — carrying all the fixes in §D and §F so it is ready to submit as the modification without a second rewrite. That way neither option requires redoing work.

---

## B. MERGE RULE: v3_aligned base + Google Doc overrides

Start from **v3_aligned**. Then apply each of these Google Doc edits as an override, because they are the team's later decisions. Keep everything else from v3_aligned (the Google Doc lacks it only because it forked from v2).

| # | Apply this Google Doc edit | Over this v3_aligned text |
|---|---|---|
| B1 | §2 item 3: *"Instructors are invited to co-design workshops to shape **a) reflection-group designs, and/or b) generative AI integration.** This includes for their courses and institutions, identifying challenges and barriers to adoption, and proposing designs and improvements."* | v3's reflection-groups-only phrasing. **This is the team's own AI-scope hook — build §F outward from it, keeping their a)/b) structure.** Clean up the grammar ("This includes for their courses" → "including for their courses"). |
| B2 | §2 item 3: *"An initial round is anticipated in **fall 2026**, repeated each design cycle, and also including roughly yearly adoption-cycle workshops."* | v3's *"anticipated in August 2026 … until the design stabilizes (expected by the end of Year 2 or 3 of the grant)"*. Drops a month-specific date that may precede approval, and drops grant-internal milestone language. Also remove the duplicate "August 2026" from the §2 Methods preamble. |
| B3 | §2 item 6 heading: **"Faculty adaptation."** | v3's *"Faculty "spin-offs.""* |
| B4 | Appendix C: *"Workshops are held **online**, facilitated by the research team…"* | v3's *"held online via Zoom [PI DECISION NEEDED: confirm workshop length…]"*. Venue de-named and the marker cleared — apply this pattern everywhere (§F, item 4). |
| B5 | §6: *"all data will be stored on a University of Maine Google Drive"* — **no folder title** | v3's *"…Google Drive **titled "Reflection Groups"**"*. Then apply §D5 on top. |
| B6 | Appendix L: *"(**reviewed** by that institution's IRB)"* | v3's *"(review by that institution's IRB)"* |
| B7 | Appendix K icebreaker: the short form, without the two verbatim example questions | v3's long form quoting *"If you could change anything about the way you were raised…"* and *"Take a minute and tell your teammates your life story…"*. Keep the mitigation, drop the quotes. |
| B8 | All `[PI DECISION NEEDED: …]` markers deleted | v3 still carries four. Convert each to `{your input needed here — …}` per §G, do not simply delete. |

**Keep from v3_aligned** (the Google Doc predates all of it — do not lose it): the full award identifier and start date in §1; interviews *"audio-recorded only (no video is recorded)"* in §2 item 2 and Appendix D; the instructor interview Compensation paragraph in Appendices A and D; the *"Other scripts (email templates)"* block in Appendix E; Cyril's *"PhD Student"* title in §3; the English-comfort item in Appendix H; the expanded core reflection questions in Appendix K.

---

## C. THE THREE GOOGLE DOC COMMENTS — VERBATIM, WITH WHAT TO DO

**C1 — Cyril, on §2 Summary, anchored to *"co-design workshops with instructors, surveys and interviews about barriers and benefits, and consultation notes are collected and analyzed to understand what makes reflection groups adoptable, alongside evaluation of reflection groups deployed in collaborating instructors' courses."***

> "Beyond participating in the design workshops will not like obligate the instructors to use reflection groups in their classes. It also won't obligate them. Instructors might use reflection groups in their classes without participating, without having their course and their students participate in research on reflection groups. We will offer in the future to instructors an option to participate to, you know, invite their students to participate in research for the reflection groups, but we will submit a modification or a separate IRB before doing that."

**Do:** (a) resolve the scope decision per §A; (b) regardless of which option is chosen, add an explicit **no-obligation** paragraph to §2 and to Appendix A, stating three separable choices — attend workshops; adopt the materials in your course; have your own or your students' data used in research — and that declining any one has no effect on the others or on the team's support. v3 has a weaker version of this (*"Working with us is separate from being in the research"*); the comment asks for the three-way separation to be explicit. Mirror IRB #1's service-first framing (§D1).

**C2 — Greg, on §2 item 4, anchored to *"an instructor may ask that any session be struck from the research record"***

> "rephrase to be not session level but part of the session; recorded or not recorded with handwritten notes"

**Do:** rewrite the consultation clause in §2 item 4, Appendix A's fourth bullet, and the Appendix C verbal script so that (a) an instructor may ask that **any part of a session**, not only a whole session, be struck from the research record; and (b) it is stated that consultations are **not recorded** — the PI takes notes, which may be handwritten, and handwritten notes are transcribed/stored under the Section 6 procedures. Update the verbal script to say this in plain language.

**C3 — Cyril, on Appendix E, anchored to *"(Nelson et al., 2025)"***

> "Should we replace all of these with the FIE paper?"

**Do:** this is a citation decision the user must make. Insert:

```
{your input needed here — citation: replace the Nelson et al. (2025) OSF preprint
(https://osf.io/wqk85) with the FIE paper throughout? If yes, supply the full FIE
citation and confirm whether it replaces the preprint in all locations — Section 2
Summary, References, Appendix E mailing-list blurb, Appendix E targeted email,
Appendix K, and Section 8 Benefits — or only in the participant-facing recruitment
texts. The transcript notes the FIE reflection-groups paper exists
(transcript 2026-07-22, 11:02).}
```

Leave the existing citation in place next to the placeholder so nothing breaks if the answer is no.

---

## D. GENERIC WORDING TO PORT FROM IRB #1

Take these from IRB #1 because they are already written in board-facing language and are generic enough to apply to IRB #2. **Adapt the nouns** (participant → instructor/student, participation cycle → semester or collection date) and keep the sentence structure. Do not import IRB #1's out-of-class-specific content.

**D1 — Service-first / research-is-separate framing.** IRB #1 §2: *"The reflection groups and reflection activities are offered as an ongoing service to participants and would be offered regardless of this research; this protocol governs the research use of data generated by that service, plus research-specific activities (surveys, interviews, and comparison groups)."* → Adapt for IRB #2: the collaboration, materials, workshops, and consultation support are offered regardless of the research; this protocol governs research use of the data those activities generate. Directly answers comment C1.

**D2 — Define "outcomes" once, then use the word.** IRB #1 §2: *"For the purposes of the research "outcomes" below refers to: professional skills & dispositions, learning, career, and other personal and social outcomes. For example, professional skills (such as iterative improvement, lifelong learning, psychological safety, and communication), self-efficacy, professional identity, and other personal, professional, and group outcomes."* → Put this in IRB #2 §2 **and extend it to cover critical and reflective generative-AI use**, per the grant's Overview and §3.2.4. Then replace every re-enumeration with the single word "outcomes": §2 Research Questions, §2 survey items, §8 Benefits, Appendix H heading, Appendix I, and the consent forms. IRB #2 currently uses the term "outcome measures" without ever defining it, and enumerates a different subset in each of five places.

**D3 — Bounded longitudinal schedule.** IRB #1 §2 item 9 and Appendix F: *"…approximately 3 months and 6 months later, and then approximately every 6 months, for up to four years after group initiation (**up to 9 follow-up surveys total**)."* → Keep IRB #2's *"roughly every 6 months … up to 4 years (8 surveys total)"* but adopt the "up to" bounding so a missed wave is not a deviation.

**D4 — Original recordings are deleted; only de-identified data are kept forever.** IRB #1 Appendix G: *"The archived data will be retained indefinitely, **except for the original audio recordings, which will be deleted at the same time as when your email address is deleted from the key file**, five years after your participation ends. For example, if your participation ends in Fall 2026, the audio recordings will be deleted by the end of December 2031."* → Port into IRB #2 §6, Appendix A, Appendix C (workshop recordings), and Appendix D. **Required, not cosmetic:** IRB #2 currently promises only that *"de-identified data [are] retained indefinitely"*, and a voice recording cannot be de-identified.

**D5 — De-named storage platform.** IRB #1 §6: *"All data for the study will be stored in a **cloud data platform that encrypts all data at rest and in transit with AES-256 bit encryption and is password protected**."* → Use this in IRB #2 §6 in place of the named Google Drive, keeping one parenthetical mention of the university-managed platform if the board expects a named system. Apply the same rule to Qualtrics ("a secure survey platform that encrypts data in transit and at rest and is access-controlled") and to Zoom ("online", or IRB #1's *"online (for example, Zoom) or in person, based on your preference"*).

**D6 — Optional data-linkage consent.** IRB #1 Appendix A: *"You may optionally give consent for the research team to link your data from this study with data from prior or related reflection-group research studies led by this research team in which you participated and consented to research use of your data (for example, reflection groups in a prior course), to help understand your experience and outcomes over time."* Plus the matching Confidentiality paragraph, and from the data-linkage mod: *"These related studies address the same research questions and use the same outcome measures, and any linked data receive the same protections described in this section."* → **IRB #2 has no linkage provision anywhere.** Add to §5, §6, Appendix A, and (if Option B/C) Appendices F and I. Also add the revocation clause: *"This includes revoking consent for linking your data with prior related studies."*

**D7 — Affirmation block.** IRB #1 Appendix G ends with: *"Your choice below indicates that you have read the above information and agree to participate. You will receive a copy of this form."* / `☐ I consent to being part of this study` / `_____ Email`. → Add to every signed consent form in IRB #2 (Appendices A and D, plus F if in scope). None currently has one, though §5 says consent is obtained electronically.

**D8 — Total time commitment, with a worked example.** IRB #1 Appendix G: *"The total time commitment is variable based on the interviews you sign up for. For example, if you participate in an interview now and one after each of the next two participation cycles, that would be a total of 1.5–3 hours, but you can sign up for fewer interviews."* Approved Appendix P: *"The total time commitment is approximately 10-15 minutes for each longitudinal follow-up survey. Beyond that, you will just participate in the class as usual."* → Add a total-burden sentence to Appendix A (which currently gives a duration for the survey only, and none for interviews, workshops, or consultations) and to Appendix F if in scope.

**D9 — Power/coercion paragraph structure.** IRB #1 §4 handles advisor/supervisor coercion explicitly. IRB #2's instructor version exists in §4 ¶3 and is good — keep it, and extend it with the three-way no-obligation separation from comment C1.

**D10 — Comparison-participant adaptation pattern.** IRB #1 Appendix F closes with a compact adaptation note ("the same consent statement is used, with the purpose sentence reading …"). IRB #2 Appendix I already uses this pattern — keep it; use the same pattern for any new AI-activity adaptation rather than duplicating whole forms.

**D11 — Consent comes first in the participant flow.** IRB #1 orders its Methods items with **Consent as item 2**, before intake and matching. IRB #2 puts "Deployment" (which includes the matching survey that collects gender and disability status) at item 7, *before* "Student consent" at item 8. Reorder so consent precedes any data collection in every stream, instructor and student. For instructors, state that Appendix A is completed before the first workshop from which data are analyzed.

**D12 — Consent-form section order and format.** From approved Appendix P and IRB #1: Researchers list → invitation paragraph → *What Will You Be Asked to Do?* → *Risks* → *Benefits* → *Confidentiality* → *Compensation* → *Voluntary* → *Contact Information* → affirmation block. Each is a **heading on its own line with body text below** — not the inline `Risks: …` one-liner style that IRB #2 Appendices B and I currently use. Rebuild B and I to the full skeleton. Add a *Compensation* section to Appendix F, which currently buries the $10 offer in a bullet.

---

## E. DECISIONS FROM THE ADVISOR MEETING (2026-07-22)

Use these; they are already extracted, so you need not re-read the transcripts.

| Source | Quote | Apply to |
|---|---|---|
| 10:52:17–10:52:48 | *"there should be a line of IRB for work … That's not involved in classes at all. Then there should be an IRB that is … working with instructors and or people at other institutions to do … work in their classes. Uh, including first design workshops, which is … in the research, like **to do a design workshop with instructors, is research. So that needs to be included in the IRB.**"* | Confirms the two-protocol split and that co-design workshops are research, not exempt planning. State the IRB #1 / IRB #2 boundary in §2, and keep workshops as consented research. |
| 10:52:51 | *"So just basically **everything that's in the grant already**. You don't have to figure it out. It's already all planned. Just doing that."* | The grant is the scope authority. Cite a grant section for every activity in the changelog. |
| 10:50:24–10:50:39 | *"we should target having like **10 faculty members** to work with … implementing reflection groups in their classes **in the fall**. To do that, we'll need to recruit **at least 25** people. And to recruit 25 people, we're going to send out messages to **several hundred** people. So we can send out messages to the **CCSE mailing list**, other things like this."* | Source of §4's funnel numbers — they are real PI targets, not invention. **But** the gap analysis recommends the board sees only the total range. Keep *"approximately 50–100 instructors over the protocol's duration"* in §4 and move the funnel to a bracketed note the user can restore: `{your input needed here — include the recruitment funnel (contact several hundred → recruit ≥25 → ~10 implementing in fall 2026) in Section 4, or keep only the 50–100 total? The funnel is a real PI target from the 2026-07-22 meeting but will drift within a semester.}` |
| 10:50:15, 10:51:59 | *"just get the IRB done as soon as possible … do that IRB thing, **it's blocking everything else**."* | Bias every judgment call toward what the board approves fastest: fewer named tools, broader ranges, no unresolved markers, no speculative future activities in the active sections. |
| 11:32:40 | *"Being able to have the IRB approvals and people **opt in where they can** … so that we're able to call it research."* | Opt-in consent for research use, service delivered regardless. Reinforces D1. |
| 10:53:12–10:53:18 | *"within class reflection groups stuff. I mean, we made a mistake. And thinking that those things weren't approved before, but they are, so we can just send them out."* | Existing approved course protocol already covers the team's own courses and their longitudinal surveys. Do not duplicate that coverage in IRB #2 — keep the boundary sentence pointing at it. |

---

## F. THE GENERATIVE-AI WORK — BUILD OUT FROM THE TEAM'S OWN HOOK

The Google Doc already opens the door (edit B1: *"a) reflection-group designs, and/or b) generative AI integration"*). The title has always said *"…Including Critical and Reflective Use of Generative AI…"* while the body has been reflection-groups-only. Close that gap.

> **[Update 2026-07-28, after this prompt was run]** This constraint no longer applies. The file is now in the repo at `inputs/approved-protocols/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` and opens fine. If you re-run this prompt, **delete the two bullets below and copy the approved language instead**: Appendices P, Q, and R MOD Jan/26 of that protocol are the board-approved AI consent forms (participation-without-interviews, bi-weekly interview, follow-up interview).

**Read this constraint first.** The user's note says the AI consent language can be inferred from "the IRB on AI." That document — `/Users/cyril/Downloads/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` — **could not be opened** (macOS blocks tool access to `~/Downloads`; it is also a different protocol number from the two local reference PDFs, and neither local PDF mentions generative AI, video reflection, or interviews at all). So:

- **Derive** the AI language from the grant (§3.2, §3.2.2, §3.2.3, §3.2.4, §3.2.5, §3.3.3) plus IRB #1's consent skeletons.
- **Mark every derived AI passage** with a trailing `{your input needed here — verify against the approved AI protocol (2023_07_10 … MOD Jan 2026); this wording is derived from the grant, not copied from the approved form. To have it copied instead, move that file out of ~/Downloads (e.g. to the project folder) and re-run.}`
- Put **one** such marker per appendix, not one per sentence.

**Where to add AI scope** (each with its grant citation):

| Location | Add | Grant support |
|---|---|---|
| §2 Summary | Second sentence covering instructor adoption of reflection-on-GenAI-use pedagogies alongside reflection groups | Overview T1/T2; §3.2.3 |
| §2 Research Questions | Broaden RQ1 and RQ2 to "reflection-group and GenAI-reflection pedagogies"; add critical/reflective GenAI use to RQ3's outcome list | Overview; §3.2.4 |
| §2 item 3 (workshops) | Keep the team's a)/b) structure; add that workshops co-design **AI course materials and GenAI-reflection assignments** | §3.1.2; §3.1.4 *"we will also include **two to three modules on critical GenAI use**"*; Education plan Activity #2 |
| §2 item 1 (survey) + Appendix B | Parallel items on interest in, and barriers to, integrating GenAI-reflection assignments | §3.2.3 *"once successful, recruit faculty from other institutions to adopt that reflection assignment"* |
| §2 item 5 / item 6 | Instructor longitudinal follow-up and faculty adaptation cover both pedagogies | §3.1.2; §3.2.3 |
| Appendix C | Workshop purpose covers reflection-group designs **and** AI course-material / GenAI-integration design | §3.1.2; §3.1.4 |
| Appendix D | Interview guide items 2, 3, 6, and 8 get a parallel GenAI-reflection clause | §3.2.3; §3.2.4 |
| Appendix E | Recruitment texts mention both offers, since the grant recruits faculty for both | §3.2.3 |
| Appendix A | *What Will You Be Asked to Do?* covers co-designing both | — |
| Appendix K (if Option B/C) | Topic modules including two to three on critical GenAI use; **and fix the exclusion sentence** — v3's *"only responses to the five core questions are collected and analyzed under this protocol"* writes the grant's GenAI modules out of the protocol. Change to cover core **and module** reflection responses. | §3.1.4 |
| Appendix H (if Option B/C) | Add critical/ethical GenAI-use self-efficacy and GenAI-use items to the outcome measures | §3.2.4 *"the ChatGPT Literacy scale, and the PI's short four question critical and ethical GenAI use self-efficacy measure"* |

**Boundary sentence — required.** IRB #2 must not silently absorb Task 2 or Task 3. Add to §2, with a placeholder:

```
{your input needed here — protocol boundary: the grant states (§3, p.6) that "All preliminary
work already has IRB approval, which was written broadly such that it also already covers the
proposed work in Task 1 and 2." Confirm which approved protocol covers (a) student
video-assisted comparative reflection on GenAI use and the screen-recording data
(grant §3.2), (b) GenAI IDE/agent log data (§3.2.2 stretch goal), and (c) the mock-workplace
GenAI agent-building assignment (§3.3.3). This protocol will state that those student-facing
activities are covered elsewhere and are not conducted under it — but the sentence needs the
correct protocol title and number.}
```

**Do not add to IRB #2** (record in the changelog as deliberately excluded, with the reason): student screen-recording / video data and the video anonymization platform (grant §3.2.5); GenAI IDE log data (§3.2.2); the mock-workplace agent assignment (§3.3.3); the paid professional comparison panel (§3.2.4 — IRB #1 explicitly disclaims a recruiting company, so this belongs to neither protocol and needs its own decision); the education-plan hackathons, community group, and high-school outreach (grant §4 states these *"will not be conducted as research activities for this proposal"* — add a one-line non-research boundary sentence like IRB #1's).

---

## G. FIXES TO CARRY IN (from the gap analysis, verified against sources)

Apply all of these. Cite the source in the changelog.

**Must fix before submission**
1. **Interview compensation contradiction.** §9 says instructors get **$10** *"matching the compensation offered for interviews under the team's companion out-of-course reflection-groups protocol"* — but IRB #1 §9 says **$25**. Two protocols to the same board, contradicting each other, with one asserting they match. Insert `{your input needed here — set the instructor interview payment: $10 (current IRB #2 text) or $25 (IRB #1's amount for interviews)? Whichever is chosen must match across IRB #1 §9 and IRB #2 §9, Appendix A Compensation, and Appendix D Compensation; delete the "matching the compensation" clause unless the amounts actually match.}` and use one amount consistently in the draft.
2. **Recording deletion** — D4. Required for approvability.
3. **Data-linkage consent** — D6. Absent from IRB #2 entirely.
4. **Define "outcomes" once** — D2.
5. **Consent before data collection in every stream** — D11.
6. **Clear all four `[PI DECISION NEEDED]` markers** as `{your input needed here — …}`: workshop length (§2 item 3 and Appendix C — propose a broad range, e.g. "approximately 1–2 hours"); mid-semester course withdrawal handling (§2, if Option B/C); the adapted icebreaker question list (Appendix K, if Option B/C); the funnel-numbers question (§4, per §E).
7. **Regenerate the standalone appendix files.** The existing `IRB2_ConsentForms_Instructor_and_Student.docx` is still **v1** text — old protocol title, `cyril@yesslab.org`, Chris Dufour missing from the roster, and a live `[PI DECISION NEEDED: final researcher list for consent form]` inside it. If that file is what gets attached, the submission contains an unresolved marker. Regenerate from v4; do not edit in place.
8. **Personnel completeness.** §3: Cyril has Roles but no *Experience* line, unlike the PI, Troy, and Chris. Add it, plus `{your input needed here — Cyril's Experience line, and CITI completion dates for all four personnel if the board expects dates}`.
9. **Student consent must disclose the matching survey** (if Option B/C). Appendix J collects availability, **gender, and disability status**, and Data collected 1.5 lists them as research data — but Appendix F never mentions the matching survey, gender, or disability. Add the bullet and a Confidentiality sentence that these are never disclosed to peers, the host instructor, or teaching assistants. Either give Appendix J its own consent statement or sequence it explicitly after Appendix F.
10. **Restore the approved career-event survey items.** The approved protocol's Appendices K and L already carry them (*"been invited to a screening/shorter phone, video, or other interview"*, *"done a job interview"*) and the grant requires them (§3.1.5: *"self-reported objective career events like obtaining internships, interviews, and jobs … and degree completion"*). Dropping items the board already approved is a pure loss.
11. **Data access for collaborating and adapting instructors.** §6 says data are *"accessible only to the research team"*, while §2 item 6 lets instructors adapt the design and evaluate their own students. State that collaborating instructors receive no identifiable research data, and that any instructor analyzing their own students' data is either added to this protocol as personnel with CITI training or operates under their own institution's approval.
12. **Total expected N.** §4 gives per-course numbers only; the approved protocol states a total (*"approximately 300-500 students over five years"*). Add `{your input needed here — total expected participant N over the protocol's duration}`.

**Add where grant-supported** (keep each to one or two sentences; do not let these balloon the document)
13. Reflection-quality rubric analysis — grant §3.1.5 (Kember three-category rubric plus a medical-education rubric). IRB #2 collects reflections but never says how they are analyzed; add Kember et al. (2000) to References (it is already in IRB #1's list).
14. Allowance for measure iteration — grant §3.1.5: *"In Year 1 we will pilot on the pre and post course surveys a wider variety of measures."* One sentence in Appendix H permitting additions, substitutions, and removals within the same outcome constructs, with substantive changes submitted as a modification.
15. UMaine's own other tech-ethics course as a comparison — grant §3.1.3: *"our institution has another tech ethics course in the other semester; we will recruit and survey in the other instructor's course."* v3's §2 item 11 reads external-only (*"Where a collaborating institution offers…"*); change to include the University of Maine.
16. Comparison students are also invited to longitudinal follow-ups — grant §3.1.3 (*"and longitudinally"*). v3's *"recruited for the surveys only"* reads as pre/post only.
17. Student and alumni interviews (if Option B/C) — grant §3.1.3, §3.1.5, §3.1.6, including *"show relevant work-products"* as a distinct data type. Needs a data row and a consent form built on IRB #1 Appendix G.
18. Broader recruitment channels once the design succeeds — grant §3.1.2: *"the PI will advertise and recruit faculty more broadly."* Add public announcements, a project website, and social media to §4 (IRB #1 already permits social media).
19. In-class student co-design session and end-of-semester retrospective (if Option B/C) — grant §3.1.2.
20. Mid-course formative feedback (if Option B/C) — grant §3.1.4.

**Trim (approvability test: if the detail would not change whether the study is approved, cut it)**
21. De-name tools and venues per D5 — Qualtrics (4 places), Zoom (5 places), Google Drive plus its folder title. Keep the *security property*, drop the brand. Keep "$10 electronic VISA gift card" — that exact phrase is in the approved forms.
22. Appendix C's six-item workshop agenda with per-item minutes (*"Introductions and study context (5–10 minutes)"* …). Co-design participants will rewrite it in session one, and none of it affects approval. Cut to three sentences: purpose, ground rules (**keep the ground rules verbatim — they are a participant protection**), and data collected. Google Doc edit B4 already started this.
23. State the student protections **once**. v3 enumerates the same four (course activity happens regardless; consent never administered by the host instructor; instructor blind until final grades; no grade effect) in full in §2 item 8, §4 ¶3, and §7 ¶3. Keep §4's version; cross-reference from the others.
24. Cut §7's restatement of §6's de-identification chain (*"participant emails are replaced with a randomized unique identifier … no later than 14 days"*) down to "mitigated by the de-identification and storage procedures in Section 6." Keep the chain in the consent forms, where participants need it.
25. Strip the repeated four-item barrier example list (*"class time, grading load, curriculum constraints, departmental expectations"*) from all but one location — it currently appears in §2, Appendix B item 6, Appendix D item 3, and Appendix E.

**Do not cut** — flagged so you do not "improve" these away:
- Appendix H's full instrument item text. The approved protocol attaches full instruments and the board reviews item wording for sensitive content.
- The §6 *"In summary, the following data … will be retained indefinitely"* recap. It duplicates the Data collected list, but `IRB2_SUMMARY.md` records it as deliberately restored to match the board-accepted Section 6.
- The Appendix C consultation verbal-confirmation script. It *is* the consent mechanism for consultation notes — revise it per comment C2, do not remove it.
- The §6 right-to-withdraw paragraph and the Appendix A–L lettering with no gaps. Both were deliberately fixed in v3.

---

## H. HOUSE STYLE AND OUTPUT RULES

- **Sections 1–9 in the UMaine order**, with the exact headings v3_aligned uses. Appendices lettered consecutively with no gaps; if Option A removes Appendices F–K, re-letter the remaining ones and update every cross-reference.
- **Every consent form** follows the D12 skeleton with headings on their own lines, ending with the D7 affirmation block.
- **Numbers must agree everywhere.** Before finishing, verify each of these is identical in every location: survey length; interview duration; workshop duration; group size; longitudinal count and interval; the 14-day archiving window; the 5-year key-deletion window and its worked example (Fall 2026 → end of December 2031); every compensation amount. List the check results at the end of the changelog. The only known conflict today is the $10/$25 interview payment (§G1).
- **`{your input needed here — …}`** is the only placeholder form. Always include enough context that the user can answer without reopening the sources: what is being asked, what the options are, and what you recommend. Never leave a bare `{your input needed here}`. Do not use `[PI DECISION NEEDED]`, `TBD`, `TODO`, or `XXX`.
- **Collect every placeholder** into a final section titled `INPUT NEEDED — resolve before submission`, numbered, each with a one-line restatement and a page/section pointer.
- Preserve v3's typographic conventions: curly quotes and em dashes, "de-identified" hyphenated, en dashes in ranges (10–15 minutes), "Section 6" not "§6" in body text.
- Do not add citations that are not in the grant's bibliography or already in IRB #1's or the approved protocol's reference lists. If a new source is needed, flag it as input needed.
- **Do not modify** any source file: not v3_aligned, not IRB #1, not the reference PDFs, not the Google Doc. Write new files only. Do not push anything back to Google Docs.

## I. FINISH BY REPORTING

1. Which scope option (§A) the draft was built under, and where the alternative content is parked.
2. Every Google Doc override applied (§B) and every comment resolved (§C), each with the resulting text.
3. Anything in the grant you judged out of scope for IRB #2, with the reason.
4. The numeric consistency check results (§H).
5. Everything you could **not** verify — especially any AI wording derived from the grant rather than copied from the inaccessible approved AI protocol.
