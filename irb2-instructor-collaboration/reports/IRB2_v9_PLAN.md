# IRB #2 v9 — plan for responding to ORA review comments

**Date:** 2026-08-10
**Reviewer:** Aubrey Rogowski (UMaine ORA), 7 open comments on Google Doc "IRB 2"
(`1evcxa_Hr…`), left 2026-08-07 between 20:57 and 21:09.
**Status:** awaiting Cyril's approval. Nothing has been drafted yet.

---

## 0. What I checked first

**The commented doc has not been edited since v8 was built from it.** Its `modifiedTime`
is `2026-08-07T21:09:17`, identical to the timestamp of Aubrey's last comment — so the only
change since the 2026-08-06 19:37 snapshot is the comments themselves. A normalized diff of
the doc against `source/protocol_v8_MIDFINAL.md` confirms it: every difference is something
v8 *added or repaired*, nothing the doc gained afterward.

That matters, because it means **v8 already answers part of the review**. Aubrey read the
unrepaired text.

**The doc she read carries three broken appendix cross-references** that v8 already fixed:

| In the doc she read | Points at | Should be |
|---|---|---|
| §2 item 6 — pre/post measures | Appendix **M** | Appendix **H** (doesn't exist in the doc) |
| §2 item 16 — site approval | Appendix **P** | Appendix **J** (doesn't exist in the doc) |
| §2 data item 1.3 — workshop recordings | Appendix **H** | Appendix **E** (H is the student intake survey — reads as correct, isn't) |

**The CAREER grant is silent on compensation.** I searched all 27 pages of
`inputs/grant/FINAL NSF_CAREER_25_Nelson.pdf` for gift cards, incentives, compensation,
stipends, honoraria, and dollar amounts. Nothing. The only related text is a "small grade
incentive" idea for a future design (p. 9). The PDF contains the project description only,
no budget justification. So the $25/$10 figures trace to prior YES Lab board precedent and
Greg's 2026-07-27 instruction — **not** to a funded commitment. Changing them breaks nothing
promised to NSF.

**Base for v9, as approved:** `source/protocol_v8_MIDFINAL.md`, with the instrument
appendices restored from `source/protocol_v7_MERGED.md`. This retires the v7/v8 split the
v8 report warned about.

---

## 1. The seven comments, mapped to their anchors

The Drive API returns comment threads and anchor spans separately. I matched them by
document order against comment chronology; every pairing is semantically unambiguous.

| # | Anchor text in the doc | Comment |
|---|---|---|
| 1 | §2 ¶3 — "an initial round of instructor design workshops anticipated in fall 2026" | "How many?" |
| 2 | §2 ¶3 — "classroom use in collaborating instructors' courses beginning in a subsequent term" | "How many classrooms and students will be impacted?" |
| 3 | §2 item 1 — "Interest and barriers survey." | "Include Appendix with survey questions." |
| 4 | §2 item 2 — "Optional interviews." | "Include Appendix with interview protocol." |
| 5 | §2 item 8 — "Group meetings and individual reflections." | "Will these be recorded?" |
| 6 | §9 — the **Instructors** compensation paragraph | "Instructors will be required to fill out a Qualtrics form requesting information for the university business administration office in order to process the gift cards. This should be a separate survey not connected to the participant's responses." → reply: link to the [ORA gift card policy](https://umaine.edu/ora/gift-card-purchases/) → reply: "UMaine employed instructors are not eligible to receive gift cards per the policy linked above." |
| 7 | §9 — the **Students** compensation paragraph | "Students will also have to provide required information to receive a gift card." |

---

## 2. Proposed changes, comment by comment

### Comment 1 — how many design workshops

**Change:** §2 ¶3 gains a count; §2 item 3 gains scale.

The grant (§3.1.2, p. 7) commits to "a yearly design cycle for adoption with faculty …
and a design workshop," plus co-design workshops with students and faculty "until the design
stabilizes, which we expect by end of Year 2 or 3." Draft language, generalized per the
approvability test so a count change isn't a protocol deviation:

> An initial round of instructor design workshops is anticipated in fall 2026, with roughly
> one to three workshops per design cycle and approximately one design cycle per year over
> the award. Each workshop typically involves a small group of instructors.

**⚠ [PI DECISION NEEDED]** — "a small group" needs a number Aubrey can use. The grant does
not give one. I suggest "approximately 5–15 instructors," which is consistent with the
~200-instructor ceiling in §4, but **Greg should set it.** I will not invent it.

### Comment 2 — how many classrooms and students

**Change:** §2 ¶3 gains a forward pointer; no new numbers invented.

The numbers already exist in §4: class sizes 30–50, roughly 10 courses per year once the
design stabilizes, up to ~1,000 students and ~200 instructors over the protocol's duration.
Aubrey asked in §2 because §2 doesn't say. Fix is to surface them at the anchor:

> …classroom use in collaborating instructors' courses beginning in a subsequent term
> (approximately 10 courses per year once the design has stabilized; see Section 4 for
> participant numbers), and a yearly faculty adoption design cycle thereafter.

**Optional, worth considering:** §4 lumps intervention-course and comparison-course students
into one ~1,000 figure. Splitting them would pre-empt an obvious follow-up. Low cost, and I'd
do it unless you say otherwise.

### Comment 3 — appendix with survey questions

**Change:** restore three instructor instruments from v7 as new appendices.

Your 2026-08-06 edit pass deleted these; v8 folded them into inline prose, justified by
`institutions/umaine.md` §5 ("a topical description plus one or two examples covers both").
**Aubrey has now overridden that** — she asked for appendices, explicitly, twice. Restoring
is preserve-not-invent: the text is already drafted and previously reviewed.

- **Appendix K — Instructor interest and barriers survey** (v7 Appendix E, 11 items, verbatim)
- **Appendix L — Instructor follow-up survey, later semesters** (v7 Appendix F, verbatim)

Student surveys already have appendices — v8 Appendix H (group-matching, pre-, post-course)
and Appendix I (longitudinal follow-up). Both are clean text in v8; the `[image]` Likert
matrices in your Google Doc were already converted.

**One gap this exposes:** §6 and data item 1.4 refer to a "group-matching survey," and v8's
Appendix H covers it, but the doc's §2 item 10 had dropped the sentence that sends the reader
there. v8 restored it. No further work needed — noting it so it isn't re-flagged.

### Comment 4 — appendix with interview protocol

**Change:** restore the instructor interview guide; author the missing student one.

- **Appendix M — Instructor interview guide** (v7 Appendix G, verbatim restore). The v8
  inline description in §2 item 2 stays, shortened to a pointer.
- **Appendix N — Student and alumni interview guide** — **does not exist in any version.**
  The v7 reconciliation report flagged this as an open gap on 2026-08-06. Aubrey's comment is
  anchored on instructor interviews, but §2 item 13 promises student and alumni interviews
  and Appendix D consents them, so a reviewer who asks for one guide will ask for the other.

**⚠ Decision for you:** author Appendix N now, or defer it? I recommend authoring it — it is
derivable from the grant's §3.1.3 longitudinal-transfer aims and from the approved interview
guides in the AI course protocol (`inputs/approved-protocols/`, Appendix L), so it is
derivation rather than invention. Deferring means a near-certain third round.

### Comment 5 — will group meetings be recorded

**Change:** already answered by v8; sharpen it and make it unmissable at the anchor.

v8 restored "Reflection group meetings are not recorded." to the end of §2 item 8 — exactly
where Aubrey asked. The doc she read had that sentence relocated to item 11 and §6, which is
why the question arose. I propose stating it affirmatively and completely, since "not
recorded" alone invites "then what *is* captured?":

> Reflection group meetings are not recorded — no audio and no video. The data collected
> from a meeting are the group's own written agenda notes and each member's individual
> written reflection, submitted by the participants themselves.

This also aligns §2 item 8, §2 item 11, §6, and data items 1.5 on one wording. Design
workshops and interviews *are* recorded (with agreement) and stay clearly distinguished.

### Comments 6 and 7 — gift card processing

Three separate changes; this is the substantive part of the round.

**(a) The separate Qualtrics payment form.** Aubrey requires that recipients submit business-
office information through a form **not connected to their responses**. This is both a
procedure change and a confidentiality claim, so it lands in three places:

- **New Appendix O — Compensation information form.** Fields limited to what the business
  office requires; introduced with a statement that it is administered separately and is
  never joined to survey, interview, or reflection data.
- **§9 Compensation** gains the mechanism for both instructors and students.
- **§6 Confidentiality** gains one sentence: payment information is collected in a separate
  instrument, stored apart from research data, and not linked to responses.
- **Appendices A, B, C, D** (the four consent forms) — the Compensation section of each gains
  a plain-language line that receiving a gift card requires submitting this separate form.
  Per `institutions/umaine.md` §7, the board requires compensation specifics *in the consent
  form*, so this cannot live only in the narrative.

**(b) UMaine employees excluded — approved.** §9 and Appendix A gain:

> Gift cards cannot be used to compensate University employees, so instructors employed by
> the University of Maine are not offered the gift card for an interview. Instructors at
> other institutions are offered the $25 electronic VISA gift card described above.

Recruitment cost is real and worth naming: early-cycle instructors are disproportionately
UMaine colleagues. It breaks no NSF commitment (see §0), and it is what ORA asked for.

**(c) A conflict to resolve while we're here.** ORA policy caps individual gift cards at $50.
Our $25 and $10 amounts are fine. But §9 currently carries worked cumulative totals — "$50 in
total" for an instructor across two interviews, "$80 in total" for a student across eight
follow-up surveys — and the >$75 tax-reporting language. Those stay: they are per-card
amounts under the cap, and `institutions/umaine.md` §7 records that this board *requires*
worked totals. **No change proposed** — flagging it so it isn't mistaken for an oversight.

---

## 3. Appendix lettering

**Proposal: leave A–J exactly as v8 has them; append K–O.**

| New | Contents | Source |
|---|---|---|
| K | Instructor interest and barriers survey | v7 Appendix E, verbatim |
| L | Instructor follow-up survey (later semesters) | v7 Appendix F, verbatim |
| M | Instructor interview guide | v7 Appendix G, verbatim |
| N | Student and alumni interview guide | **new** — derived, pending your decision |
| O | Compensation information form | **new** — derived from ORA requirements |

Re-lettering into a more logical order is tempting and I am recommending against it. Twenty
of forty-one cross-references broke the last time appendix letters moved. Appending changes
zero existing references, so the only new refs are the five above. I will still run a full
mechanical contiguity and dangling-reference check over every appendix mention.

---

## 4. Deliverables (repo only, as approved)

- `source/protocol_v9_ORA_RESPONSE.md` — the source
- `CURRENT/IRB2_Protocol_v9_ORA_RESPONSE.docx` — built with `tools/build_docx.py`, every
  addition and change marked in bold red so you can see the whole diff at a glance
- `reports/IRB2_v9_ORA_RESPONSE_REPORT.md` — the Phase-4 verification report: alignment diff
  vs. v8, coverage vs. the grant, internal consistency across protocol/consents/recruitment,
  and the `compliance-check.md` pass against `institutions/umaine.md`
- `archive/IRB2_Protocol_v8_SUPERSEDED_2026-08-10.docx`
- A comment-by-comment response table you can paste back to Aubrey

No Google Doc will be created. The commented doc stays untouched as the round-1 record.

---

## 5. Open items for Greg

1. **Number of instructors per design workshop** — not in the grant, needed by Aubrey.
2. **Author the student/alumni interview guide now, or defer?** — my recommendation is now.
3. **Confirm the UMaine-employee exclusion is acceptable for recruitment** — Cyril approved
   the drafting approach; Greg owns the recruitment consequence.

---

## 6. Skill self-revision this round triggers

- `references/board-rules.md` — the board requires **actual instruments as appendices** for
  surveys and interview guides. This is a substantive requirement.
- `references/institutions/umaine.md` §5 — the "topical description plus one or two examples
  covers both" allowance is **contradicted** by this review. It drove the v8 design and cost a
  round. Correct or qualify it.
- `references/institutions/umaine.md` §7 — add the gift card rules: employees ineligible,
  $50 per-card cap, separate unlinked payment form required, W-9 where applicable, with the
  ORA policy URL as the source.
