---
name: irb-writing
description: Preserve-derive-verify workflow for drafting IRB protocols for YES Lab studies, funded or unfunded — reflection groups and any other project. Use this skill whenever the user mentions IRBs in any way - drafting a protocol, editing an existing IRB draft, listing which IRBs still need to be written, preparing consent forms or recruitment materials, comparing an IRB draft against a grant or study proposal, or responding to IRB reviewer feedback. Also trigger when the user mentions any grant or funded project (the CAREER grant or another funder) in connection with studies, human-subjects approval, protocol modifications, or "getting approval" for reflection groups, design workshops, interviews, or surveys.
---

# IRB Writing (YES Lab)

Getting protocols submitted is on the critical path for recruiting — a protocol that
sits in draft costs a semester of data. The goal of this skill is a *submittable*
draft, fast, that reuses previously approved language wherever it exists.

Division of labor: the AI does retrieval, adaptation, and verification. The human does
judgment — what the study was actually committed to, which risks are real, what the PI
wants scoped in. The PI reviews before every submission.

## Operating posture

Read this before drafting; it determines hundreds of small choices.

- **Submit and iterate.** The target loop is: AI drafts → human checks correctness →
  submit → board returns changes → same-day AI turnaround → brief review → resubmit.
  Optimize for cycle time, not for a flawless first submission (Greg, 2026-07-27).
- **Don't model a hostile board.** Writing defensively against an imagined adversarial
  reviewer wastes time and inflates the protocol. Write for reasonable people.
- **Leave findable problems.** Reviewers who find nothing will invent something. A few
  obvious, cheaply-fixed issues give them something real to catch. Do not sand the
  draft to a mirror finish.
- **Ignore inconsequential AI-isms.** Over-hedged phrasings and needless qualifiers
  that don't change meaning are not worth the edit pass.
- **Ship narrow, modify later.** If a component (custom software, a student-facing
  study arm) risks slowing approval, submit without it and file a modification or a
  separate protocol. Prefer two fast approvals over one slow one.

## Ground rules

### 1. The approvability test — the main filter

**Include a detail only if it affects whether the research is ethical and approvable.**
Everything else comes out.

Over-specification is not just verbose, it is *risky*: any concrete number becomes a
commitment you can violate. If the protocol says groups meet for 10 weeks and a group
meets for 12, that is now a protocol deviation for no benefit.

Apply it like this:

| Instead of | Write |
|---|---|
| "meetings run 10 weeks" | "meetings run over the course of a semester" |
| "stored in Google Drive" | "stored in a secure cloud platform" |
| "held over Zoom" | "held online" + the properties that matter ("connections are encrypted") |
| a per-meeting agenda | "groups complete an icebreaker and then set their own agenda" |

**Name properties, not vendors.** Vendors change; a named vendor is a modification
waiting to happen.

The counterweight: the board *does* require certain specifics, and they live in the
consent form. See `references/board-rules.md` for the required-inclusion list before
cutting anything from a consent document.

### 2. Preserve before you write

Prior approved documents are the template. The board has already told us what it
accepts in this exact program, and that knowledge is not in the model's head — an AI
drafting fresh does not know the shape of *this* board's protocol, and does not know
what is safe to cut. Divergence in format from previously approved language is a signal
that the approved version wasn't used as input.

### 3. No invention — everything traces to a governing source

Never invent procedures, populations, instruments, compensation amounts, or data flows.
Every substantive claim in the protocol traces to one of:

- the **governing document** for this study (see Phase 0 — a grant proposal, a study
  design brief, a dissertation proposal, a pre-registration, or a PI-provided plan),
- a **prior approved protocol**, or
- an **explicit PI or researcher instruction** in the working session.

If a required field has no answer in any of those, mark it
`[PI DECISION NEEDED: ...]` and surface it in the handoff summary. Do not fill the gap
with something plausible — a plausible invention in an approved protocol is a
commitment nobody agreed to.

### 4. Define terms once

Define a construct (e.g. "outcomes") once, near the top, then use the term throughout
rather than re-enumerating its contents at each mention. Re-enumeration is how numbers
and lists drift out of sync across a document.

### 5. Never duplicate content across sections

A specifically-AI failure mode: something already covered under confidentiality gets
re-bulleted under procedures, then again under risks. Duplication triples the surface
area for inconsistency and reviewers notice the mismatch, not the coverage. One
canonical location per fact; cross-reference if needed.

### 6. Scope hygiene

Strip language belonging to a scope this protocol doesn't have. An out-of-class protocol
should carry no course, enrollment, grading, or graduation language; a protocol with no
non-consenting participants should carry no non-consenting-participant procedures.
Leftover language invites a reviewer to ask why eligibility criteria don't match.

## Working format

The board wants **Word documents**. Round-tripping through Google Docs destroys
formatting, and the damage scales with how bullet-heavy the document is. Work in
`.docx` end to end (see the `docx` skill for reading and editing them), and keep
paragraph-structured prose over deep bullet nesting where either would do.

## Phase 0 — Provenance (do not skip; this is where hours get lost)

Starting from the wrong base document silently discards approved language.

1. **Establish the governing source.** Ask, and do not assume:

   > Is this study governed by a grant or funded project? If so, which document is
   > authoritative, and where is it? If not, what should I treat as the description of
   > the planned research?

   Three cases, and they change Phase 4:

   - **A grant or funded project** — get the specific proposal file and its version. Do
     not assume it's the CAREER grant just because most YES Lab work is; other funders,
     subawards, and collaborators' grants all impose their own promised activities.
   - **An unfunded or self-directed study** — ask for whatever stands in: a study design
     brief, dissertation proposal chapter, pre-registration, or a prior paper the study
     extends. If nothing written exists, capture the plan from the researcher in the
     session and write it down as a short brief; that brief becomes the governing source
     and gets handed over with the draft, so later verification has something to check
     against.
   - **Multiple governing documents** — e.g. a grant plus a collaborator's protocol.
     List them all and note which governs where they conflict. Ask if unclear.

   Record the answer at the top of the working draft. Every later reference in this skill
   to "the governing document" means whatever was established here.

2. **Ask which file is the base protocol.** Do not infer it from the most recent email —
   email threads and internal drafts diverge from the approved version. Ask the PI
   directly, and prefer asking over guessing: a 2-minute question beats a 4-hour rewrite.
   If there is no prior protocol to build from, say so explicitly in the handoff, because
   it means the draft has no approved-language backstop and needs closer PI review.
3. **Ask what else would help.** Literally: "what sources of data or files would be
   helpful for this task?" Prior interview consent forms, approved modifications, related
   protocols in the same program, and the governing document are all commonly-forgotten
   inputs.
4. **Locate the current consent forms.** In the master protocol document, consent forms
   accumulate chronologically at the bottom. To find the newest version of one, search
   the term (e.g. "interview") from the top of the document, then jump to the *last*
   match.
5. **Snapshot the base.** Copy it, or commit it, before any edits — Phase 4 needs a
   before/after diff, and without one, silently dropped sections stay silent.

Record all inputs used at the top of the working draft — governing document, base
protocol, and supporting files, each with version or date — so the PI can see what the
draft was built from without asking.

## Phase 1 — Mark up the base, then edit

Before changing anything, tag every section of the base document:

- **KEEP** — approved language that carries over verbatim. Do not touch. Do not
  "improve." Board-required example statements live here.
- **ADAPT** — approved structure, new specifics for this study.
- **CUT** — fails the approvability test, or belongs to a scope this protocol lacks.
- **DEFER** — content coming from another file or from screenshots.

For every DEFER, leave an explicit inline comment: *"everything from [file] goes here."*
Otherwise the PI spends review time on text you were about to replace — that happened,
and it wasted a review pass.

Keep the markup visible in the draft you hand over, so the reviewer knows where to look.

## Phase 2 — Draft the consent form first

Write the consent form(s) completely, then derive the protocol narrative from them. The
consent form is where the board's demand for specificity actually originates, so
settling it first fixes the level of detail for everything downstream. Doing it in the
other order produces a protocol that over-specifies and a consent form that
under-specifies.

Read `references/board-rules.md` for what this board requires in a consent form, what
must stay out of it, and how many consent forms a study needs.

Sanity-check compensation against time asked: it must be plausible payment for the
burden. $10 for a 60-minute interview is not; ~$25 is the floor for that (Greg,
2026-07-27).

## Phase 3 — Derive the protocol narrative

There is a minimum viable shape, and it is short:

1. A paragraph on group reflection and the evidence base.
2. What we are doing now.
3. The research questions.
4. Methods — lifted from the prior approved protocol, generalized if needed.
5. Data management, stated as properties (secure, access-controlled, retention period).

Reuse the approved *description of the meetings* rather than authoring new agendas.
Generalizing approved language is fine; replacing it is not.

Generate alternative phrasings only for genuinely contested judgment calls — scope
drawn broadly for future coverage vs. narrowly for fast approval, for instance — and
cap it at two options with a one-line trade-off each. Do not generate variants of
sections where approved language already exists; that is churn, not choice.

## Phase 4 — Verification (mandatory; produce the report)

Three mechanical passes. Run them, iterate on what they surface, and **hand the report
to the PI alongside the draft** — it tells them what not to re-check.

1. **Alignment diff** against the base document: what is similar, what differs, and
   specifically whether anything marked KEEP was dropped or altered.
2. **Source coverage** against the governing document from Phase 0: what it plans that
   the protocol omits; what research details should be in the protocol but aren't; what
   detail is in the protocol that isn't needed. If the governing source is a brief
   captured in-session rather than a formal document, check against that brief — the pass
   still runs, it just has a lighter source.
3. **Internal consistency**: every repeated fact — participation cycle counts, session
   lengths, participant numbers, compensation, retention periods — reads identically in
   the protocol, the consent forms, and the recruitment materials.

Full prompts and the checklist are in `references/review-protocol.md`. For detailed
document-vs-document comparison, a document-grounded tool (NotebookLM-style) beats
plain chat.

## Phase 5 — Handoff

Deliver: the draft `.docx` files, the verification report, a list of every
`[PI DECISION NEEDED]` item, and a one-line note on what the draft assumes.

For anything as large as a full protocol, **create a Linear task and assign it to the
PI ahead of the review meeting** — reviewing cold during a meeting is slower for
everyone.

When the board responds: turn the changes around the same day, review briefly,
resubmit. Do not batch board feedback into a weekly cycle.

## The IRB backlog

Maintain `references/irb-backlog.md` with status per protocol, and record which governing
document each entry answers to. The entries below are the current reflection-groups
program under the CAREER grant — they are examples of the format, not a fixed scope.
Submit these separately:

1. **Reflection groups outside of classes** — no course involvement at all.
2. **Instructor collaboration protocol (CAREER)** — running reflection groups in other
   instructors' courses, explicitly including co-design workshops with instructors (a
   design workshop with instructors *is* research). This one is large and will take
   longer to clear, so consider submitting the design-workshop portion first with
   explicit language that participation does not obligate instructors to use reflection
   groups in their courses, and that student-facing research will come via a
   modification or separate protocol. Note that the CAREER grant covers the AI work as
   well as reflection groups — workshops may be about reflection groups, about designing
   AI integration in courses, or about designing reflection around AI.

Derive further entries from the activity table of each governing document: any planned
human-subjects activity not covered by an existing or backlogged protocol gets an entry.
When asked "what IRBs do we still need," ask which project or grant they mean if more than
one is active, then answer from this file and update it.

## Knowledge base (build once; refresh if >1 semester old)

Maintain `references/irb-knowledge-base.md`:

1. **Prior approved YES Lab protocols** — section outlines, consent language, risk
   framing, data-management plans. Highest-weight input.
2. **An activity table per governing document** — every planned human-subjects activity
   as a row: activity, population, data collected, instruments, timeline, aim, and which
   protocol covers it. This table is the backbone of every protocol and the basis of the
   Phase-4 coverage check. Keep one table per grant or project rather than merging them,
   so coverage checks stay scoped to the right authority. The CAREER grant table is the
   one that exists today; add others as projects arrive.
3. **Current institutional requirements** — fetch the University of Maine Office of
   Research Compliance submission requirements, forms, review categories, and CITI
   prerequisites fresh rather than from memory.
4. **Board behavior log** — what this board has accepted, questioned, or required
   changed, accumulated across submissions. Weight this above generic internet guidance
   on IRB writing; exemplars from this board beat best-practice advice when they
   conflict.

## Human judgment checkpoints (do not delegate)

- Which base document to start from
- Scope decisions: what goes in this protocol vs. a later modification
- Every `[PI DECISION NEEDED]` item
- Compensation amounts
- Final pre-submission review by the PI

## Where this skill lives

This belongs in the shared lab skills repository, not a personal one — the point is that
nobody in the lab writes their own IRB skill from scratch, and that it can be dropped
into future projects.

## Self-revision

After each submission and each board response, log what the board accepted, questioned,
or required changed into the board-behavior log, and revise this file. Log tasks the AI
handled badly in `ai-capability-log`.

A stronger version of this loop, worth building: after a working session, take the
retrospective plus the interaction history, re-run the original task using the revised
skill, and compare the result against what was actually produced and approved. That
tells you whether the revision genuinely improved the skill instead of just feeling like
it did.
