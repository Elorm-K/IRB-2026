# Fall 2026 — semester plan

**Governing document:** NSF CAREER Award 2544192 (`inputs/grant/FINAL NSF_CAREER_25_Nelson.pdf`),
Year 1. **PI direction:** Greg Nelson, advisor meeting 2026-07-22
(`inputs/meetings/Advisor Meetings transcript_2026-07-22_12.12.04.txt`).
**Drafted:** 2026-08-25.

Every item below traces to a grant section or to the 2026-07-22 meeting. Nothing here is
invented scope.

---

## The PI's direction, in his words

> "It is really a super critical time for the reflection group stuff… we should target having
> like 10 faculty members to work with, like implementing reflection groups in their classes
> in the fall… To do that, we'll need to recruit at least 25 people. And to recruit 25 people,
> we're going to send out messages to several hundred people."
>
> "Reflection groups are the most important research that I've ever done that you've ever done."
>
> "Once we get those IRBs submitted, we need to gear up. Send out like the longitudinal surveys
> to everybody that has done the reflection groups and comparison groups so far… we made a
> mistake and thinking that those things weren't approved before, but they are, so we can just
> send them out."
>
> "So that's what I would say you should focus on."

**Target: Task 1, instructor stream.** Not Task 2, not the Task 3 tool.

## The one re-timing

"10 faculty implementing in the fall" was said on 2026-07-22 aiming at a semester that starts
in days. It is no longer reachable: fall syllabi are set, and IRB #3 has not gone back to ORA.

The reachable version, which matches the grant's own cadence better — §3.1.2 describes a yearly
cycle of survey → workshop → adoption, not same-semester adoption:

**Fall = recruit and run the workshops. Spring 2027 = 10 faculty implementing.**

**The hard date is mid-November**, when spring syllabi lock — not the start of the semester.
Everything in Track C is scheduled backward from it.

---

## Track A — Collect now, under approvals that already exist

### A1. Send the longitudinal follow-up surveys — do this first
**Grant:** §3.1.3 ("deepen the evaluation step of our preliminary work with follow-up
interviewing and surveying the students from that course and also other students who did not
take that course for comparison"), §3.1.5.
**Approval:** already covered — `inputs/approved-protocols/2024_08_09 Nelson_MOD_2_Jan_2026_FINAL.pdf`,
whose Sept-2025 modification also approved **$10 per longitudinal survey**. No new submission needed.
**Timing:** out by week 2; reminder cadence through the semester.

- Recipients: all prior reflection-group students plus comparison-section students.
- Core instrument (§3.1.5): Self-reflection and Insight Scale (20 items), self-directed learning
  scale (25 items), psychological safety scale (7 items), one-question STEM professional identity measure.
- Year-1 wider measure pilot (§3.1.5, "In Year 1 we will pilot on the pre and post course surveys
  a wider variety of measures"): the candidates listed in `irb1-reflection-groups/IRB1_SUMMARY.md`
  decision 11 — Short Big Five, BRS, CD-RISC-2, Personal Growth & Development Scale.
- Retention practices from §3.1.6: thank participants sincerely, follow up regularly, make
  responding easy. The grant's ≥80% retention target depends on this.

**Why first:** it is the only item on the whole list that degrades if you wait. Every semester of
delay is attrition on a longitudinal cohort that cannot be re-recruited.

**Verify before sending:** that the wider measure set sits inside the approved instrument
appendices. If any instrument is not already approved, send the core set now and add the rest by
modification — do not hold the send-out for it.

**Boundary to hold:** surveys only. Follow-up *interviews* with these same students are not
covered by any protocol (backlog #3) — they arrive via A2/B5. Do not let the send-out grow an
interview invitation.

### A2. Re-analyse the existing video-reflection corpus — background thread
**Grant:** §3.2.2 ("First, we will interview students who did the video reflections… We will
also analyze their videos and actual written reflections from the assignment").
**Approval:** unresolved — see Open Questions. Answer that before touching the data.

By the grant's own account (§3.2.1) the published pilot analysis covered only Articulate Learning
questions 3, 6 and 7, chosen "to balance a manageable set of data to analyze." The Describe and
Examine tables, the time-category estimates, the comparison columns and the videos themselves are
collected and un-analysed. No new collection, so no new approval — provided the original approval
covers re-analysis.

---

## Track B — Unblock the pipeline

### B1. IRB #3 v2 back to ORA — week 1
Five open decisions in `irb3-instructor-adoption/reports/IRB3_v2_ORA_RESPONSE_REPORT.md`:
consultation materials kept or not; whether workshop recording is a participation requirement;
no compensation for consultations; follow-up cadence; and the reviewer's separate UMS-campuses
email, which only the PI can answer. Then strip the `{{...}}` markers, rebuild with
`tools/build_docx.py`, send.

**This is the gate for all of Track C.** Nothing in the funnel can start until #3 is approved.

### B2. IRB #2 v9 back to ORA — weeks 1–2
Two blocking items, both PI calls: Chris Dufour on the protocol or off it (he is on the cover
page, absent from §3 and all four consent forms), and the cover-page start date is still a
bracketed placeholder — the application is returned incomplete without it. Then three open items:
instructors per workshop (drafted "approximately 5 to 15"), the UMaine-employee compensation
exclusion and its recruiting cost, and Appendix H's missing AI-measure items.

While in there: §7 asserts a professional-reputation risk to instructors, which forecloses exempt
category 2(ii). The cover page's review-category selection has to agree with that.

### B3. Reconcile the #2 / #3 instructor-stream overlap — week 2
Both protocols cover the same instructors, the same workshops, the same surveys. Two live
protocols at one board covering one population is what a reviewer catches, and it costs a round.
Unresolved in the repo — see `irb3-instructor-adoption/README.md`.

### B4. IRB #1 — submit narrow — weeks 2–5
**Grant:** §3.3.2 ("To help gather requirements, in Year 1 we will invite students from the
preliminary ethics course (mostly graduated)… for ongoing reflection groups").

Two gates: confirm which of the three candidate files is live (evidence points cleanly at
`IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx`; needs a human's yes, then
the other two move to `archive/`), and work the 12 decisions in `IRB1_SUMMARY.md`.

Only about eight are Year-1 load-bearing. Drop from the critical path:

- **Decision 4, recruiting company** — Year 3 (§3.2.4), and the live draft already says none is used.
- **Decision 5, video module** — answer "out." Year 1's video work is course-based, so the
  out-of-class protocol would not cover it anyway.
- **Decision 2a, the matching tool** — the tool is Year 2 (§3.3.2, "Starting in Year 2, supported
  by our matching tool"). Year-1 groups are matched by hand, as in the preliminary work. Scope the
  tool out and add it by modification.

**Do decision 9 first**, because it is verifiable rather than a judgment call: whether the approved
course protocol's consent permits recontacting alumni to invite them into a new study. Year 1's
entire Task-3 activity is that recontact. If the answer is no, the recruitment channel has to be
rebuilt before submission, not after. The file is in `inputs/approved-protocols/`.

### B5. One course-protocol modification carrying three things — weeks 6–10
**Grant:** §3.2.3 (video reflection), §3.1.3 (follow-up interviews), cross-task data linkage.

Submitted in the fall, approved for spring deployment. Bundle:

1. **The video-assisted comparative reflection assignment** for the PI's software engineering
   course — three times in the semester, with the midpoint and final metacognitive components and
   GenAI coding agents at the end of the series (§3.2.3). Needs the video-anonymization platform
   named (§3.2.5) and retention terms for the recordings.
2. **The Task-1 follow-up interviews** with the preliminary ethics-course students (§3.1.3,
   backlog #3). IRB #2 does not reach them — its §4 excludes courses taught by the research team —
   and the approved course protocol carries surveys but not interviews.
3. **The data-linkage appendix**, already drafted at
   `course-protocol-mod/CourseProtocol_AppendixA_DataLinkage_MARKED.docx` and never submitted.

All three change *procedures only* for a population and purpose the course protocol already covers,
so one modification holds under UMaine's rule that a change to two or more of {population,
procedures, purpose} becomes a new study.

**Ippolito's advanced programming courses are not in this bundle.** Adding them would change
population *and* procedures, so they go into IRB #2 as an amendment once v9 clears.

---

## Track C — Recruit (gated on B1)

**Grant:** §3.1.2, the yearly faculty design cycle. **Funnel numbers:** the PI's, 2026-07-22.
These fit inside what is already drafted — IRB #2's ceiling is approximately 200 instructors and
IRB #3 says 5–15 per workshop, so 25 recruited and 10 adopting sits comfortably under both.

Ordered, because here the order carries real information — each step's yield sets the next step's size:

1. **Build the outreach list and send** — several hundred messages, CCSE mailing list and others.
   Mid-September, immediately on #3 approval. Requires the approved recruitment texts from #3.
2. **Interest-and-barriers survey out** — target ~25 respondents willing to continue. Late September.
3. **Co-design workshops** — 5–15 instructors each, October into November.
4. **Ten implementation commitments in hand — by mid-November.** The hard date.
5. **PI office-hours consultations** — running alongside, as instructors come in (§3.1.2).

---

## Track D — Design work with no approval gate

### D1. Build the modules — weeks 2–6
**Grant:** §3.1.4, explicitly Year 1 — "our Year 1 design iteration will focus on creating modules,
which effectively create a more careful sequence of varied meeting agendas… for particular
professional skills, to scaffold gradually opening up in the group," including **two to three
modules on critical GenAI use**, each carrying one or two icebreaker questions to reconnect.

No IRB gate at all. Two reasons this is not optional and not late-semester work:

- It is what you put in front of faculty in October. You cannot run a co-design workshop with
  nothing to co-design.
- It is IRB #1 decision 12's appendix and part of IRB #2's materials.

Also here: the full adapted icebreaker question list (IRB #1 decision 12).

### D2. Longitudinal video-reflection design v2 — weeks 6–10
**Grant:** §3.2.3. Feeds B5 directly — the design *is* the protocol appendix, so this work and the
modification are the same task done once.

---

## Track E — Writing

Two papers pending, one to submit, plus the TOaST conversion — endorsed by the PI on 2026-07-22,
and explicitly ranked below the reflection-group work. The FIE reflection-groups paper is the
model for drafting fast ("we wrote that paper very quickly"). **Timebox it.** Do not let it
displace the November date.

---

## Not feasible this fall — deliberately deferred

| Item | Grant § | Why not, and when |
|---|---|---|
| 10 faculty **implementing** reflection groups | §3.1.2 | Fall syllabi set, #3 not approved. Commitments by mid-Nov, implementation Spring 2027 |
| Video assignment deployed in the PI's SWE course | §3.2.3 | Needs B5 approved. Spring 2027 |
| Video assignment in Ippolito's courses | §3.2.3 | Needs an IRB #2 amendment after v9 clears. Spring 2027 |
| Student classroom data in collaborating courses | §3.1.4 | Needs #2 approved plus spring syllabi. Spring 2027 |
| Matching / behaviour-change tool | §3.3.2 | Year 2 by the grant's own timeline |
| Professionals as peer group members | §3.3.2 | Year 2 |
| Professional comparison group, ~200 via a recruiting company | §3.2.4 | Year 3 |
| Mock workplace, private-LLM hosting | §3.3.3 | Year 2+ |
| GenAI tool log data | §3.2.2 | Stretch goal, no protocol |

Two things I raised earlier and am parking here on purpose: the recruiting-company contradiction
(grant commits to one, IRB #1's live draft disclaims one, `IRB1_SUMMARY.md` decision 4 still lists
it open) and the participant-number ambiguity in §3.2.4 (60–100 and ~200, then "we will over-recruit
participants anticipating a drop-out rate of 50%" — so recruitment ceilings may need to be double
the stated populations). Both are **Year 3**. Neither blocks this semester.

---

## Open questions that gate parts of this

1. **Which approval did the video-reflection pilot actually run under?** The repo concluded the
   approved GenAI course protocol does not cover the video assignment — zero occurrences of
   "replay" or "anonymiz", screen recordings only during interviews — yet the pilot ran, and §3.2.5
   says "we already have IRB approval for the student studies." Both cannot be right. The answer
   decides whether backlog #8 is a modification or a new protocol, and whether A2 can start.
2. **Is the Year-1 wider measure set inside the approved instrument appendices?** Determines whether
   A1 ships complete or ships core-only.
3. **Did IRB #2 v9 or #3 v2 go back to ORA since 2026-08-14?** The repo's last commit is that date;
   nothing records a resubmission. If either went back, B1/B2 shrink to waiting.
4. **Does the approved protocol's consent permit recontacting alumni?** IRB #1 decision 9, and the
   gate on B4.
5. **What is on the Research Plan FigJam board** that is not here. Not readable from this session —
   the Figma account has a View seat, and the MCP needs an Editor seat. This plan is built from the
   grant and the PI meeting only, and should be reconciled against the board.
