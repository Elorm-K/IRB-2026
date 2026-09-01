# IRB #1 v6 — submission-ready protocol, response report

**2026-09-01.** Built from v5 ORA response (`source/protocol_v5_ORA_RESPONSE.md`), with all
`{{…}}` change marks stripped. Content is identical to v5; no substantive edits were made
between v5 and v6. v6 is the clean copy for board submission.

## Files

- `source/protocol_v6.md` — the clean source (no change marks)
- `CURRENT/IRB1_Protocol_v6.docx` — the built Word document. **This is the file to submit.**
- `source/media/` — the five instrument images from Appendix C, carried over intact

Rebuild with `python3 tools/build_docx.py source/protocol_v6.md CURRENT/IRB1_Protocol_v6.docx`.

The v5 files (`source/protocol_v5_ORA_RESPONSE.md`, `CURRENT/IRB1_Protocol_v5_ORA_RESPONSE_MARKED.docx`)
are the marked-up drafts for PI review; v6 is what goes to the board.

---

## 1. Reviewer point verification (all 40 points)

Every point from the board's review was verified against v6. All 40 are addressed; 0 are
missed.

### General

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| G1 | Use "members" for group status, "participants" for research role, throughout | Done | §2 definition paragraph; consistent throughout all sections and appendices |
| G2 | No "opt-in"/"opt-out" for group membership; only for research | Done | Every surviving "opt out" refers to research data use only |

### Methods

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| M1 | Items 1 & 2 belong in Recruitment and Informed Consent; use verbal script and opt-out | Done | Deleted from Methods; verbal script is Appendix F.1; opt-out form is Appendix A |
| M2 | Abbreviate service section; drop instrument appendices for it; state data is not sensitive | Done | Six one-sentence items; no service instrument appendix; sensitivity statement in §2 |
| M3 | Rename "For the research" | Done | "Research data collected outside of normal reflection group activities" |
| M4 | Don't reference recruitment materials in Methods, only instruments | Done | Points only to Appendix C, E, and the consent forms |
| M5 | State whether surveys are anonymous or confidential | Done | "confidential rather than anonymous" in §2 item 7 and Appendix B |
| M6 | More detail on interview timing | Done | Six worked examples after item 8 |
| M7 | State interview length | Done | 30–60 minutes in §2, Appendix D, Appendix F.3 |
| M8 | State interview format | Done | One-to-one; online on Zoom or in person; no group interviews |
| M9 | State how interviews are audio recorded | Done | Zoom audio-only online; handheld recorder in person; no video; recording not required; transcribed by named investigators |
| M10 | Comparative group details or modification statement | Done | Modification statement in §2 item 9 |
| M11 | Delete enrolment/recruitment-channel sentence from Methods | Done | Moved to §4 (4)&(5) |

### Recruitment

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| R1 | Replace recruitment section with five parts | Done | Sections (1)–(3) and combined (4)&(5) |
| R2 | Include and reference all recruitment appendices | Done | Appendix F: F.1–F.3 written, F.4/F.5 reserved |
| R3 | Modification statement for comparison-group recruitment | Done | §4 (4)&(5) |

### Informed Consent

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| C1 | Five consent forms (three written, two deferred) | Done | A (opt-out), B (survey), D (interview); comparison deferred |
| C2 | For each, state how received, what indicates consent, opt-out mechanics | Done | §5 rewritten as five subsections with full mechanics |

### Confidentiality

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| F1 | Delete the first paragraph | Done | Deleted |
| F2 | Delete-on-request paragraph is optional | Kept | Board-approved language; flagged as intentional |
| F3 | Re-organize around the five sections | Done | §6 reorganized |
| F4 | Audio-recording details, month/year, no indefinite retention | Done | 72-hour removal; five-year deletion; no recording beyond December 2036 |

### Risks / Benefits / Compensation

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| K1 | Delete peer-disclosure risk | Done | Deleted from §7 and all consent forms |
| B1 | Delete participant-benefit clause | Done | "There are no direct benefits to participants." |
| B2 | Frame broader benefits as potential | Done | "may … may … may" with closing caveat |
| P1 | Delete first compensation sentence | Done | Replaced with "no compensation for research use of reflection-group materials" |
| P2 | Delete "(the initiation survey is not compensated)" | Done | Deleted; initiation survey is now service data |
| P3 | Same $25 for comparative interviews? | Done | Stated in §9 |
| P4 | Final distribution dates (MON/YR) | Done | December 2035 for gift cards |

### Appendices

| # | Reviewer point | Status | Where in v6 |
|---|---|---|---|
| A1 | Appendix A should be opt-out form only | Done | Rewritten; six material types; no checkbox, no signature |
| A2 | Co-design sessions as a sixth undescribed method | Done | Rolled into materials method |
| A3 | Cross-study data-linkage consent unnecessary | Done | Deleted everywhere |
| A4 | Each section relevant only to use of materials | Done | Surveys/interviews only in Appendices B and D |
| B1 | Delete Appendix B (intake/invitation) | Done | Deleted with its two images |
| C1 | Delete Appendix C intro paragraph | Done | Deleted; course language fixed |
| D1 | Five recruitment scripts | Done | Appendix F with F.1–F.5 |
| E1 | Delete other-scripts appendix | Done | Deleted |
| F1 | Survey consent should not describe intake survey | Done | Opens with reviewer's sentence |
| G1 | Interview consent should not read as group interviews | Done | Singular "one-to-one interview" throughout |

## 2. Appendix structure (v6)

| Letter | Content |
|---|---|
| A | Opt-out form for research use of reflection group materials |
| B | Longitudinal follow-up survey consent form (submission indicates consent) |
| C | Longitudinal follow-up survey instrument (5 PNG images) |
| D | Interview consent form |
| E | Interview guide |
| F | Recruitment texts: F.1 verbal script, F.2 survey email, F.3 interview email, F.4–F.5 reserved for comparison population |
| G | Compensation information form |

## 3. Open items for the PI (carried from v5)

These remain open from the v5 report and are unchanged:

1. **Comparison-population consent forms and details** — deferred to a modification.
2. **December 2035 / December 2036 dates** — derived; confirm or replace.
3. **Transcription by named investigators** — stated as fact; a service would need a modification.
4. **Two-week opt-out window** — a drafting choice, not reviewer-specified.
5. **Protocol-candidate files in `CURRENT/`** — still unarchived.

## 4. Build verification

| Check | Result |
|---|---|
| Paragraphs | 562 |
| Images | 5 (image1.png, image4.png, image5.png, image6.png, image7.png) |
| `{{…}}` marks | 0 — confirmed by grep |
| Red spans in .docx | 0 — no MARK_STYLE rendered |
| Page footer | "Page X of Y" field present |
