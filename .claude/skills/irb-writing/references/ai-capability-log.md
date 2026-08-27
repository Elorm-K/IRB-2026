# AI capability log

Tasks the AI handled badly on real IRB work, and the countermeasure. Referenced from
`../SKILL.md` "Self-revision." Add an entry when the AI produces something the PI had to
catch — the point is that the next run doesn't repeat it.

Format: what happened · why it happened · the countermeasure, and where it now lives.

---

## 1. Derived approved language instead of copying it, because the source file was unreadable

**What happened.** All generative-AI wording in IRB #2 v4 was written from the grant plus
IRB #1's consent structure, and presented as if that were the only option. Approved AI
consent language existed the whole time — three board-approved forms in the January 2026
mod of the `2023_07_10` protocol. The file was in `~/Downloads`, where macOS blocks tool
access, so it was recorded as "not accessible" and the draft moved on without it. Once the
file was moved into the repo it opened fine.

**Why.** An unreadable input was treated as a missing input. The draft continued rather than
stopping to ask for the one thing that would have changed its content most.

**Countermeasure.** An unreadable governing or approved-language file is a blocker, not a
caveat: ask for it to be moved into the project and wait. `SKILL.md` Phase 0 already says to
ask what other files would help; the addition is that "I can see it but cannot open it" gets
escalated immediately, and any wording derived rather than copied is labelled as derived in
the verification report so it can be replaced later. Ground rule 2 ("Preserve before you
write") is the rule that was effectively broken.

## 2. Chose the base document by inference instead of asking

**What happened.** IRB #2 v4 was built on `v3_aligned` because it was the richest text. The
PI was never asked to confirm it, and a live Google Doc forked from v2 carried later hand
edits that then had to be merged in a second pass.

**Why.** Phase 0 says to ask which file is the base and not to infer it. The step was skipped
because a plausible answer was available.

**Countermeasure.** Phase 0's base-document question is not optional even when the answer
looks obvious, and where it was not asked, the verification report must say so under
Assumptions rather than presenting the choice as settled. This one is already logged as an
Assumption in `IRB2_v4_VERIFICATION_REPORT.md`; the lesson is that it should not have needed
to be.

## 3. Standalone attachment files drifted from the protocol appendices they duplicate

**What happened.** `IRB2_ConsentForms_Instructor_and_Student.docx` stayed at v1 while the
protocol's appendices went through v2 and v3 — old protocol title, a stale contact address, a
missing team member, no Compensation section, and an unresolved `[PI DECISION NEEDED]` marker
still in the text. If those files had been the ones attached, the submission would have
contained a live decision marker.

**Why.** The same content lived in two files with no generation relationship, and every
verification pass read the protocol.

**Countermeasure.** Standalone files are **generated** from the same source parts as the
protocol appendices and verified byte-identical after normalization, never hand-edited in
parallel. And Pass 4 runs on the **assembled package** — every file that will actually be
attached — which is now stated at the top of `compliance-check.md`.

## 4. Fabricated a policy quotation in an automated page summary

**What happened.** During the UMaine requirements research, an automated summary of a policy
page produced a fluent sentence saying a single protocol may cover "multiple participant
populations or study arms" given "coherent scientific objectives and unified ethical
oversight." No UMaine page contains it. It was caught only by extracting the policy PDF's
text and searching for the phrase.

**Why.** A summarization step was trusted for a load-bearing rule. The invented sentence was
more quotable and more confident than anything the real page said, which is exactly what made
it dangerous — it was about to justify a scope decision.

**Countermeasure.** `institution-research.md` §3: exact quotes with URL and fetch date, and
anything unsourced is `UNVERIFIED` rather than asserted. `compliance-check.md` requires every
`VIOLATION` to carry a traceable quote for the same reason. The correction itself is retained
in `institutions/umaine.md` §13 as a standing example rather than deleted.

## 5. Whole rule layer was missing from verification until an external audit supplied it

**What happened.** Phase 4 had three passes — base-document alignment, grant coverage,
internal consistency — and no pass checking the draft against the reviewing institution's
rules. Nine substantive findings on IRB #2 v4 came from an independent audit rather than from
the skill: no permission to publish de-identified quotes, no future-use/data-sharing
provision, an access clause too narrow for the coders the grant funds, no written
not-research determination for outreach involving minors, an undisclosed processing location,
and a dual-role conflict, among others.

**Why.** The verification protocol checked the draft against its sources and against itself,
and assumed institutional conformance came from starting from an approved base. That holds
only for content the base already contained.

**Countermeasure.** Pass 4 (`compliance-check.md`), and the per-institution rule files it
runs from. Every one of those nine findings maps to a line in sections C–H. Added 2026-07-28.

## 6. Added generic consent-form content that no approved form contains ("AI drift")

**What happened.** The IRB #3 consent forms accumulated sections and statements that appear
in consent forms generally but in none of this board's approved forms — data-sharing
assurances, fairness guarantees ("we won't treat you differently if you don't participate"),
restatements of confidentiality under other headings, and meta-explanations of the study's
structure. The PI spent a session (2026-08-11) hand-deleting them: "none of these things are
in any of the IRBs… if you don't see it in the existing consent forms, it doesn't belong
there," and separately judged "the AI is really bad at working on consent forms. It wants to
add all these things… the average consent form is not equal to the consent forms that our
IRB wants."

**Why.** The model's prior for "good consent form" is an average over many institutions, and
it fills silence with best-practice content. Some additions were also risky, not just noisy:
they could have changed the risk categorization, and one was a blanket commitment the lab
could not keep.

**Countermeasure.** Provenance rule in `SKILL.md` ground rule 3: consent-form content must
trace to an approved form of this board; anything else needs an explicit source or comes
out. Phase 1 markup (KEEP/ADAPT/CUT) applied to consent forms specifically. The
no-new-risk-categories rule sits alongside it. The deeper fix the PI named (2026-08-17):
feed these transcripts back into the prompt — which is this file and `board-rules.md`.

## 7. Over-applied reviewer requests and volunteered unrequested detail in a response round

**What happened.** On the IRB #3 response round (2026-08-17): a comment asking for recording
details in the methods narrative was answered by also adding recording details to the
invitation email; reviewer-supplied text was expanded into a longer paraphrase instead of
pasted; IP-address statements were added in places the instructions don't ask for them. Each
drew a PI correction, and each enlarged the review surface for the next round.

**Why.** The model treats a reviewer comment as evidence of a global gap and "fixes" it
everywhere, and treats supplied text as a draft to improve. Both instincts are wrong here:
the board wants per-location compliance, verbatim.

**Countermeasure.** `board-rules.md` §5c (scoped compliance): change only the anchored
location, paste supplied text verbatim, take the simpler option when offered one, add
nothing unrequested, expect and tolerate board self-contradiction. Referenced from
`SKILL.md` Board-response rounds.

## 8. Rendered a payment-channel restriction as "no compensation for employees"

**What happened.** The ORA gift-card rule ("gift cards may not be used to compensate
employees") was drafted into IRB #3 v2 — and recorded in this skill's backlog — as "UMaine
employees receive no compensation." The PI caught it in the submitted-draft review
(2026-08-17): "it's not going to work to be like, if you're a UMaine person, we're not going
to pay you. That sounds pretty unfair." The correct reading: same amounts, paid through
payroll instead of a gift card. The policy digressions written into the application also
actively confused the reviewers.

**Why.** The harshest consistent reading of a policy fragment was adopted without asking
what the policy is for, and UMaine's payment documents are themselves partially
contradictory (thresholds). A denial-of-payment conclusion should have been a
`[PI DECISION NEEDED]`, not a drafted sentence.

**Countermeasure.** `board-rules.md` §4 correction block and `institutions/umaine.md` §7:
a rule limiting a payment mechanism is not a rule limiting payment; any reading that denies
or reduces payment to a participant class gets verified with the business office / grant
administrator before it enters a draft. State the outcome in the protocol, not the policy
analysis.
