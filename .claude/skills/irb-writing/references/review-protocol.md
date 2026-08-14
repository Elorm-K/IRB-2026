# Verification protocol (Phase 4)

Four passes. Each produces findings; iterate on the draft until a pass returns nothing
material. Then compile the findings into a short report and hand it over **with** the
draft — its purpose is to tell the PI which parts they don't need to re-check.

The passes check different things and none substitutes for another:

| Pass | Checks the draft against | Lives in |
|---|---|---|
| 1 | the base document it was built from | here |
| 2 | the governing document (grant, brief, proposal) | here |
| 3 | itself | here |
| 4 | the reviewing institution's published rules | `compliance-check.md` |

Pass 4 is the one that was missing. Passes 1–3 assume institutional conformance comes from
starting from an approved base, which holds only for content the base already contained.

For document-vs-document work, prefer a tool that grounds answers in the documents
themselves (NotebookLM-style) over plain chat, which drifts on long comparisons.

---

## Pass 1 — Alignment diff against the base document

Prompt shape:

> Align these two documents and show which parts are the same, which differ, and which
> exist in only one of them. Do not summarize — enumerate section by section.

Then specifically check:

- [ ] Every section marked **KEEP** in Phase 1 appears unchanged. This is the highest-value
      check in the whole protocol: silent deletion of approved language is the failure mode
      that has actually cost time.
- [ ] Every section marked **CUT** is gone, and nothing was cut that wasn't marked.
- [ ] Every **DEFER** placeholder carries its "content comes from [file]" comment.
- [ ] Format of reused documents (interview consent form especially) matches the approved
      version. A format divergence means the approved version wasn't used as the base.

## Pass 2 — Source coverage

Run against the **governing document established in Phase 0** and its activity table.
Substitute the actual document name into the prompt rather than saying "the grant":

> Compare this protocol against [governing document]. (a) What does [it] plan that the
> protocol does not cover? (b) What details of the research should be in the protocol but
> are missing? (c) What is in the protocol in too much detail, or not needed at all?

Then:

- [ ] Every planned human-subjects activity in scope for this protocol is covered.
- [ ] Every activity the governing document plans that this protocol deliberately excludes
      is listed in the handoff note as deferred to a modification or a separate protocol.
- [ ] Outcome measures match those already validated in prior work in this program — a PI
      review item; flag it explicitly rather than resolving it.
- [ ] The protocol promises nothing the governing document doesn't support. Over-coverage
      is as much a problem as under-coverage: it commits the lab to work nobody funded or
      planned.

### If the governing source is a grant

- [ ] All arms of the grant are represented, not just the most familiar one. A grant
      covering two lines of work (e.g. reflection groups *and* AI integration) will have
      activities in both, and the less-salient arm is the one that gets dropped.
- [ ] Where a companion protocol already covers part of the grant, note which one, so a
      reviewer doesn't read an apparent gap as an omission.

### If there is no grant

The pass still runs — against the study design brief, dissertation proposal,
pre-registration, or the in-session brief captured in Phase 0. Additionally:

- [ ] The brief itself is attached to the handoff, since it is the only record of what the
      protocol was checked against.
- [ ] Anything the brief leaves open is marked `[PI DECISION NEEDED]` rather than resolved
      by inference. An informal brief is thinner than a grant, so the temptation to fill
      gaps is higher and the cost of guessing is the same.

### Output shape

Do not deliver Pass 2 as prose. This structure came out of
`irb2-instructor-collaboration/reports/IRB2_GapAnalysis_vs_CAREER_grant.md` and is the
format that let the PI act on 30+ findings without re-reading the grant:

1. **Documents compared**, by path and version, and **what could not be verified**, stated
   up front rather than buried. A finding derived from an inaccessible source is labelled
   as inferred, not asserted.
2. **What's left out** — a table: item · where in the governing doc *and* where in the draft
   (quote both) · issue · recommendation.
3. **Missing research detail** — same table shape. Things that are in scope and present but
   under-specified: burdens without durations, data types with no consent, populations with
   no total N.
4. **Too much detail** — same shape. Over-specification is a commitment you can violate, so
   this section is not cosmetic.
5. **Also check** — a short run of targeted questions this particular protocol raises
   (is the defined term used consistently? is scope drawn where the title claims? is there
   one consent form per distinct activity, and does consent come first?).
6. **What was verified as *not* dropped** — and if there were no KEEP markers to check
   against, say that explicitly instead of implying a clean check.
7. **Top N to fix before submitting**, ranked, each with the specific locations to edit.

Quote the governing document rather than summarizing it. A recommendation that quotes the
grant clause it comes from survives disagreement; a paraphrase gets argued with.

## Pass 3 — Internal consistency

Repeated facts must be identical everywhere they appear — protocol body, each consent
form, recruitment materials, appendices. Build a table and check it mechanically:

| Fact | Protocol | Consent | Recruitment |
|---|---|---|---|
| Participation cycle count | | | |
| Meeting frequency / duration | | | |
| Study duration | | | |
| Number of participants | | | |
| Compensation per activity | | | |
| Data retention period | | | |
| Storage description | | | |
| Interview length | | | |

Then a second table, **method × attribute** — one row per data-collection method the
narrative names, follow-ups included (a follow-up survey is a method, not a footnote):

| Method | Mode/venue + named platform | Recording + agreement terms | Data collected | Compensation (or "none") | Consent-form bullet | Own recruitment script | Instrument appendix |
|---|---|---|---|---|---|---|---|
| Survey | | | | | | | |
| Workshop | | | | | | | |
| Consultation | | | | | | | |
| Interview | | | | | | | |
| Follow-up survey / interview | | | | | | | |

Every empty cell is a finding. Most of the IRB #3 ORA round (2026-08-14) was empty cells
in this matrix: consultations had no recruitment script, follow-ups had no instrument
appendix or stated frequency, compensation was stated only for the compensated methods,
and no Methods item named its platform. The board-level rules are `board-rules.md` §5b;
this matrix is how they get checked mechanically. Recording rows also need the *terms*:
whether agreeing to the recording is required to participate, or notes are the fallback.

Also:

- [ ] Defined terms (e.g. "outcomes") are defined once and used consistently, not
      re-enumerated.
- [ ] No fact appears in two sections with different wording that implies different
      commitments.
- [ ] `[PI DECISION NEEDED]` markers are all still present and collected in the summary
      (none silently resolved by the AI).
- [ ] Standalone attachment files (consent forms, recruitment texts) agree with the
      protocol's own appendices. Generate them from the same source parts and verify
      identical after normalization — do not hand-edit both. A standalone consent file once
      sat two versions behind the appendix it duplicated, still carrying the old protocol
      title and a live decision marker.
- [ ] Every "Appendix X" reference resolves to an appendix that exists, checked
      **mechanically** — grep the built text for `Appendi` and compare against the actual
      appendix list — and the lettering has no gaps. "Appendices K and Li8" survived to
      the IRB #3 submission and reached the reviewer.
- [ ] Consent forms and recruitment texts speak in second person throughout — a stray
      "the participant's" gets flagged (board-rules §5b).

## Pass 4 — Institutional compliance

The full checklist is `compliance-check.md`. In brief: the **assembled package** — protocol,
every appendix, every standalone file that will actually be attached — against
`institutions/<slug>.md` for the board recorded in Phase 0.

- [ ] The institution file exists and is less than a semester old. If not, build or refresh
      it with `institution-research.md` **before** running the pass. Never check against
      remembered requirements.
- [ ] Sections A–I of `compliance-check.md` run, and any section skipped is named with a
      reason.
- [ ] Every `VIOLATION` carries an exact quote of the rule and a traceable URL. An
      unsourceable finding is `UNVERIFIED`, not a violation.
- [ ] Hard gates (§A, §B) separated from everything else — those are the ones that get an
      application returned unread.
- [ ] The draft applies every `board-rules.md` entry **newer than the base protocol it was
      built from** — a rule learned on a sibling protocol's review round applies to this
      one immediately, not after this one's own review restates it. The published-rules
      check above does not catch these, because board behavior is not published.
- [ ] Nothing was edited. This pass reports; the PI decides.

Where more than one board reviews the study, run the pass once per board against the
documents that board will see.

## What not to check

Do not spend passes on:

- Inconsequential phrasing artifacts. If rewording doesn't change meaning or
  approvability, leave it.
- Polishing toward a zero-finding submission. Some easily-fixed issues should survive to
  submission so reviewers have something real to catch.
- Defensive elaboration against hypothetical objections. If a reviewer raises it, answer
  it then, same day.

---

## Report format

Keep it to one page:

```
## Verification report — [protocol name], [date]

Governing source: [grant / brief / proposal — file, version/date; or "none, brief attached"]
Reviewing IRB(s): [institution(s); rules file + fetch date]
Base protocol: [file, version/date, how confirmed; or "none — drafted fresh"]
Package checked: [every file that will be attached, by name]
Other inputs: [files]

### Alignment vs. base
- Sections preserved verbatim: [list]
- Sections adapted: [list + one-line why]
- Sections cut: [list + one-line why]
- Deferred (content from elsewhere): [list]

### Source coverage (vs. [governing source])
- Covered: [activities]
- Deliberately deferred: [activities → which future protocol/mod]
- Gaps needing PI input: [list]

### Consistency
- Facts checked: [n]; discrepancies found and fixed: [n]
- Remaining known discrepancies: [list, or none]

### Compliance (vs. [institution], rules fetched [date])
- Hard gates: [n] checked, [n] violations   ← any violation here blocks submission
- Blocking findings: [list, each with the rule quoted]
- Non-blocking findings: [list]
- Unverified: [list — rule not found, or conformance not confirmable]
- Nothing in this pass was edited; fixes await PI instruction

### PI decisions needed
1. ...

### Assumptions this draft makes
- ...
```

---

## Skill-improvement loop (post-submission retrospective)

After a submission cycle closes, run this rather than only editing the skill from memory:

1. Take the working session's retrospective plus the interaction history for the task.
2. Re-run the original task using the revised skill, from the same starting inputs.
3. Compare the output against what was actually produced and submitted, and against
   whatever the board then required changed.
4. Keep the skill revisions that measurably close the gap; discard the ones that only
   felt like improvements.

This is what distinguishes a skill that accumulates real board knowledge from one that
accumulates plausible-sounding advice.
