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

Provenance tags: (GN <date>) = advisor meeting transcript of that date, in `inputs/meetings/`.

## Contents

1. Consent forms — required inclusions
2. Consent forms — required exclusions
3. Consent form architecture (how many, and when)
4. Compensation (4a PI drafting preferences · 4b instruments in appendices)
5. Keep / cut catalog (5b IRB #3 review findings · 5c response-round mechanics ·
   5d instructor-adoption framing)
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

**CORRECTION (GN 2026-08-17): "no gift cards for employees" limits the payment channel, not
the payment.** The employee rule above was drafted into IRB #3 v2 as "UMaine employees receive
no compensation," and the PI flagged that reading as an error — "it's not going to work to be
like, if you're a UMaine person, we're not going to pay you." Employees receive the **same
amounts through the University's regular payment process (payroll) instead of a gift card**.
The submitted IRB #3 sentence is the accepted wording; reuse it:

> "Instructors employed by the University of Maine receive the same compensation. Because
> University policy does not permit gift cards to be used to compensate University
> employees, their compensation is issued through the University's regular payment process
> instead of a gift card."

Related: UMaine's own payment-policy documents can be internally contradictory (some clauses
apply only above a payment threshold). When a policy reading would deny or reduce payment to
a participant class, verify with the business office / grant administrator who has processed
such payments before writing it into a protocol — do not adopt the harshest reading. And note
the confusion cost: the policy digressions that were written into the IRB #3 application
mainly confused the reviewers ("why are UMaine people different?"). State the outcome, not
the policy analysis.

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
  Summary only — no longer Methods.** The IRB #3 review (§5b) requires each Methods item
  to name its mode and platform; the institution's instructions *require* vendors named in
  the Confidentiality section and in consent-form data-handling text, and the board has
  approved forms that name them — see `institutions/umaine.md` §6. De-naming in any of
  those places is a violation, not a simplification. What survives of this cut: don't fix
  a vendor where nothing asks for one, and keep the properties ("encrypted," "restricted
  access") alongside any name.
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

## 5b. ORA review of IRB #3, 2026-08-14 — board-wide unless marked

From the reviewer's response to the instructor-adoption protocol. Each was a required
change; apply them when drafting, not after a round.

- **Exempt activities: consent forms are not signed.** The reviewer's words: participating
  in a workshop/consultation/interview *indicates* consent; for surveys, either submission
  indicates consent or an "I consent" checkbox gates the questions. Delete signature
  lines; keep the approved checkbox-plus-email block. Confirms the sample-form note in
  `institutions/umaine.md` §4 empirically.
- **Group sessions need the cannot-guarantee-confidentiality statement** in the narrative
  Confidentiality section *and* the consent form: researchers cannot guarantee
  confidentiality of responses, participants are asked not to share others' responses
  outside the session. The IRB #2 v9 sentence is accepted language — reuse it.
- **State when survey data is deleted from the collection platform**, not just where it is
  archived. Tying it to the existing archival window ("within 14 days of collection") adds
  no new commitment.
- **Each Methods item must say the mode and platform**: online or paper, and the named
  platform (they asked "Qualtrics?" directly), whether sessions are Zoom and/or in person,
  and for every recorded activity whether agreement to the recording is required to
  participate or notes are the fallback.
- **Follow-ups must be specified, not gestured at**: same procedures as the initial
  instruments (say so) or a promised future modification (say that instead), plus
  frequency. A follow-up instrument named in the narrative needs its own appendix — §4b
  applied to follow-ups.
- **Recruitment texts**: say it is research in the opening sentence, not the closing one;
  every script names a researcher and contact info; scripts for recorded activities
  describe the recording and what other data are collected; **every recorded activity
  needs its own recruitment script** — consultations were missing one and it was flagged.
- **Consent forms speak in second person throughout** — stray "the participant's" gets
  flagged.
- **No calendar dates in consent forms that outlive them** ("on Dec 15, 2031" ordered
  deleted; the example-format dates tied to a participation cohort survived).
- **Survey verbs: "respond to" / "submit," not "complete"** — participants may skip
  questions, and the form must read that way. Pair with per-invitation compensation
  clarity ("one gift card per survey invitation") so repeat surveys can't be misread as
  farmable.
- **State compensation (or its absence) for every data-collection method** in the
  narrative, not just the compensated ones.

## 5c. Response-round mechanics — board-wide (GN 2026-08-17, GN 2026-08-25)

How to answer a review round, learned across the IRB #3 rounds. These are about *how* to
respond, where §5b is about *what* the board requires.

**The board's returned Word document is the new base.**

- The board responds — and approves — by returning the application as a Word document
  containing **its own edits**, changes that were not in the submitted version. From that
  moment, the returned file is the canonical document. Never respond by editing your own
  copy and never "restore" a prior version over theirs; you would silently discard board
  edits.
- Changes go **into the returned document, in Microsoft Word, with Track Changes on**
  (All Markup view) — this is stated in the board's response email and is a hard
  requirement, not a preference. Drafting elsewhere is fine, but the deliverable is the
  returned file with tracked changes; from a Google Doc, that means a manual copy-paste
  pass at the end (open the returned `.docx` fresh, don't round-trip it through Docs).
- **Save under a new descriptive filename** (e.g. "…with student arm added") before
  editing. A changed file carrying the board's filename is mislabeled — it is no longer
  the file the board sent.

**Scoped compliance — do exactly what was asked, exactly where they asked it.**

- A comment asks for a change **in the place it is anchored** (usually a narrative
  section). Do not propagate it to recruitment emails, consent forms, or other sections
  the comment doesn't touch. "Add details about the recording" against Methods does not
  mean the invitation email needs recording details — adding them there was corrected out
  (GN 2026-08-17). The board *does* separately want some facts repeated across sections
  (§6), but let each comment tell you which section; don't guess.
- When the reviewer supplies text ("add this"), **paste their wording verbatim**. A longer
  paraphrase of their sentence is worse than their sentence.
- When the reviewer offers an option ("you may include X or not"), **take the simpler
  path — don't do the optional thing.** "If they give you an option to not do something,
  don't do something. Keep it simple."
- **Never add anything nobody asked for** in a response round. Unrequested additions
  (IP-address statements sprinkled beyond §6 where the instructions want them, new
  hedges, new details) create fresh review surface. The response's job is to close
  comments, not improve the protocol.
- **The board contradicts itself across rounds.** A date the board ordered added in one
  round was ordered deleted in a later round, on language lifted verbatim from an
  approved protocol. Comply with the current instruction, note the reversal in the
  response report, and do not argue from the board's own precedent — per-round compliance
  is cheaper than being right.
- Capitalize platform names (Qualtrics, Zoom) — a lowercase vendor name drew a correction.

**Accepted language from the IRB #3 rounds — reuse verbatim where the point recurs:**

- Group-session recording gate: *"Workshops are group sessions so you must agree for
  recording to take part in the workshop. You may ask after a session for anything you
  said to be removed from the recording."* The PI singled this sentence out as the right
  mechanic.
- Future-proofed category phrasing: *"For any group activities such as the workshops…"*
  — write the category with the current activity as an example, not the activity itself,
  so a later modification doesn't have to touch the sentence (GN 2026-08-17). Same move
  as §4a's "broaden the construct one notch," applied to consent/confidentiality text.
- Participatory flexibility: *"we will figure out the workshop design with the
  participants"* was accepted. Co-design language is a legitimate way to avoid
  committing to session details this board would otherwise pin down.

## 5d. Instructor-adoption program framing **[program-specific]** (GN 2026-08-25)

For IRB #3 and its student-arm modification. The load-bearing distinction: **we do research
*about* instructors; instructors do not do research.** Language that blurs it invites
multi-site IRB obligations at every instructor's institution — the exact outcome the
program design avoids.

- Instructors are **participants, not collaborators or research-team members**. Cut
  "collaborating with us," "joining the research," and anything implying they execute a
  study protocol in their course.
- Instructors make **teaching decisions as instructors**: whether to adopt, how to adapt,
  whether to give course credit for surveys, what extra questions to add for their own
  use. None of that is a research decision, and the protocol must not describe it as one.
  If the research team wants an instrument change for everyone, that is a modification to
  *our* protocol.
- **No comparison/control-course language.** We do not assign conditions. What an
  instructor did in their course is *data we collect from them* (an instructor survey
  item), not a design lever we hold.
- The research team's asks of instructors are narrow: distribute recruitment/survey links
  to their students, and pass along data **only for students who consented**. Students
  opt in individually to *our* study.
- Do not describe a non-research participation path inside the protocol ("you can use our
  materials without being in the research"). True, but the board expects only the research
  to be described, and it reads as confusing (GN 2026-08-11). Say it in recruitment or
  presentations, not the application.

## 6. Known board tendencies

- Wants **Word documents**; formatting damage from Google Docs round-trips is a recurring
  cost, and worsens with bullet density.
- Does not consistently handle exempt / minimal-risk review as such — expect
  full-review-style scrutiny of low-risk procedures. **Scrutiny level and consent
  formality are independent, though:** the review reads like full review, but exempt
  consent mechanics (no signature — §5b) still apply. Do not add signing formality
  defensively; the reviewer deletes it.
- Tends to ask for paragraphs to be **moved or duplicated between sections** rather than
  rewritten. Cheap to satisfy; not worth pre-empting. The same fact is expected in the
  methods narrative, the consent form, and the session script — when a round says "you
  didn't say this," it usually means one of the three copies is missing, in the section
  the comment is anchored to (GN 2026-08-17).
- **Reverses its own instructions across rounds** (add a date → delete the date, on
  approved-protocol language). Treat each round's instruction as current-round-only;
  comply and log, don't pre-empt or argue (§5c).
- May object to detail that doesn't affect approvability. That is an argument for cutting
  such detail up front, not for justifying it at length. The sharpest form of this
  (GN 2026-08-17): a misleading or unusual detail doesn't just draw a comment — it can
  **raise the board's perceived risk level** ("we won't recruit people who might be
  suicidal" reads as *your study involves suicidal people*). Never introduce a risk
  category, population, or blanket "we will never…" commitment the sources don't require.

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
