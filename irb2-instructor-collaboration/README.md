# IRB #2 — Instructor Collaboration (incl. critical and reflective use of generative AI)

The draft furthest along. **v7, drafted 2026-08-06, awaiting PI review.** Backlog item 2.

**v7 is a reconciliation**, not a redraft: Cyril's Google Doc ("IRB 2") is the base text, with the
v6 instructor consent-form merge applied on top and a short list of board-required items restored.
Every change is **bold red** in the `.docx` — strip the `{{...}}` markers from `source/p2/*.md`
and rebuild before submitting.

**One protocol, two populations.** Instructor-facing research (interest-and-barriers survey,
optional interviews, co-design workshops, consultation notes, longitudinal follow-up,
instructor adaptation) *and* student-facing research in collaborating instructors' courses
(classroom use, student consent, surveys, reflection materials, longitudinal follow-up,
student and alumni interviews, student design input, comparison courses, external sites).

Both grant arms are represented — reflection groups *and* generative AI. v3's failure mode
was a title that named GenAI over a body that didn't.

## v5 reversed v4's split — read this before re-splitting it

v4 was staged narrow: instructors now, students later by modification. That plan doesn't
work. Per UMaine's modification rules, a modification changing **two or more** of {study
population, study procedures, study purpose} *"becomes a new study"* — adding the student arm
changes population **and** procedures. Staging would have cost two full applications instead
of one plus an amendment, which removed the load-bearing reason to split.

The full argument, and instructions for regenerating the narrow version if you want the split
back on cycle-time grounds, are in
[../irb2b-student-stream-held/README.md](../irb2b-student-stream-held/README.md).

## Read in this order

1. **[reports/IRB2_v7_RECONCILIATION_REPORT.md](reports/IRB2_v7_RECONCILIATION_REPORT.md)** —
   start here. What your Google Doc changed, what was restored and why, the defects fixed, and what
   is still open.
2. **[reports/IRB2_v6_VERIFICATION_REPORT.md](reports/IRB2_v6_VERIFICATION_REPORT.md)** —
   what the consent-form merge changed, and the four verification passes on it.
3. **[reports/IRB2_v5_VERIFICATION_REPORT.md](reports/IRB2_v5_VERIFICATION_REPORT.md)** — why the
   protocol is merged rather than split, the fixes applied, the consistency pass, and what is still
   covered by no protocol. Everything v6's report does not restate. It tells you what you do *not*
   need to re-check.
4. **[CURRENT/](CURRENT/)** — the documents themselves.
5. **[reports/IRB2_v4_VERIFICATION_REPORT.md](reports/IRB2_v4_VERIFICATION_REPORT.md)** and
   **[reports/IRB2_v4_MARKUP_KEEP-ADAPT-CUT.md](reports/IRB2_v4_MARKUP_KEEP-ADAPT-CUT.md)** —
   v4's provenance. Still the record of which passages are preserved approved language, and
   why each cut was made; v5 inherits those decisions.

## `CURRENT/` — the live drafts

| File | What it is |
|---|---|
| `IRB2_Protocol_v7_MERGED_SUBMISSION.docx` | The submission: narrative plus all appendices, both populations |
| `IRB2_CoverPage_v7.docx` | Cover-page values, prepared for pasting into the official downloaded template |

The consent forms in v5 are rebuilt from the **January 2026 board-approved templates** in
`../inputs/approved-protocols/2023_07_10 Nelson_MOD_Jan_2026_FINAL.docx` — copied approved
language, not language derived from the grant. That was v4's largest unverified item and it
is now closed.

## `source/` — edit here

- **`p2/`** builds v7: `narrative.md`, `consentA.md`, `consentB.md`, `consentCD.md`,
  `appx.md`, `coverpage.md`. Change the source, then regenerate:

  ```
  python3 ../../tools/build_docx.py source/protocol_v7_MERGED.md \
      CURRENT/IRB2_Protocol_v7_MERGED_SUBMISSION.docx
  ```

  `protocol_v7_MERGED.md` is `narrative.md` followed by the four consent files and `appx.md`,
  joined by a blank line pair.
- `protocol_v5_MERGED.md` is the assembled v5 markdown, kept for the alignment diff.
- `consent_v4.md`, `protocol_v4.md`, `recruit_v4.md`, `held_v4.md` are v4's parts, kept for
  lineage.

The board wants Word documents and round-tripping through Google Docs destroys formatting, so
the `.docx` is the delivery format, not the working format.

## Before submitting

**3 decisions** are carried in the document as `{your input needed here}` markers: the GenAI
self-efficacy items and the wider first-year measure set (both Appendix L), and the adapted
icebreaker question list (Appendix N). Nine others were closed on 2026-08-04 — see the two
addenda at the end of the v5 report. The cover page also needs a human-subjects start date.

v6 adds two decisions of its own, both in its report: whether to add an optional interview
checkbox to the merged instructor form, and whether Appendix C (student survey consent) should be
narrowed to comparison courses.

**One thing closed by marker deletion but not actually resolved:** the **Dufour dual-role
conflict**. §4 excludes any course taught by a member of the research team, Chris Dufour is
listed as personnel in §3, and the funded plan names his one-credit seminar as a deployment
site. The marker is gone; the conflict is not.

Two process items remain open: the **official cover page template** must be downloaded and
the prepared values pasted in, and the **Linear task for PI review** (workflow Phase 5) was
never created — the connector isn't authorized.

## What this protocol still does not cover

Confirmed, not presumed, now that the GenAI protocol has been read: the **video-assisted
comparative reflection assignment** (students screen-recording programming sessions with and
without generative AI, then comparing them) and the budgeted video-anonymization platform are
authorized by no protocol. Backlog item **8**. The grant deploys it in a collaborator's
courses, which the team's own course protocol does not reach.
