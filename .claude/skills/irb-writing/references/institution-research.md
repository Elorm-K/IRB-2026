# Researching an institution's IRB rules

The compliance pass (`compliance-check.md`) can only check rules it has. This file is how
those rules get obtained, for **any** institution — the skill must not assume UMaine.

Output: one file per institution at `institutions/<slug>.md`, written from the template in
§4. `institutions/umaine.md` is the worked example.

**When this runs:** at Pass 4, not before drafting. If a current file already exists for the
reviewing institution, skip straight to the pass. Phase 0 only *records which institution*;
it does no fetching.

---

## 1. Establish the reviewing IRB(s)

Ask; do not infer from the PI's affiliation. The question:

> Which IRB will review this protocol? And will any activity happen at another institution
> — a collaborating instructor's campus, a partner school, a recruited site?

Three cases, and they change how much work this is:

- **One institution.** One file. The common case.
- **The PI's institution plus collaborating sites.** Each site has its own rules and its own
  file. For each, establish which of three arrangements applies: a **reliance agreement**
  (the PI's IRB reviews for both), a **local review** at that site, or an **exempt /
  not-research determination**. Committing in writing to full local review at every site is
  a promise that is expensive to keep — check what the protocol currently says before
  assuming.
- **Participants recruited outside any institution** — paid panels, professional samples,
  community members. No second institution to research, but the vendor's own terms and the
  home institution's rules on paid recruitment both apply, and the home institution's
  compensation and tax thresholds still govern.

Record the answer in the working draft's provenance block alongside the governing document
and the base protocol.

## 2. What to fetch

A source-type checklist, not a URL list — every institution publishes these under different
names. Use WebSearch to locate each, WebFetch to read it. Search patterns that work:
`<institution> IRB application instructions`, `<institution> informed consent template`,
`<institution> exempt categories`, `site:<domain> research compliance human subjects`.

| # | Source type | What it settles in the institution file |
|---|---|---|
| 1 | Human-subjects / IRB landing page | Which office, submission address, entry point to everything else |
| 2 | Application instructions | **The required narrative headings and their order** — §3 of the file. Usually also the mechanics |
| 3 | Forms / instructions / samples index | §12: what to use rather than author |
| 4 | Consent form sample(s) | §4: heading order and closing block |
| 5 | Informed consent checklist | §5: required disclosures, reading level, concise-summary trigger |
| 6 | Exemption categories page | §8: which category the protocol can claim |
| 7 | IRB policy document (dated PDF) | §8 review categories, §9 vulnerable populations, continuing review |
| 8 | Modification request process | §10: what counts as a modification vs. a new study |
| 9 | Submission mechanics page | §2 hard gates: file format, attachments, page numbering |
| 10 | Review timing / meeting calendar | §8: deadlines, expected turnaround |
| 11 | Compensation and payment policy | §7: gift-card rules, tax-reporting thresholds |
| 12 | Vulnerable-populations guidance | §9 |
| 13 | Training prerequisites (CITI or equivalent) | §2 or §3, per how the institution gates it |

Any source type you cannot find is recorded as `UNVERIFIED` in the file with the searches
you tried. A gap you can see is worth far more than a gap you filled.

## 3. Recording rules

These are the point of the exercise. A rules file that cannot be trusted quote-by-quote is
worse than no rules file, because the compliance pass will cite it to the PI.

- **Exact quotes, with URL and fetch date.** Never paraphrase a hard gate. The pass reports
  violations by quoting the rule back; a paraphrase becomes a rule the institution never wrote.
- **Never assert an unsourced rule.** If it is not on a page you fetched, it is `UNVERIFIED`.
  This is not caution for its own sake: during the 2026-07-28 UMaine research, an automated
  page summary produced a fluent, plausible sentence about a single protocol covering
  "multiple participant populations or study arms" with "coherent scientific objectives and
  unified ethical oversight." No UMaine page contains it. See `institutions/umaine.md` §13.
  A fabricated rule is the failure mode this file exists to prevent.
- **Record published rule and approved practice separately when they conflict.** They will.
  A board routinely approves forms that depart from its own published sample. The file
  carries both, plus one line naming which to follow and what the evidence is. Do not
  silently keep the one you prefer — the next person needs to know a conflict exists.
  UMaine has at least four: consent heading order, the closing block, recording retention,
  and vendor naming.
- **Distinguish "returned unread" from "reviewer might ask."** Only the first belongs in §2
  hard gates. Inflating a preference into a gate makes the pass cry wolf and trains the PI
  to ignore it.
- **Quote the dollar amounts and dates verbatim**, including thresholds. These get compared
  arithmetically against the draft, so a rounded number is a wrong number.

## 4. The institution file template

Thirteen sections, in this order. Keep the numbering stable — `compliance-check.md` refers
to sections by number.

```
# Institution: <name> (<short>)

Slug · reviewing body · submission address
Fetched and verified <date>. Refresh if >1 semester old or on announced process change.

1.  Sources                       — every URL, as a link list
2.  Hard gates                    — returned-unread items, as a checkbox list
3.  Required narrative headings   — in order, plus what must be removed
4.  Consent form structure        — published order; approved-in-practice order; which wins
5.  Required consent disclosures  — concise summary trigger, reading level, examples, burden
6.  Confidentiality disclosures   — vendors, IP, recordings, key, access, dates
7.  Compensation                  — rules, vendor/value, withdrawal, thresholds
8.  Review categories and timing  — categories, deadlines, turnaround, continuing review
9.  Vulnerable populations        — who must be named and justified
10. Modifications                 — mod vs. new study; mechanics
11. Multi-site and reliance       — arrangements available
12. Templates to use              — rather than author
13. Unverified and corrections    — gaps, conflicts unresolved, fabrications caught
```

Sections 5–9 are what the compliance pass spends most of its time on. Sections 2 and 3 are
what get an application returned.

## 5. Staleness

- Refresh if the file is more than one semester old.
- Refresh immediately if the institution announces a process change, and record the
  announcement in §13 until it is confirmed in effect. UMaine has one outstanding as of
  2026-07-28.
- Refresh the specific section if a board response contradicts it — and log the
  contradiction, since a board that enforces a rule differently than it publishes it is the
  most valuable thing in the file.

## 6. Where new rules land after a board response

- Returned for a **mechanics** reason → `institutions/<slug>.md` §2. It was a hard gate and
  the file was missing it.
- Board **required a change** to substance → `board-rules.md` (empirical board behavior),
  and cross-reference from the institution file if it conflicts with a published rule.
- Board **accepted** something the published rules seem to forbid → the conflict entry in
  §4/§5/§6/§7 of the institution file, as approved practice with the approval as evidence.
