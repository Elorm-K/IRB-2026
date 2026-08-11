# Google Docs review set — upload + verification, 2026-08-03

The live drafts are now in Google Docs so they can be commented on. This file records what
went up, proof that each doc faithfully represents its repo source, and the content problems
the verification pass turned up along the way.

**The repo stays authoritative.** The Google Docs are review scratch only. Nothing is ever
converted back to `.docx` — comments get read out of Docs and applied to the repo sources
(`source/p2/*.md` for IRB #2, the `.docx` for IRB #1 and the course mod). That avoids the
round-trip formatting damage the skill warns about.

## The review folder

[IRB Review — 2026-08-03](https://drive.google.com/drive/folders/1xv8m8rtz8ZU8SRKOpg_UoQ-nocXMygky)

| Google Doc | Repo source |
|---|---|
| [IRB1 — Protocol, Reflection Groups Outside Classes](https://docs.google.com/document/d/1IFsi2p1cmW2_jideOZ9Jm6bdx4cs9MjL0mmFzEauSu0/edit) | `irb1-reflection-groups/CURRENT/protocol-candidates/IRB1_Protocol_..._FINAL_structured.docx` |
| [IRB1 — Consent Form, Participation](https://docs.google.com/document/d/1Hd8A9y4_yPOxSd5ebR3j3qG2hFfvR_74R9zB0FHnGvk/edit) | `irb1-reflection-groups/CURRENT/IRB1_ConsentForm_Participation.docx` |
| [IRB1 — Recruitment Texts](https://docs.google.com/document/d/1iWQcu99MioZMb4zTnFBZgAHjzqqXDWO7d2YIamPcjaw/edit) | `irb1-reflection-groups/CURRENT/IRB1_RecruitmentTexts.docx` |
| **[IRB2 v5 — Protocol (CONSOLIDATED — review this one)](https://docs.google.com/document/d/1H4PaliShiGFC8j_J76x30sDlV5xoGuriH82rw0oRdvI/edit)** | `irb2-instructor-collaboration/source/protocol_v5_MERGED.md` |
| [IRB2 — Cover Page v5](https://docs.google.com/document/d/1hHgO4xlJBJqdzOArOhHocPz2By_0Sgp3YWkIL2zNHDI/edit) | `irb2-instructor-collaboration/CURRENT/IRB2_CoverPage_v5.docx` |
| [Course Protocol MOD — Appendix A, Data Linkage](https://docs.google.com/document/d/1-A6-VA-TOFdHFwHwKok4g9LUFTmL0mwnd0-L3Z74whY/edit) | `course-protocol-mod/CourseProtocol_AppendixA_DataLinkage_MARKED.docx` |

### Superseded — do not review, do not comment

IRB #2 v5 first went up split into four parts. That was wrong: it should be read as one
continuous document, the way the board sees it. The consolidated document above replaces them.
The Drive tools available here can create documents but cannot delete them, so **these four
need deleting by hand in the Drive UI**:

- IRB2 v5 — Part 1, Protocol Narrative
- IRB2 v5 — Part 2, Consent Forms A & B (Instructors)
- IRB2 v5 — Part 3, Consent Forms C, D & E (Students)
- IRB2 v5 — Part 4, Appendices F–P

## Verification — all 9 documents

Each Google Doc was exported back out and diffed against its repo source, normalizing away
formatting-only differences (emphasis markers, list bullets, heading levels, auto-linked
emails, byte-order marks). Anything surviving that is real content drift.

| Document | Result |
|---|---|
| **IRB2 v5 consolidated** | 17,313 words; 2 differences, both the placeholder artifact below |
| IRB1 protocol | **MATCH** — identical, 6,823 words |
| IRB1 consent form | **MATCH** — identical, 902 words |
| IRB1 recruitment texts | **MATCH** — identical, 342 words |
| IRB2 cover page | **MATCH** — content read back and confirmed |
| Course-mod Appendix A | 1 difference, the placeholder artifact below |

The four superseded IRB #2 parts were also each verified MATCH before being replaced
(narrative 6,054 words; consents A+B 3,063; consents C+D+E 4,418; appendices F–P 3,776),
which is why the consolidated document could be assembled from them with confidence.

No paraphrasing, no dropped or altered passages, no changed numbers anywhere.

### The one upload artifact: angle-bracket placeholders are eaten

Google Docs' markdown import treats `<...>` as an HTML tag and deletes it. Every occurrence
across all nine documents was enumerated mechanically; there are exactly three, all in the
same sentence pattern:

| Document | Source text | Reads in Docs as |
|---|---|---|
| Course-mod Appendix A | `"Opt out of reflection research in <course number e.g. COS100>"` | `"Opt out of reflection research in "` |
| IRB2 v5 Appendix C, Voluntary | `"Opt out of reflection research in <course number>"` | `"Opt out of reflection research in "` |
| IRB2 v5 Appendix D, Voluntary | `"Opt out of reflection research in <course number>"` | `"Opt out of reflection research in "` |

**The repo sources are correct** — the placeholders are intact there. Please don't "fix" these
three sentences based on how they look in Docs. The available Drive tools can create documents
but cannot edit or delete them, so these could not be patched in place.

## Content problems found while verifying

These are in the source documents, not artifacts. Nothing has been changed — flagging only.

### 1. BLOCKING — the standalone IRB #1 consent form contradicts the protocol's own Appendix A

`irb1-reflection-groups/CURRENT/IRB1_ConsentForm_Participation.docx` (2026-07-23) and
Appendix A inside `IRB1_Protocol_..._FINAL_structured.docx` (2026-07-27) are both the
participation consent form, and they disagree on six points. This is the exact failure mode
`WHICH-IS-LIVE.md` predicted when it noted the standalone files predate all three protocol
candidates.

| | Standalone file | Protocol Appendix A |
|---|---|---|
| Study title | "Designing and Evaluating Reflection in Agency-Affirming Learning and Collaboration Environments" | "Group and Individual Reflection and Collaboration" |
| Cyril's email | `cyril@yesslab.org` | `cyril.agbewalikoku@maine.edu` |
| Interview compensation | absent — carries an open `[PI DECISION NEEDED]` about it | commits **$25** per interview |
| Open decision markers | 2 live | 0 |
| 12-week participation cycle | not mentioned | stated |
| Supervisor/advisor protections | **present** | **absent** |

Two of these matter beyond bookkeeping:

- **The two documents commit to different compensation.** The protocol promises $25 per
  interview; the form a participant would actually sign says nothing about interview payment.
- **The protocol's Appendix A dropped the supervisor/advisor conflict-of-interest paragraph**
  that the standalone form still carries — "extra protections apply", "a different member of
  the team will handle your decision", the supervisor "will not know whether you participated
  until the data are archived", and no effect on "lab membership, assistantship, funding,
  authorship, advising, evaluations, or letters of recommendation". Section 5 of the protocol
  body also softened opt-out routing from *a team member who does not supervise or advise you*
  to *a member of the research team*.

  This looks like approved protective language lost in a rewrite rather than a scope decision,
  and it is the kind of protection this board cares about, since the population includes
  university students the team may advise. **Recommend restoring it** unless it was cut
  deliberately.

- Relatedly, the standalone `IRB1_RecruitmentTexts.docx` has a **lab / graduate-student
  invitation** script, "sent by a team member who does not supervise the invitee". The
  protocol's Appendix D replaced that script with an organization/listserv one. If lab and
  grad-student recruitment is still in scope, the script and its protections need to come back;
  if it is out of scope, the standalone recruitment file should be archived so it cannot be used.

### 2. Recruitment and email scripts have blank URLs

Several participant-facing scripts read "Details are in the consent form: ." with nothing where
the link belongs — the URL placeholder is simply missing, not a conversion artifact.
In `IRB1_RecruitmentTexts.docx`: the alumni and lab/graduate-student invitations. In the
protocol's Appendix D and E: the alumni invitation, the organization/listserv invitation
("Details, the information session schedule, and the consent form are at: ."), and all three
email templates. Reviewers will notice these.

### 3. Which of the three IRB #1 protocol candidates is live is still unconfirmed

Still open from `WHICH-IS-LIVE.md`. This review used
`IRB1_Protocol_ReflectionGroups_OutsideClasses_FINAL_structured.docx`, the recommended one.
If that is wrong, the Docs copy is wrong too.

## Also worth knowing

- **The Drive account is `cyril.webdev@gmail.com`**, not `cyril@yesslab.org`. These documents
  are in a personal Gmail Drive, which matters for sharing with Greg and for anything treated
  as institutional record. Protocols under review are ordinarily not published; sharing should
  be by explicit invitation, not link-open.
- **The IRB #1 protocol's 7 appendix survey screenshots are not in the Docs copy.** Google Docs'
  markdown import cannot carry images, so each one shows as an `[IMAGE: …]` marker naming the
  file. They are validated instrument screenshots (self-efficacy items, the STEM-identity
  pictorial item, reflection scales). To comment on those, open the `.docx`.

## When you're back

Comment in the Docs, then say the word and I'll read every comment thread and apply the changes
to the repo sources. I have not edited any protocol content — the three items above are flagged
for your decision, per the rule that the compliance pass flags and the PI decides.

---

# Refresh round 2 — 2026-08-04

The repo's IRB #2 v5 changed today: compensation decided ($25 per interview, workshops unpaid) and
the final IRB #1's drafting decisions ported in. See the addendum at the end of
`irb2-instructor-collaboration/reports/IRB2_v5_VERIFICATION_REPORT.md`. Open decisions 12 → 9.

**The consolidated Google Doc was refreshed by hand, not by re-upload.** The Drive tools can create
documents but cannot edit them, so a tool-driven refresh would have meant a *new* document —
orphaning any comment threads on the existing one and adding a third "consolidated" doc to delete.
Instead the updated `.docx` was opened and its contents pasted over the body of the existing doc,
which keeps the URL and every comment thread:

[IRB2 v5 — Protocol (CONSOLIDATED — review this one)](https://docs.google.com/document/d/1H4PaliShiGFC8j_J76x30sDlV5xoGuriH82rw0oRdvI/edit)
← `irb2-instructor-collaboration/CURRENT/IRB2_Protocol_v5_MERGED_SUBMISSION.docx` (md5
`d5487db82dc85281fe3ee6677d18445e`, 34,755 bytes, 944 paragraphs)

**Pasting from the `.docx` rather than importing markdown also fixes the placeholder artifact.**
The `<course number>` placeholders in Appendices C and D survive a Word paste; they were being eaten
only because the first upload round went through Google Docs' *markdown* import, which treats `<…>`
as an HTML tag. If this doc is ever refreshed by markdown import again, that artifact returns.

**Note the source-of-truth change for IRB #1.** The IRB #1 row in the table above points at a repo
`.docx` that is no longer live — editing moved to a Google Doc and the submitted version differs from
the repo copy. See the warning block at the top of `irb1-reflection-groups/README.md`. The IRB #1
Google Doc in this review folder is a copy of the *stale* repo file, so do not review it either; the
live one is `IRB1_Protocol_ReflectionGroups_OutsideClasses_structured`, shared in from another
account.

Still needing manual deletion in the Drive UI, now six documents: the four superseded IRB #2 parts
listed above, plus `IRB2 v5 — Full Protocol (Consolidated, Appendices A–P)` (an earlier consolidation
from 02:00 on 2026-08-04) and the stale `IRB1 — Protocol … (FINAL_structured)` copy.
