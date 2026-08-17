# IRB #3 — audit of the Google Doc against ORA feedback (2026-08-17)

Source audited: Google Doc "Developing Professional Skills Including Critical and
Reflective Use of Generative AI in Computing Education"
(`docs.google.com/document/d/1evcxa_HrsjqH7PlaSCmaED_CoEMaDp9wz6oBimoR8Pg`), read
2026-08-17.

Legend: **DONE** = the correction is in the doc. **FLAG** = not in the doc (or only
partly), with what to add. Six substantive items and seven smaller ones are flagged.

> **Read this first.** Six of the flags below are already written and approved-style in
> `irb3-instructor-adoption/source/protocol_v2_ORA_RESPONSE.md` in this repo, but are
> absent from the Google Doc — the Doc looks like a hand-edited copy that diverged from
> the v2 draft. Rather than re-writing those six, copy them across from the v2 source
> (line numbers given per item).

---

## Methods

**1. Survey confidential; online or paper; which platform.**
**DONE (with a one-word gap)** — Methods item 1 now says "a confidential survey" and
"administered via qualtrics."
**FLAG (minor):** the word *online* is never stated in Methods item 1; Qualtrics implies
it but the reviewer asked explicitly. Fix: "a confidential online survey … administered
via Qualtrics; there is no paper version."

**2. Workshops — specify Zoom.**
**DONE** — Methods item 2 states "Workshops are held online via zoom."

**2. Workshops — recordings, and whether agreement to record is required.**
**DONE** — item 2 states each workshop is recorded with webcam video deleted, and that
because these are group sessions "participants must agree to the recording in order to
take part," plus deletion-on-request.

**3. Consultations — will you collect copies of instructor materials.**
**DONE** — item 3 states that with the instructor's permission the team may keep copies
of teaching materials referred to or shared in the session, handled under Section 6.

**3. Consultations — online via Zoom and/or in person.**
**DONE** — item 3 states "Consultations are held via zoom" (Zoom-only), and Appendix A's
consultation bullet matches.

**4. Follow-ups — same procedures, or a future modification; frequency.**
**DONE** — item 5 states follow-ups use the same procedures as the initial
surveys/interviews, points follow-up interviews at Appendix E, and caps frequency at one
follow-up survey and one follow-up interview per semester.
**FLAG (minor):** the data-collected list still reads "(Appendices D and Li8)" — "Li8"
is a broken reference. Also, Methods 5 sends follow-up surveys to Appendix D, which is
titled the *interest and barriers* survey; either retitle it or add the follow-up
instrument as its own appendix (the v2 source added it as Appendix F).

---

## Recruitment

**1. Other UMS campuses besides UMaine/UMM (answer in the separate email chain).**
**NOT A DOC CHANGE — still owed.** Nothing to correct in the protocol; this is your
email reply to the reviewer. Flagging so it doesn't get lost, and because recruitment
text may need an edit depending on the answer.

**2. Missing office-hours consultation recruitment script with recording language.**
**FLAG — NOT DONE.** Appendix C has no consultation invitation; the only consultation
script is the in-session recording ask in Appendix B, which is not recruitment. Ready
language exists at `source/protocol_v2_ORA_RESPONSE.md:270-272` ("Consultation ('office
hours') invitation" — states it is research, recording with consent plus notes
alternative, materials with permission, no compensation, voluntary, contact info).

---

## Informed consent

**1. No signature needed; participation indicates consent; survey checkbox.**
**DONE** — Section 5 states surveys use an "I consent" checkbox that gates the questions,
and that for workshops, consultations, and interviews taking part after receiving the
form indicates consent. Appendix A's signature line is gone.
**FLAG (minor):** Appendix A now ends at Contact Information with **no consent statement
at all**, and Appendix D's introduction has no "I consent" checkbox item (only "Your
Email:"). The reviewer removed the *signature*, not the consent block — keep an
unsigned consent statement in Appendix A and show the checkbox in the survey instrument
so the mechanics described in §5 are visible where they happen.

---

## Confidentiality

**1. When survey data are deleted from the platform.**
**DONE** — Section 6 states survey responses are deleted from Qualtrics once archived,
within 14 days.

**2. Group sessions — cannot guarantee confidentiality; ask participants not to share.**
**DONE** — Section 6 carries both sentences (ask participants to respect peers'
confidentiality; we cannot guarantee it in a group setting).

---

## Compensation

**1. Say if there is compensation for the other data collection methods.**
**FLAG — NOT DONE in the Narrative.** Section 9 still covers only the $25 for interviews
and workshops: no $10 survey compensation and no statement that consultations are
uncompensated. Both are promised in Appendix A, so the narrative is the piece that
contradicts the consent form. Ready sentence at
`source/protocol_v2_ORA_RESPONSE.md:147`.

**2. Clarify the "$25 into someone's UMaine account" language.**
**FLAG — NOT DONE.** Section 9 still reads "employees of the University of Maine will
receive the $25 instead transferred to them via UMaine…" — the exact language the IRB
found confusing, and it now **contradicts** Appendix A and the interview/follow-up
recruitment emails, which all say UMaine employees receive no gift card or other
compensation. Replace §9's sentence with the Appendix A version (the IRB #2 v9 wording
you already adopted). This is the highest-priority flag: it is an internal contradiction
a reviewer will catch.

---

## Appendix A — Consent form for instructor participation

**1a. "Respond to" instead of "complete."**
**DONE** — both survey bullets now read "Respond to."

**1b. Surveys are online and confidential.**
**DONE** — "Respond to an online confidential survey…" and the follow-up bullet matches.

**1c. Design workshop — must they agree to the recording; what other data are collected.**
**DONE** — the workshop bullet states Zoom, recording with webcam video excluded, "you
must agree for recording to take part," deletion on request, and that materials produced
in the workshop are also collected.

**1d. Interviews — briefly explain the topic; fix the in-person inconsistency.**
**DONE** — the interview bullet now names the topics (teaching context, benefits and
barriers, integration experiences) and says "on Zoom or in-person," matching the
narrative.

**2a. Change third-person phrasing to "you/your."**
**MOSTLY DONE — FLAG two spots.** The confidentiality section is now in second person
except: "Participants in design workshops will be asked to respect the confidentiality
of their peers…" (should be "You will be asked…"), and a garbled clause, "when your
email address email addresses is deleted from the key mapping file."

**2b. Delete "on Dec 15, 2031."**
**DONE, but FLAG the neighbours.** The literal phrase is gone and the final sentence
carries no date. However three "for example, for the Fall 2026 semester … by the end of
December 2031" examples remain in the form (confidentiality ×2, Voluntary ×1). The
reviewer's reason — this form will be used beyond 2026 — applies to those too; consider
cutting them and keeping "five years after your participation."

**2c. Group sessions — cannot guarantee confidentiality.**
**DONE** — present in both Risks and Confidentiality.

**3a. "For each interview or design workshop session you participate in."**
**DONE** — that is the exact wording now used.
**FLAG (minor):** the same paragraph still says "You must reach the end of a session to
receive the compensation … if you stop partway through you will not receive the gift
card," which reintroduces the completion condition the reviewer was steering away from.
Also "sent by email within 2 business days **of the interview**" should say "of the
session," since the sentence also covers workshops.

**3b. Survey compensation must appear in the Narrative; "For each survey that you submit."**
**HALF DONE — FLAG.** Appendix A has "for each survey that you submit … You may skip the
occasional question … one gift card per survey invitation." The Narrative still does not
mention survey compensation — see Compensation 1 above.

**3c. Say whether consultation sessions are compensated.**
**DONE in Appendix A** ("There is no compensation for consultation ('office hours')
sessions") — **FLAG:** missing from Narrative §9.

**4. Participants need not sign the consent form.**
**DONE** — no signature line remains (see the Informed consent minor flag about keeping
an unsigned consent statement).

---

## Appendix B — Design workshop protocol

**1. Specify that workshops are conducted on Zoom.**
**DONE** — the first line reads "Workshops are held online via zoom," and the ground
rules add that agreeing to the recording is part of taking part.

---

## Appendix C — Instructor recruitment texts

### Mailing-list blurb

**1. Say it is research earlier.** **DONE** — the first sentence opens "As part of a
research study, we are recruiting instructors…"

**2. Zoom, recorded, agreement to record, other data collected.** **DONE** — "held on
zoom (audio and screenshares are recorded but webcam videos are deleted) … Agreeing to
the recording is part of taking part, and the notes and materials produced during the
workshop are also collected."

**3. Survey is online and confidential.** **DONE** — "confidential online 10–15 minute
survey."

**4. "These approaches may include…" instead of "This may include…"** **DONE** — reads
"These approaches may include, for example."

### Targeted email to an individual instructor

**1. Say it is research earlier.** **DONE** — the opening sentence invites them to "a
University of Maine research study online design workshop."

**2. Zoom, recorded, agreement to record, other data collected.**
**FLAG — NOT DONE.** This email says only "Workshops run about one to two hours." No
Zoom, no recording, no agreement-to-record, no other-data statement. Copy the blurb's
sentence across (or `source/protocol_v2_ORA_RESPONSE.md`, targeted-email block).

**3. Survey is online and confidential.** **DONE** — "confidential online 10–15 minute
survey."

**4. "These approaches may include…"**
**FLAG — NOT DONE.** This email still reads "Workshops run about one to two hours. This
may include, for example: a) small student reflection groups…" — the exact ambiguity the
IRB flagged. Fixed in the blurb but not here.

### Workshop invitation

**1. Say it is research earlier.** **DONE** — "as part of a University of Maine research
study, we are holding an online design workshop."

**2. Zoom, recorded, agreement to record, other data collected.** **DONE** — venue,
recording, webcam deletion, agreement-to-record, and notes/materials all stated.

**3. Researcher name and contact information.** **DONE** — "Questions: Greg Nelson,
Assistant Professor, University of Maine (gregory.nelson@maine.edu)."

**4. Compensation (optional).** **DECLINED, deliberately** — per your doc comment, left
out because the IRB said it was optional. No action needed; adding "$25 per workshop
session" would help recruiting if you change your mind.

### Instructor follow-up survey

**1. Researcher name and contact information.** **DONE** — Greg Nelson and Cyril
Agbewali-Koku with emails.

**2. Compensation (optional).** **DECLINED for this template** — the $10 appears in the
longitudinal version only. Fine as optional, but see the next section: if the two
templates merge, the compensation line comes with it.

### Interview

**1. Say the interview is on Zoom (and possibly in person).** **DONE** — "held on Zoom or
in person, based on your preference."

**2. Recorded, with notes if they decline.** **DONE** — "With your agreement the
interview is audio-recorded (no video is recorded); if you would rather not be recorded,
the researcher will take written notes instead."

**3. Researcher name and contact information.** **DONE** — both researchers with emails.

**4. Rewrite the "thank you for offering to talk with us further" opener.**
**DONE** — now opens "we are inviting you to take part in a research interview about
your teaching context…" with a scheduling link, following the reviewer's suggested
framing.

**5. Compensation (optional).** **DONE** — the $25 card and the UMaine-employee
exception are stated.

### Longitudinal follow-up

**1. Researcher name and contact information.** **DONE** — both researchers with emails.

**2. "We are not sure what is different about this from the other follow-up survey."**
**FLAG — NOT DONE.** Both templates are still in Appendix C and still near-identical;
the only differences are the word "online" and the compensation sentence, and nothing
explains why there are two. The v2 draft resolved this by **deleting** the standalone
longitudinal template and keeping one follow-up email (with compensation and the
one-card-per-invitation line). Either do that, or state plainly what distinguishes them.

**3. Clarify compensation is one gift card per invitation, not per survey in a sitting.**
**DONE** — "one gift card per survey invitation" appears in this email and in Appendix A's
compensation section.

---

## Summary of what still needs doing

Substantive (a reviewer would notice):

1. **Narrative §9 UMaine-employee language** — still the confusing "$25 transferred via
   UMaine," and it contradicts Appendix A and the recruitment emails.
2. **Narrative §9 missing survey ($10) compensation and the no-compensation-for-
   consultations statement** — promised in Appendix A only.
3. **No office-hours consultation recruitment script** in Appendix C.
4. **Targeted email** lacks Zoom/recording/agreement/other-data.
5. **Targeted email** still says "This may include, for example."
6. **Two duplicate follow-up survey emails** with no stated difference.

Smaller cleanups:

7. Methods item 1: add "online."
8. "Appendices D and Li8" broken reference; Appendix D title vs. follow-up use.
9. Appendix A: "Participants in design workshops…" → "You…"; fix "your email address
   email addresses is deleted."
10. Appendix A: consider deleting the remaining "Fall 2026 → December 2031" examples.
11. Appendix A/D: keep an unsigned consent statement, and show the "I consent" checkbox
    in the survey instrument.
12. Appendix A compensation: the "must reach the end of a session" condition, and "within
    2 business days of the interview" → "of the session."

Items 1–6 all have finished language in
`irb3-instructor-adoption/source/protocol_v2_ORA_RESPONSE.md`; the fastest path is to
reconcile the Google Doc against that file rather than editing the Doc point by point.
