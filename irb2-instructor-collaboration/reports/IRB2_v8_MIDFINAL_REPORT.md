# IRB #2 v8 "mid-final" — restructure, grammar pass, and appendix repair

**2026-08-06.** Base text: your Google Doc **"IRB 2"** (`1evcxa_Hr…`), as it stood at its
2026-08-06 19:37 revision. Output:

- `source/protocol_v8_MIDFINAL.md` — the source
- `CURRENT/IRB2_Protocol_v8_MIDFINAL.docx` — 14,157 words, 876 paragraphs, page-numbered footer

**Everything I added or restored is bold red.** 91 marked spans. Delete any of them and the
document still reads correctly. Grammar and cross-reference corrections are *not* marked — they
are itemized below instead, because marking them would have buried the red that matters.

> **Lineage note.** Your doc is v5-lineage. It did not pick up v7, so v8 is *your* doc repaired,
> not v7 continued. `source/p2/*.md` still holds the v7 line and I did not touch it. Before the
> next round, pick one lineage — v8 or v7 — and retire the other, or they will keep diverging.

---

## 1. The appendix problem, and how it was fixed

Your edit pass deleted six appendices and renumbered the consent forms, but the narrative still
carried the old v5 letters. Of the **41** appendix cross-references in the document, **20 were
broken**: 11 pointed at an appendix that no longer exists (D, F, G, H, O, P), and 9 pointed at an
appendix that now contains something else (B, C, M, N). The second kind is worse than a plain
dangling reference, because it reads as correct:

- §2 item 9 sent students to *"the consent form (Appendix C)"* — Appendix C was by then the
  longitudinal survey form, not the course consent form.
- §2 item 11 sent readers to *"Appendix N"* for longitudinal survey content — Appendix N was by
  then the site-approval letter.

### Final lettering — contiguous A–J, no gaps

| v8 | Contents | Was, in your doc |
|---|---|---|
| **A** | Instructor consent — survey, workshops, consultations, **interviews**, follow-ups | A |
| **B** | Student consent (collaborating courses) | B |
| **C** | Student survey consent (submission indicates consent) + comparison adaptation | C |
| **D** | Student and alumni interview consent | E |
| **E** | Design workshop protocol and consultation procedure | I |
| **F** | Instructor recruitment texts | J |
| **G** | Student recruitment script | K |
| **H** | Student group-matching, pre-course, and post-course surveys | L |
| **I** | Student longitudinal follow-up survey | M |
| **J** | Site approval / letter of support request | N |

### The six deleted appendices — where each reference now goes

| Deleted | What referenced it | Fix |
|---|---|---|
| **B** instructor interview consent | Appendix A twice ("a separate consent form"), §5, §9 | **Folded into Appendix A.** A now carries the interview task bullet, the recording terms, the 30–60 minute estimate, the $25 compensation, and a decline-an-interview clause. §5 now says four consent forms, not five. |
| **F** instructor interest and barriers survey | §2 item 1, §2 data item 1.1 | **Described inline.** Item 1 now names the topics the survey covers; the appendix pointer is gone. |
| **G** instructor follow-up survey | §2 item 5, data item 1.1 | **Described inline** in item 5. |
| **H** instructor interview guide | §2 item 2, data item 1.2 | **Topical description plus two example questions inline**, red, in item 2. `institutions/umaine.md` §5: *"A topical description plus one or two examples covers both."* |
| **O** reflection group meetings | data item 1.5, "topic modules" | **Pointed at §2 item 8**, which is the new meeting-structure item (see §2 below). Topic modules and instructor adaptations restored there. |
| **P** site approval | §2 item 16 | **Pointed at Appendix J.** |

Plus one appendix that existed but was empty or wrong:

- **Appendix C's "Comparison-course adaptation"** was a heading with nothing under it, announced
  two paragraphs earlier by *"A comparison-course adaptation follows at the end of this appendix."*
  Restored (red) from the v7 text: three named changes — purpose sentence, scope statement,
  compensation.
- **Appendix E (student and alumni interview consent) contained the wrong document.** Its body was
  the IRB #1 outside-classes reflection-group consent — matching into a 3–5 person group, a
  12-week participation cycle, a "supporting tool", nine follow-up surveys. Nothing in it was about
  an interview. **Replaced wholesale** with the student/alumni interview consent form (now Appendix D).
  This is the single largest change in v8; please read Appendix D rather than skim it.

---

## 2. Structural fixes (not marked red)

1. **§2 item 7 was three items spliced into one paragraph** — classroom use, then a matching-survey
   pointer, then an orphan sentence fragment *"Group meetings and individual reflections."*, then a
   four-step numbered list that collided with the numbering of the Methods items around it. Split
   into item 7 (classroom use) and item 8 (group meetings, as bullets). Everything after renumbered;
   items are now 1–16 and every internal reference to them was updated.
2. **Data-collected list** re-pointed: 1.1 and 1.2 now cite Methods items instead of dead
   appendices; 1.5 cites item 8; 1.4, 1.6, 1.7, 1.9 re-lettered.
3. **Appendix B carried two contradictory time-commitment paragraphs**, back to back — one saying
   *"10-15 minutes for each longitudinal follow-up survey"*, the next *"10–15 minutes for each
   survey, plus about 5 minutes for the matching survey."* Kept the second; it matches the procedures.
4. **Appendix B's data-linkage checkbox had no explanation.** The optional second checkbox survived
   your edit; the Confidentiality paragraph defining what linkage means did not. Restored (red),
   with the matching bullet and the revocation clause.
5. **Appendix B's two archival paragraphs** ("Work from assignments will be copied…" and "Survey
   data will be copied…") were near-identical. Merged into one.
6. **Appendix B lacked any publication/data-sharing statement.** Every other form has one. Added (red).
7. **Appendix B's revocation date** was the bare *"Dec 15, 2031"*, with no explanation of where it
   comes from. Now reads as the key-file rule, as in the other three forms.
8. **Chris Dufour removed from all four consent forms' Contact Information lines.** You removed him
   from §3 Personnel; he was still listed as a contact in every form. See open item 3 below.
9. **Angle-bracket placeholders converted to square brackets** — `<course name >` → `[course name]`,
   `<course number e.g. COS100>` → `[course number, e.g., COS100]`. This matches the `[course number]`
   already used in Appendix C, and it is also what stops Google Docs' markdown import from silently
   eating them as HTML tags.
10. **Empty instrument sections filled.** Appendices H and I had headings — *Self-efficacy*,
    *Professional and reflection skills*, *Professional and STEM identity* — with no items under
    them. Each now carries a red note naming the measures used (Grant et al.; Kember et al.;
    Edmondson; the STEM-identity pictorial item), which also rescues five references that had been
    left uncited when the instrument appendices were deleted. One `{your input needed here}` marker
    remains, for the generative-AI measure — see open item 5.
11. **Appendix H gained the group-matching survey** as a first sub-section (red), because Appendix B
    and §2 both still refer to it. Gender and race/ethnicity items restored to the pre-course
    demographics.
12. **Appendix I gained the missing consent pointer** (Appendix C is its first page) and a career-
    and-progress section, which §2 item 12 implies.

### Grammar and wording

- §2 item 3: *"Workshops invite instructors who integrated a design, attempted to and encountered
  barriers."* — the sentence lost its third clause and its verb agreement. Now *"…who have integrated
  a design, who attempted to and encountered barriers, or who chose not to integrate"*, matching
  Appendix E.
- §4: "enrol" → "enroll".
- §7: *"mitigated by the confidentiality protections in Section 6 by the workshop ground rules"* —
  missing conjunction. Now "in Section 6, by the workshop ground rules, and by…".
- §7: the third-party-application paragraph opened on a sentence fragment (*"Risks of their data
  leaking from…"*). Rewritten as a complete sentence; "Tiktok" → "TikTok"; "the user" → "the
  participant" in the skip-questions sentence.
- §1 and Appendix J: stray leading space inside the quoted award title.
- Appendix B Benefits: hyphen-prefixed lines converted to bullets; missing terminal punctuation added.
- Appendix C and D Researchers lists: stray empty bullet removed.
- Appendix B's *"You must be at least 18 years of age to participate, and participating in
  `<course name >`"* — sentence ended mid-clause. Now *"You must be at least 18 years of age and
  enrolled in [course name] to participate."*

---

## 3. Red restorations that carry a citation

These I applied rather than only flagging, because each has a rule behind it. Each is one deletion
away if you disagree.

1. **"CAREER:" prefix on the title** — `institutions/umaine.md` §2, hard gate: *"Title must match
   the grant title if funded."* The award title is *"CAREER: Developing Professional Skills…"*.
   Applied to the document title, §1's quoted award title, all four consent-form titles, and the
   site-approval letter. **Without it the application can be returned unread.**
2. **Tax-reporting language in all four consent forms** — umaine.md §7: over **$75** cumulative
   triggers the HR / Purchasing / Form-1099 block, computed against the *maximum cumulative* payment
   one participant can receive. A student completing all eight follow-up surveys reaches **$80**; an
   instructor at $25 per interview crosses $75 on the fourth. Your current doc had removed it from
   every form.
3. **Vendor names in §6 Confidentiality** — umaine.md §6: *"If data collection will occur online,
   state the program that will be used (e.g., Qualtrics, Skype, etc.)"*. Qualtrics, Zoom, and Google
   Drive named in §6 only. Your de-naming in the Methods body is untouched — `board-rules.md` §5's
   de-naming rule applies there, and the two rules do not conflict.
4. **§9 worked totals and the course-credit paragraph** — umaine.md §7 requires the worked-total
   pattern (*"that would be $90 in total"*), and where credit is offered, the alternative-route
   statement. Your Appendix B still offers course credit, so the §9 statement is load-bearing.
5. **Recording-deletion language in §6** — umaine.md §6, approved practice: recordings die with the
   key file at five years. "De-identified data retained indefinitely" does not state a recording's
   fate, because voice is an identifier.
6. **CITI training sentence in §3** — one sentence, standard for this application.

---

## 4. Flagged, not fixed — your call

1. **No consent form has a Concise Summary.** umaine.md §5 records the trigger as *">1 page **or**
   federally funded"* and CAREER meets both — but **zero** approved forms in this program contain
   one, so the compliance pass reports this `UNVERIFIED`, not `VIOLATION`. v7 restored all four; you
   have none in all four, which is at least internally consistent. Leaving as you have it. The four
   summaries are in `source/p2/consentA.md`, `consentB.md`, `consentCD.md` if you want them back.
2. **Consent-form reading level is grade 10.7–11.7.** The gate says *"no higher than an 8th grade
   reading level."* This has been flagged since v6 and not acted on. It is a real gate, and the
   cheapest fix is shortening sentences in the Confidentiality sections.
3. **The cover page still names Chris Dufour as CO-INVESTIGATOR.** `CURRENT/IRB2_CoverPage_v7.docx`
   lists him with his email; the protocol no longer does anywhere. One of the two must change before
   submission.
4. **"Our application" was cut from §7.** Your third-party-risk paragraph said participants should
   not submit content to third-party services *"including our application"* — but no application is
   described anywhere in this protocol, so a reviewer would ask what it is. I generalized to
   "third-party services". If a tool *is* in scope for IRB #2, it needs describing in §2 and §6.
5. **One `{your input needed here}` marker remains**, in Appendix H: the exact items for the critical
   and reflective generative AI use measure. The funded plan names the ChatGPT Literacy scale and
   your four-question critical/ethical AI self-efficacy measure.
6. **There is still no student/alumni interview guide.** Instructors now have a topical description
   with examples inline; students and alumni have a consent form with two example questions and no
   instrument. Not a hard gate, but a visible asymmetry.
7. **Merging the instructor interview consent into Appendix A** removed an instructor's ability to
   consent to the study without consenting to interviews. If you want that back, the cheapest fix is
   a second checkbox: *"☐ I am willing to be contacted about a confidential interview (optional)"*.

---

## 5. Verification

- **Appendices A–J, contiguous. Zero dangling references. Zero orphan appendices.** Checked
  mechanically against the appendix headings.
- Nine narrative headings present, in the required order, with instruction text absent.
- Page-number footer intact (*Page X of Y*), Word format, single document.
- Repeated facts agree across the narrative, the four consent forms, and the recruitment texts:
  8 follow-up surveys · $10 per survey · $25 per interview · $80 maximum student total · $75 tax
  threshold · 30–60 minute interviews · 10–15 minute surveys · 5-minute matching survey · five-year
  key file, December 2031 worked example · 200 instructors · 1,000 students.
- No angle-bracket placeholders remain; no `[PI DECISION NEEDED]` markers remain.
- Chris Dufour: zero occurrences.

## Before submitting

Strip the red. The `{{…}}` markers live in `source/protocol_v8_MIDFINAL.md`; deleting them and
rebuilding with `python3 tools/build_docx.py` produces a clean document. Nothing red is meant to
reach the board as red text.
