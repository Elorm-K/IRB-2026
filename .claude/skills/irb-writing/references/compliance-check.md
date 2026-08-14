# Pass 4 — Institutional compliance check

The fourth Phase-4 pass. Passes 1–3 check the draft against the base document, the governing
document, and itself. **This pass checks it against the rules of the board that will review
it** — the layer that produced most of the findings on IRB #2 and that no other pass would
have caught.

Two hard constraints on how it runs:

**Flag only. Fix nothing.** This pass edits no document. It produces findings; the PI decides
which to apply, and fixes happen afterward on instruction. That includes findings with an
obvious single correct fix — write the recommended fix in the table and stop there.

**Run on the assembled package.** The protocol body, every appendix, *and* every standalone
file that will actually be attached or sent. Reading only the protocol misses a whole class
of defect: IRB #2's standalone consent file was still v1 text, carrying the old protocol
title, a departed contact address, a missing team member, and a live
`[PI DECISION NEEDED]` marker, while the protocol's own appendix was correct.

---

## Before you start

1. **Which institution?** From the Phase-0 provenance block. If more than one board is
   involved, run the pass once per board against the documents that board will see.
2. **Is `institutions/<slug>.md` current?** If it is missing or more than a semester old,
   run `institution-research.md` first. Do not run this pass from memory of an institution's
   rules — that is how invented rules reach the PI.
3. **List the files in the package.** Write the list into the report. A file you did not open
   is a file you did not check.

Every row below cites the institution file by section number, so the same checklist works
for any board.

---

## A. Submission mechanics — institution file §2

The returned-unread gates. Cheapest findings in the whole protocol and the most embarrassing
to miss.

- [ ] File format is what the institution demands (Word vs. PDF), for **every** attachment.
- [ ] Attachment split matches the rule (e.g. cover page separate, narrative + appendices as
      one document).
- [ ] Page numbers present across the entire document.
- [ ] Submission address correct.
- [ ] Deadline: which review track, and does the calendar date still work for the study's own
      timeline? A protocol whose first activity precedes its earliest possible approval is a
      finding, not a scheduling detail.
- [ ] Title matches the grant title if funded.
- [ ] No tracked changes or comments left in, unless the institution asks for them (some
      require them for modifications — check §10).

## B. Narrative structure — institution file §3

- [ ] Every required heading present.
- [ ] Headings in the required **order**.
- [ ] No instruction/boilerplate text from the template left in the submission.
- [ ] No unresolved placeholders or decision markers anywhere in the package. Grep for the
      marker syntax the draft uses (`[PI DECISION NEEDED`, `{your input needed here}`, `___`,
      `TBD`, `XXX`). Distinguish real fill-in blanks that belong in a participant-facing form
      from markers that were meant to be resolved — the first are intentional, the second are
      violations.
- [ ] Cross-references resolve; appendix lettering has no gaps. Check mechanically — grep
      every `Appendi` mention against the actual appendix list. "Appendices K and Li8"
      survived to the IRB #3 submission and reached the reviewer.

## C. Personnel

- [ ] Every person listed has an experience statement in the form the institution requires,
      **with a number** where a number is required. A prose sentence about someone's
      background does not satisfy "state the years; if none, say 0." One missing line on one
      person is a returned application.
- [ ] Required training (CITI or equivalent) asserted for everyone, per-person rather than
      collectively if the institution asks per-person, with dates if required.
- [ ] Roles stated for each person.
- [ ] **Personnel turnover** addressed for a multi-year study: whether people can be added
      later under the PI's supervision, and whether the access clause in §6 covers them. A
      five-year protocol staffed by graduate students and undergraduate coders will change
      hands.
- [ ] **Dual roles named.** Anyone who is both researcher and instructor/supervisor for
      participants, and how the conflict is handled.

## D. Consent forms — institution file §4, §5

Run this sub-checklist **once per consent form**, and list the forms by name in the report.

- [ ] Heading order matches the order the institution requires — using the approved-practice
      order where the institution file records a conflict, and saying so in the finding.
- [ ] Reading level within the stated ceiling.
- [ ] Concise summary present where the trigger applies, with all required elements
      including why someone **may not** want to participate. Report as `UNVERIFIED` rather
      than `VIOLATION` where the institution file says enforcement is unconfirmed.
- [ ] **Time burden** stated per activity *and* as a total commitment. Per-activity durations
      without a total is a finding; so is a form where some activities have durations and
      others don't.
- [ ] Board-required **example statements** present, and none deleted relative to the
      approved form they descend from. Deleting an approved example is a regression — check
      against the approved source, not against taste.
- [ ] **No instruments inside the form.** Interview guides, survey items, agendas belong in
      their own appendix.
- [ ] Every genuinely distinct activity a participant is asked to do is named in the form.
      Cross-check against the protocol's data-collected list: **any data type collected from
      a participant must appear in a form that participant signs.** IRB #2's matching survey
      collected gender and disability status, listed them as research data, and never
      mentioned them in the student consent form — the two most sensitive fields in the
      protocol, consented nowhere.
- [ ] Closing block in the required form (signature vs. checkbox — see the conflict entry).
- [ ] Investigator does not sign, where the institution forbids it.
- [ ] Contact block complete: PI, and the compliance office.
- [ ] Voluntary / withdrawal language present, including what happens to already-collected
      data on withdrawal.
- [ ] **Consent precedes data collection** in the written sequence, not just in practice. If
      the Methods section orders a data-collecting activity before the consent item, the
      board will ask, whatever the real workflow is.
- [ ] One form per genuinely distinct activity; no separate form where the study consent
      already covers it.

## E. Confidentiality and data — institution file §6

- [ ] Vendors/platforms named where the institution requires naming (usually the
      confidentiality section and the consent forms' data-handling text) — and de-named in
      the narrative body where naming is only a liability.
- [ ] Whether IP addresses are collected, stated.
- [ ] Recording handling: platform-side deletion window, transcription by service or by named
      investigators, and **a destruction date with month and year** rather than "upon
      completion."
- [ ] **Recordings cannot be de-identified.** If the package says only "de-identified data
      retained indefinitely" and collects audio or video, the original recordings have no
      stated fate. This is an approvability issue, not a style one.
- [ ] Key file: paper or electronic, encrypted if electronic, and its deletion date.
- [ ] Retention periods stated with dates, and a worked example if the board expects one.
- [ ] Access assurance in the institution's required form.
- [ ] **Access clause wide enough to be true.** "Only the research team" is a violation
      waiting to happen if the study actually uses external transcriptionists, outside
      qualitative coders, or undergraduate assistants — and worse if the grant funds them.
      Check the budget and the personnel plan, not just the protocol's sentence.
- [ ] **Permission to publish de-identified quotes.** If the team quotes participants in
      papers — and it does — the consent forms must say so. Absent from every IRB #2 consent
      form until an audit caught it.
- [ ] **Future use and data sharing.** "Retained indefinitely" is not "may be shared."
      De-identified sharing, public-repository deposit, and secondary analysis each need
      saying if they will happen, and the recordings need explicitly excluding if they will
      not be shared.
- [ ] **Cross-study linkage**, if the program links data across protocols, with its own
      optional consent.
- [ ] Every processing location named — including tools the protocol treats as
      infrastructure. A matching or scheduling tool that holds participant data is a
      processing location.
- [ ] Group-confidentiality caveat where participants can see each other's disclosures.

## F. Compensation — institution file §7

- [ ] Amount and vendor stated.
- [ ] Handling on withdrawal stated.
- [ ] Extra credit, if used: alternative ways to earn it, and agreement from every instructor
      involved.
- [ ] **Tax thresholds computed against maximum cumulative payment per participant**, not
      per activity. Repeated interviews and longitudinal surveys add up; the threshold is
      about what one person can receive over the study. If the maximum stays under the
      threshold, say so explicitly so a reviewer doesn't have to work it out.
- [ ] Payment plausible for the burden asked — cross-check every duration in §D against its
      amount. An unpaid activity asking one to two hours is a finding even if the funder
      budgeted nothing for it.
- [ ] Worked totals where the board expects them.
- [ ] **Consistent across protocols reaching the same board.** Two protocols paying different
      amounts for the same activity is a question you get asked once, in writing. Worse if
      one of them claims to match the other.

## G. Review category and population — institution file §8, §9

- [ ] The review track requested is one the institution allows the investigator to request
      at all — most reserve the determination for the IRB.
- [ ] **Asserted exemption category consistent with the risks the protocol itself claims.**
      This is the highest-yield internal contradiction available: a protocol that describes
      professional-reputation or employability risk cannot rest on a category conditioned on
      the absence of that risk. Read the risk section against the category.
- [ ] Every vulnerable or undue-influence population the institution requires naming is named
      **and justified** — students and employees of the institution usually qualify.
- [ ] Minors: whether any participant could be under 18, and assent/parental consent if so.
      Includes populations reached incidentally through outreach.
- [ ] Populations in the recruitment section match the eligibility criteria and the consent
      forms. Leftover criteria from a base protocol are a standing invitation to be asked why
      they don't match.

## H. Multi-site and adjacent activities — institution file §10, §11

- [ ] For each site that is not the PI's institution: which arrangement — reliance agreement,
      local review, or determination — and does the protocol commit to something more
      expensive than needed?
- [ ] Site approval documentation where required.
- [ ] Whether a collaborating instructor or site investigator counts as research personnel
      for data-access purposes, and whether they hold their own copy of their students' data.
- [ ] **Adjacent activities that are not research need a written determination**, not an
      assertion. Outreach events, community groups, hackathons, and program evaluation that
      touch the same populations as the protocol are the likeliest place to collect data
      without coverage — especially where minors are involved. Ask for the determination
      before anything is collected, and state the boundary in the protocol so a reviewer
      doesn't have to guess.
- [ ] Staging check against §10: if the plan is "submit narrow now, modify later," does the
      later addition change enough dimensions to count as a **new study** rather than a
      modification? Adding a population *and* procedures usually does. Getting this wrong
      turns one amendment into a second full application, and it is better known now.

## I. Funder overlay

Only where a funder is involved, from the Phase-0 governing document.

- [ ] Public-access, open-data, or data-management commitments the funder imposes, reflected
      in the consent forms' sharing language. A federal award promising public data with
      consent forms that never mention sharing is a contradiction between two documents the
      same reviewers may both see.
- [ ] Participant-facing promises in the funded proposal that the protocol must support.
- [ ] Compensation the funder budgeted vs. what the protocol offers.
- [ ] Activities the funder's own text declares non-research — the protocol should say the
      same thing, and collect nothing from them.

---

## Findings format

One table per section, sections in order, only for sections that produced something. Then
the summary block.

| Rule | Quote | Source | Status | Where in package | Recommended fix |
|---|---|---|---|---|---|
| Personnel experience years | "Include the years of human subjects research experience for ALL personnel listed; if none, say 0 years." | umaine.md §2 → [instructions](url) | VIOLATION | Protocol §3, fourth entry | Add an experience line with a number |

**Status values, and they mean different things to the PI:**

- `PASS` — checked and conforming. Worth listing for the gates, because the point of the
  report is telling the PI what they don't need to re-check.
- `VIOLATION` — a stated rule, quoted, that the package breaks.
- `N/A` — the rule doesn't apply here, with one line on why.
- `UNVERIFIED` — could not confirm the rule, or could not confirm the package satisfies it.
  A first-class outcome, never a silent omission. Two flavors worth distinguishing: the rule
  exists but enforcement is unconfirmed, and the rule could not be found at all.

**Every `VIOLATION` carries a quote traceable to a URL in the institution file.** A finding
you cannot source is not a finding — it is the fabrication failure from
`institutions/umaine.md` §13 wearing a table row. If a rule seems obviously true but no page
says it, it is `UNVERIFIED`.

### Summary block

```
## Compliance — <institution>, <date>

Institution file: institutions/<slug>.md (fetched <date>)
Package checked: <every file, by name>
Sections run: A–I  ·  Not run: <section + why>

Hard gates (§A, §B): <n> checked, <n> violations   ← any violation here blocks submission
Violations: <n>   Unverified: <n>   N/A: <n>
Blocking vs. non-blocking: <split>

Nothing in this pass was edited. Fixes await PI instruction.
```

---

## What not to spend this pass on

- Rewording that doesn't change whether a rule is met.
- Polishing to zero findings. The operating posture applies here too: a submission with a
  couple of cheap, real, non-blocking findings gives reviewers something to catch. Hard
  gates are the exception — those get fixed, because a returned application costs a cycle
  and buys nothing.
- Arguing with the institution's rules. Quote and move on.
