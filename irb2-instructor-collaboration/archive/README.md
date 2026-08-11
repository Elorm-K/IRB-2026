# IRB #2 archive — superseded work

Never submit from this folder. The live drafts are in [../CURRENT/](../CURRENT/), generated
from [../source/](../source/).

Files were renamed on 2026-07-28 to put version and date in the name; `git log --follow`
recovers the original filenames.

| File | Was | What it is |
|---|---|---|
| `IRB2_Protocol_v1_2026-07-23.docx` | `IRB2_Protocol_InstructorCollaboration.docx` | First draft. An independent audit was run against this version; its findings are reconciled in the addendum to [../reports/IRB2_v4_VERIFICATION_REPORT.md](../reports/IRB2_v4_VERIFICATION_REPORT.md) |
| `IRB2_Protocol_v2_2026-07-24.docx` | `..._v2.docx` | After the pre-review and anchor-review passes in [../reports/IRB2_SUMMARY.md](../reports/IRB2_SUMMARY.md). **The live Google Doc forked from this version**, not from v3 |
| `IRB2_Protocol_v3_aligned_2026-07-25.docx` | `..._v3_aligned.docx` | Aligned to house style. The base document v4 was built from |
| `IRB2_Protocol_v3_aligned_BASE_SNAPSHOT.docx` | `_BASE_SNAPSHOT_v3_aligned.docx` | Phase-0 snapshot taken before v4 edits, so the Phase-4 alignment diff had a fixed base. **Byte-identical to the file above** (verified by checksum); kept because the verification report cites it by name |
| `IRB2_ConsentForms_v1_STALE_2026-07-23.docx` | `IRB2_ConsentForms_Instructor_and_Student.docx` | **Known-drifted.** Still carries the old protocol title, a wrong contact address, a missing team member, and a live decision marker. It is the reason `CURRENT/` consent forms are generated rather than hand-edited |
| `IRB2_RecruitmentTexts_v1_2026-07-23.docx` | `IRB2_RecruitmentTexts.docx` | Superseded by the generated v4 recruitment file |
| `IRB2_Protocol_v6_SUPERSEDED_2026-08-06.docx` | `IRB2_Protocol_v6_MERGED_SUBMISSION.docx` | The consent merge applied to the v5 text, before Cyril's Google Doc edits were reconciled in. Superseded within the day by v7 |
| `IRB2_Protocol_v5_SUPERSEDED_2026-08-06.docx` | `IRB2_Protocol_v5_MERGED_SUBMISSION.docx` | Superseded by v6, which merged the two instructor consent forms into one and relettered the appendices. **The last version with five consent forms and appendices A–P**; v6's alignment diff is taken against it |

## The version tangle worth knowing about

v4 was merged from **two** parents, not one:

1. `IRB2_Protocol_v3_aligned_2026-07-25.docx` — the richest text, used as the base.
2. A live **Google Doc** (`1RtTxaxVy70cO8ss9HY1C8d_iYZ29XFA2gOveEET16a0`) that had **forked
   from v2**, then accumulated hand edits and three open comment threads. It is not in this
   repo, and a doc ID is not a version — if it has moved since 2026-07-28, the merge needs
   rechecking.

Which parent wins where is recorded per-section in
[../reports/IRB2_v4_MARKUP_KEEP-ADAPT-CUT.md](../reports/IRB2_v4_MARKUP_KEEP-ADAPT-CUT.md).
The verification report flags that **the base document was never confirmed with the PI**,
which the workflow's Phase 0 asks for — so if the PI considers the Google Doc authoritative,
the merge direction needs review.
