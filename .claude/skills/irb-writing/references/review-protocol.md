# Verification protocol (Phase 4)

Three passes. Each produces findings; iterate on the draft until a pass returns nothing
material. Then compile the findings into a short report and hand it over **with** the
draft — its purpose is to tell the PI which parts they don't need to re-check.

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

Also:

- [ ] Defined terms (e.g. "outcomes") are defined once and used consistently, not
      re-enumerated.
- [ ] No fact appears in two sections with different wording that implies different
      commitments.
- [ ] `[PI DECISION NEEDED]` markers are all still present and collected in the summary
      (none silently resolved by the AI).

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
Base protocol: [file, version/date, how confirmed; or "none — drafted fresh"]
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
