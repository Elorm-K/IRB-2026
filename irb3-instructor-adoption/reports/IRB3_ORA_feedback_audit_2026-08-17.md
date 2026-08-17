# IRB #3 — audit of the Google Doc against ORA feedback

Source audited: Google Doc "Developing Professional Skills Including Critical and
Reflective Use of Generative AI in Computing Education"
(`docs.google.com/document/d/1evcxa_HrsjqH7PlaSCmaED_CoEMaDp9wz6oBimoR8Pg`).

- **Pass 1:** 2026-08-17, morning. 13 items flagged.
- **Pass 2:** 2026-08-17, after Cyril's revisions. **8 of 13 fixed; 5 still open, plus 4
  cosmetic.** Only one of the open items is a reviewer request that is still entirely
  unaddressed (the consultation recruitment script).

---

## Fixed since pass 1

1. **Methods item 1 now says "online"** — "invited to an online confidential survey …
   administered via qualtrics." Reviewer's Methods 1 fully satisfied.
2. **Narrative §9 now states survey compensation** — "$25 … and for each survey the
   instructor submits, they are offered a $10 gift card." The narrative no longer
   under-promises relative to the consent form (Compensation 1, main part).
3. **Narrative §9's confusing UMaine-account language is gone** — replaced with the
   policy-based version: gift cards may not compensate University employees, so
   UMaine-employed instructors are not offered one and take part on the same terms
   otherwise. This resolves Compensation 2 **and** the contradiction with Appendix A that
   was my highest-priority flag.
4. **Targeted email now explains Zoom, the recording, agreement-to-record, and the other
   data collected** — the blurb's sentence was carried across (Appendix C, targeted
   email, point 2).
5. **"Appendices D and Li8" typo fixed** — now "(Appendices D)".
6. **Appendix A's garbled clause fixed** — "your email address email addresses is
   deleted" now reads "your email address is deleted."
7. **Appendix A compensation timing fixed** — "within 2 business days of the **session**"
   instead of "of the interview," so it correctly covers workshops.
8. **One of the three "December 2031" examples removed** from Appendix A (the recordings
   paragraph).

---

## Still open

### 1. No consultation ("office hours") recruitment script — Recruitment 2

The only reviewer request still entirely unaddressed. Appendix C has the blurb, the
targeted email, the workshop invitation, the follow-up survey email, the interview
invitation, the longitudinal follow-up email, and the compensation email — no
consultation invitation. The reviewer specifically asked for one that explains you would
like to record the session for research purposes. Ready text sits at
`irb3-instructor-adoption/source/protocol_v2_ORA_RESPONSE.md:270-272`.

### 2. Targeted email still says "This may include, for example" — Appendix C, targeted email, point 4

The mailing-list blurb was fixed to "These approaches may include, for example," but the
targeted email still carries the original wording the IRB flagged as implying that
workshops would contain student reflection groups. One-phrase edit. (There is also a
stray double period: "non-use of generative AI..")

### 3. Both follow-up survey emails are still there — Longitudinal follow-up 2

"Sending out an instructor follow-up survey" and "Sending out an instructor longitudinal
follow-up survey" remain near-identical; the only differences are the word "online" and
the compensation sentence, and nothing states what distinguishes them. The reviewer asked
what the difference is. Cleanest answer: delete the standalone longitudinal template and
keep one follow-up email carrying the compensation and one-card-per-invitation line.

### 4. Narrative §9 has two loose ends left — Compensation 1

- **Consultations are still not mentioned.** Appendix A says "There is no compensation for
  consultation ('office hours') sessions"; §9 is silent, so the narrative still doesn't
  answer "is there compensation for the other data collection methods" completely.
- **The employee exception now reads too narrowly:** "not offered a gift card **for an
  interview**." Now that §9 also promises $10 per survey, this leaves open whether a
  UMaine employee gets paid for a survey. Appendix A says employees receive no gift card
  or other compensation at all — so make §9 say "for any of these activities."
- Minor: §9 still says the card is sent "within 2 business days of **the interview**"
  while that clause now also governs surveys and workshops. Appendix A already says "of
  the session"; match it.

### 5. Appendix A has no consent statement, and Appendix D shows no "I consent" checkbox — Informed consent 1

§5 correctly describes the mechanics (checkbox for surveys, participation-indicates-
consent for sessions), but Appendix A now ends at Contact Information with no closing
consent block at all, and Appendix D's introduction still goes straight from the intro
paragraph to "Your Email:". The reviewer removed the *signature requirement*, not the
consent statement. Add an unsigned consent statement to Appendix A, and show the "I
consent" item in the survey instrument so the reviewer can see what §5 describes.

---

## Cosmetic, take or leave

- **Appendix A:** "In design workshops, you will be asked to respect the confidentiality
  of **their** peers" — the switch to second person left "their" behind; should be "your
  peers."
- **Two "December 2031" examples remain** (Appendix A confidentiality paragraph 3, and the
  Voluntary section). The reviewer only required the final sentence's date be dropped, so
  this is optional — but their reason (the form outlives 2026) applies to these too.
- **Appendix A compensation** still says "You must reach the end of a session to receive
  the compensation … if you stop partway through you will not receive the gift card,"
  which reintroduces the completion condition the reviewer was steering away from with
  their "participate in" edit. Low risk; your call.
- **"(Appendices D)"** — plural word, single appendix. Also worth deciding whether
  Appendix D, titled "interest and barriers survey," should be retitled or split, since
  Methods 5 routes follow-up surveys to it.

---

## Outside the document

**Recruitment 1 — other UMS campuses besides UMaine/UMM.** Still owed as your email reply
in the separate thread. If the answer adds campuses, recruitment text may need a
follow-up edit.

---

## Verdict

The package now answers every reviewer point except the consultation recruitment script
(open item 1) and the "This may include" phrase in the targeted email (open item 2) —
those two are direct requests still unmet and would likely come back. Items 3–5 are
places where a reviewer could reasonably ask again. Everything else is either done or
cosmetic.
