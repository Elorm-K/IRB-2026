# Board-specific rules (UMaine, YES Lab protocols)

Everything here is empirical — what this board has actually required or accepted, not
general IRB advice. Where this conflicts with generic guidance, this wins. Update it
after every board response.

**Two kinds of rule live here, and they don't transfer the same way.** Sections 1–4 and 6
are *board-wide*: they apply to any protocol going to this IRB, whatever the project or
funder. Section 5's catalog is *program-specific* — the calls were made on
reflection-groups protocols, and items marked **[program-specific]** should be re-derived
rather than copied when drafting for a different study or grant. When adding to this file,
mark which kind you're adding.

Provenance tags: (GN 2026-07-27) = advisor meeting transcript, 2026-07-27.

## Contents

1. Consent forms — required inclusions
2. Consent forms — required exclusions
3. Consent form architecture (how many, and when)
4. Compensation
5. Keep / cut catalog
6. Known board tendencies
7. Calibration from the approved GenAI protocol

**The institution's own published rules are not here.** They live in
`institutions/<slug>.md` — for UMaine, `institutions/umaine.md`. This file is what the board
has *done*; that file is what the institution has *written*, plus the conflicts between the
two. Phase 4 Pass 4 (`compliance-check.md`) checks against that file, not this one.

---

## 1. Consent forms — required inclusions

- **Example statements.** This board requires concrete examples rather than bare
  policy statements. A retention policy stated as "data retained for five years" has
  previously been insufficient on its own — an example statement is expected alongside
  it. Deleting the example statements from a previously approved consent form is a
  regression, not a simplification (GN 2026-07-27).
- **An estimate of time burden.** How much time participation asks of people. Broad
  ranges are acceptable and preferable — the estimate is required, the precision is not.
- **Any genuinely distinct activity.** If participants are being asked to do a different
  kind of activity, the board will want it named in the consent form, and it should be
  there.
- **Benefits.** Err toward including more of them rather than fewer.
- **Platform properties, where they matter.** Not the vendor name — the property
  ("connections are encrypted," "stored in a secure cloud platform with restricted
  access").

## 2. Consent forms — required exclusions

- **Interview questions.** The consent form says participants will take part in
  interviews; it does not contain the instrument (GN 2026-07-27). Verified against the
  most recently approved interview consent form.
- **Meeting agendas.** Groups are adaptable by design; fixing an agenda in the consent
  form both misdescribes the intervention and creates deviation risk.
- **Content already covered elsewhere in the same form.** Do not restate
  confidentiality provisions under other headings.

## 3. Consent form architecture

- **One consent form per study**, by default.
- **A separate consent form is appropriate for a genuinely different activity** — e.g.
  interviews. Base it on the most recently approved interview consent form; do not
  author a new format.
- **No separate survey consent form is needed** where participants have already consented
  to the study.
- **Consent must happen first.** For approval, what matters is that consent occurs early
  in the process, not the specific mechanism. The protocol can stay flexible about how
  it is administered (an initial interview, an interest session, a help session), because
  the mechanism doesn't affect approvability (GN 2026-07-27).
- **Where participation is voluntary and outside a course, there are no non-consenting
  participants.** Delete non-consenting-participant procedures — they're inherited
  boilerplate from classroom protocols. Relatedly, in the reflection-groups-outside-class
  study, everyone who participates in a reflection group is part of the research; there
  is no non-research participation path (GN 2026-07-27).

## 4. Compensation

Must be plausible payment for the burden requested. Reference points:

- 60-minute interview: **$10 is too low; ~$25 is the floor** (GN 2026-07-27). A floor, not a
  norm — the board has approved $30 per interview plus a retention bonus for students. See
  `institutions/umaine.md` §7 for the approved amounts, the worked-total pattern, and the
  tax-reporting thresholds.
- Delivered as gift cards.

Compensation amounts are a PI decision — flag rather than set them, but flag loudly when
a carried-over amount is implausible for the time asked.

**The gift card mechanism is reviewable, not just the amount (ORA, 2026-08-07).** On IRB #2
the reviewer required three things the protocol had not addressed: recipients submit the
University's payment information on a **separate instrument not connected to their
responses**; **University employees cannot be paid by gift card at all**; and no individual
card exceeds $50. Any protocol that pays participants needs a payment-information appendix,
a confidentiality statement that it is stored apart from research data, and a line in every
consent form saying a gift card requires it. The rules themselves are in
`institutions/umaine.md` §7.

## 4b. Instruments belong in appendices **(ORA, 2026-08-07)**

The board asks for the **actual instrument**, not a description of it: "Include Appendix
with survey questions" and "Include Appendix with interview protocol," against a protocol
whose narrative described both in prose. Every survey and every interview guide named in
the narrative needs its own appendix, for both instructor-facing and student-facing
instruments — a reviewer who asks for one guide will ask for the other.

This **contradicts** the allowance recorded at `institutions/umaine.md` §5 that "a topical
description plus one or two examples covers both." That allowance was inferred from approved
forms, and it drove an IRB #2 revision that folded three instrument appendices into inline
prose. The review cost a round. When a published checklist asks for instruments and approved
practice appears to permit less, follow the checklist: an extra appendix is free, a review
cycle is not.

**Pay per interview, not once (GN, final IRB #1, 2026-08-04).** All three protocols in this
program pay per interview; every approved Compensation section in the program does. A "$X once,
however many interviews" scheme is the outlier — it drives the average below the floor as soon as
interviews repeat, and it silently drops the tax-reporting language, because a single payment
cannot cross $75. If interviews can repeat, write per-interview, add a worked total, and check
whether the maximum cumulative payment now crosses $75 in **every** consent form for a
compensated activity.

## 4a. PI drafting preferences (from the final IRB #1, 2026-08-04)

Greg's edits between the drafted and the submitted IRB #1. Apply these when drafting rather than
waiting to be told:

- **Expected N: state a ceiling, not a forecast.** In the population section, give one generous
  maximum with a one-clause rationale for why it cannot be predicted (*"Given we will openly
  recruit people online, over 5 years we may have up to 1,000 participants"*). Keep any arm-by-arm
  planning figures in Methods as the basis, not in the population section, where they become the
  approved number. Do **not** state a recruitment funnel — those figures drift within a semester.
- **Every person listed gets a years-of-experience figure.** The application requires a number, and
  "if none, say 0 years." Do not leave the line off.
- **Lists of criteria are illustrative, not exhaustive.** *"based on shared affinity and other
  characteristics such as …"* rather than a closed list that a change of practice would violate.
- **Delete detail that constrains a mechanism.** Cut from the drafted IRB #1: "which uses only the
  same intake information" (matching tool), "as peer members (not mentors)" (professionals), and a
  sentence describing which sub-consents the consent form carries.
- **Broaden the construct one notch.** "Reflection groups" → "reflection **activities**, such as
  reflection groups" wherever the modality is incidental, so a variant does not need a modification.
- **State consent mechanics once**, in the informed-consent section — not again in Methods.

## 5. Keep / cut catalog

Concrete calls made on real drafts. Extend this list as more are made.

### Cut

- Fixed durations that reality may vary ("10 weeks" → semester-aligned language).
- Named vendors and tools (Google Drive, Zoom) → property descriptions. **Narrative
  Summary/Methods body only.** The institution's instructions *require* vendors named in the
  Confidentiality section and in consent-form data-handling text, and the board has approved
  forms that name them — see `institutions/umaine.md` §6. De-naming there is a violation, not
  a simplification.
- Per-meeting agendas and step-by-step activity breakdowns → "complete an icebreaker,"
  then group self-direction.
- Course, enrollment, and graduation language in out-of-class protocols.
- Eligibility criteria the protocol doesn't actually impose (e.g. not having previously
  been in a reflection group) unless it is a real criterion.
- Restatements of content covered elsewhere in the document.

### Keep

- Board-required example statements in consent forms.
- The approved description of what group meetings are (generalize if needed; don't
  rewrite).
- The approved data-management framing.
- Approved interview consent form structure.

### Add, if absent

- A statement that once a group has started meeting, its members decide how to use their
  time — this makes group self-direction part of the described intervention rather than a
  deviation from it (GN 2026-07-27).
- **[program-specific]** For the CAREER protocol: language allowing workshops to concern
  reflection groups, designing AI integration in courses, or designing reflection around AI.
- **[program-specific]** For the CAREER protocol, if submitted in stages: participation in design workshops does
  not obligate instructors to use reflection groups in their courses; instructors may use
  reflection groups without their course or students participating in research; research
  involving their students will be submitted as a modification or separate protocol.

## 6. Known board tendencies

- Wants **Word documents**; formatting damage from Google Docs round-trips is a recurring
  cost, and worsens with bullet density.
- Does not consistently handle exempt / minimal-risk review as such — expect
  full-review-style scrutiny of low-risk procedures.
- Tends to ask for paragraphs to be **moved or duplicated between sections** rather than
  rewritten. Cheap to satisfy; not worth pre-empting.
- May object to detail that doesn't affect approvability. That is an argument for cutting
  such detail up front, not for justifying it at length.

---

## 7. Calibration from the approved GenAI protocol (added 2026-07-28)

Source: `../inputs/approved-protocols/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` — "Learning with Generative AI in introductory college courses." Board-approved through **January 2026**, the most recent approved consent forms in the program. **This is the highest-weight consent template**, ahead of the course protocol's Appendix P and ahead of IRB #1's drafts.

**The board-wide items from this calibration have moved to `institutions/umaine.md`**, where
they sit next to the published UMaine rule each one conflicts with, so the conflict is
visible rather than implied:

| Item | Now in |
|---|---|
| Approved consent heading order (Confidentiality before Compensation) vs. the public sample | `institutions/umaine.md` §4 |
| Approved affirmation block — checkbox plus email, not Printed Name / Signature / Date | §4 |
| Concise summary — required on paper, never yet used in this program | §5 |
| Sample interview questions — topical description accepted in place of examples | §5 |
| Vendors **are** named in approved Confidentiality sections | §6 |
| Approved recording retention — 5 years, tied to the key file | §6 |
| Approved interview compensation — $30 plus a retention bonus, with worked totals | §7 |

What stays here is the program-specific finding:

### What this protocol does and does not cover **[program-specific]**

It covers generative-AI-integrated courses, GenAI tool usage logs, weekly reflections, surveys, and recurring qualitative interviews — including *"screen recordings (which will not include your face)"* taken **during interviews**.

It does **not** cover the grant's Task 2 video-assisted comparative reflection **assignment**: zero occurrences of "replay" or "anonymiz", and no screen-recording-as-assignment procedure. Combined with the course protocol and IRB #1, **no protocol covers grant §3.2's video-reflection assignment, the budgeted anonymization platform, or GenAI IDE log data.** The grant's claim at §3, p.6 that existing approvals "already cover the proposed work in Task 1 and 2" does not hold for the assignment itself.
