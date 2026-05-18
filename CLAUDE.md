# CLAUDE.md — Colorado River Accountability Tracker

This file primes Claude Code for working on this project. Read this before making any changes.

---

## What this project is

An investigative journalism accountability tracker for the seven-state Colorado River water crisis negotiations. The deliverable is a clickable HTML dashboard plus an automated data pipeline that pulls primary-source data on a schedule.

**Tone:** Editorial / data journalism. Think ProPublica, The Markup, The Pudding. Newsprint aesthetic, serious but readable. NOT corporate dashboard, NOT government PDF.

**Audience:** General public + other journalists who can use this as a reporting tool.

---

## Core sourcing standard (DO NOT VIOLATE)

This is journalism, not aggregation. Every factual claim must be traceable to a primary or reputable secondary source. Use the three-tier system:

- **Tier 1 — Defensible:** Multiply confirmed by reputable sources OR sourced to a primary document (USBR press releases, UCRC press releases, peer-reviewed studies, government filings). Safe to publish.
- **Tier 2 — Needs cross-check:** Single reputable source. Attribute clearly; verify with primary docs if possible.
- **Tier 3 — Unverified / fabricated:** DO NOT PUBLISH. If a quote or name can't be sourced, remove it. Silence is more honest than fabrication.

**The previous version of this project caught three fabricated quotes attributed to real public officials.** Never let this happen again. If you can't find a real quote, leave the quote field blank or remove that part of the UI rather than inventing one.

Every claim in the HTML has an inline source comment like:
```html
<!-- CLAIM: X | TIER: 1 | SOURCE: Y -->
```

Maintain this convention for any new content you add.

---

## Current state of the project

**Files in this repo:**
- `colorado-river-tracker.html` — the verified v3 dashboard (single-file HTML, no build step)
- `fact-check-checklist.md` — the verification log; track every Tier 2 → Tier 1 upgrade here
- `PROJECT_CONTEXT.md` — human-readable background; read this for the full story
- `NEXT_STEPS.md` — the queued tasks in priority order
- `scraper/fetch_reservoirs.py` — starter script for USBR data (Phase 1 of automation)

**Verified facts (Tier 1, defensible):**
- 7 basin states split into Upper (CO/UT/WY/NM) and Lower (AZ/CA/NV) by 1922 Compact
- Lake Powell: ~3,526 ft / ~23% full (USBR April 2026 24-Month Study)
- Lake Mead: ~1,055 ft / ~30% full (same source)
- Lower Basin proposal May 1, 2026: AZ 760K + CA 440K + NV 50K = 3.2M ac-ft over 3 years
- Federal alternative: up to 3M ac-ft/year cuts (~40% of 7.5M Lower Basin allotment), per Reuters May 15, 2026
- $1.4T economic activity (James et al. 2014, ASU Seidman Research Institute)
- All 7 negotiator names verified to UCRC press release April 23, 2026 + secondary sources
- All 7 quotes verbatim from on-record reporting (see HTML source comments for citation)
- Sector breakdown 52% ag / 32% cattle feed / 19% nat veg / 18% M&C / 11% evaporation (Richter et al. 2024)
- SNWA: 58% per-capita reduction 2002-2025, +876K population (snwa.com primary)

**Known weaknesses to address:**
- Cut figures are "pledged" not "delivered" — the page currently doesn't distinguish. This is the most important structural improvement queued.
- Reservoir levels are hardcoded; should be read from `data.json` once the scraper exists.
- No formal DOI citations for Richter/James studies (Phase 3 polish).
- Some Tier 2 items remain (Las Vegas metro pop, turf rebate $3/sq ft) — attributed but not primary-verified.

---

## What's next (queued tasks)

See `NEXT_STEPS.md` for the full list. Top priorities:

1. **Pledged vs. Delivered split.** The UI implies states pledging cuts = states doing the work. They're not the same. Add a "Delivered" column that's empty for now (cuts haven't been measured yet for the 2026-2028 period) but sets up the tracking spine.

2. **Starter Python scraper.** `scraper/fetch_reservoirs.py` should fetch live Lake Mead and Lake Powell elevations from USBR's public endpoints, calculate % full, write to `data.json`. No dependencies beyond `requests`. Designed for laptop cron.

3. **HTML reads from JSON.** Refactor reservoir levels to read from `data.json` instead of hardcoded values. Page should still work if JSON is missing (fallback to hardcoded).

4. **Outreach for comment.** Phase 4 in the checklist — emails to each state's communications office. Standard journalism practice.

---

## Constraints

- **No paid services.** This runs free. Laptop cron, GitHub Actions free tier, no API costs unless explicitly approved.
- **No JavaScript build step.** The HTML is single-file with vanilla JS. Keep it that way for now. Don't introduce React, Vite, Webpack, etc.
- **No frameworks for the scraper.** Python stdlib + `requests` + `pdfplumber` if PDFs. Nothing heavier.
- **Mobile-first.** Always test the HTML at narrow viewports. Most readers will be on phones.
- **Accessibility.** Keep semantic HTML, sufficient contrast. The current design uses `--ink: #1a1612` on `--bg: #f4ede0` for AAA contrast.

---

## Style notes for the HTML

- Fonts: Fraunces (serif, editorial display + body) + JetBrains Mono (data labels)
- Color palette: cream/sand/rust/water-blue/black — newsprint-derived, no neon
- Section numbering convention: `§ 01 — Section Name`
- All formatting via CSS variables (`--ink`, `--rust`, etc.) — never hardcode hex
- State cards toggle `.open` class on click; hover and `.open` should both invert to dark background

---

## What NOT to do

- Don't add quotes you can't source to an on-record statement. Empty is better than fake.
- Don't infer current officeholders from training data. Check UCRC roster / state agency rosters.
- Don't write report-style markdown summaries for the user; this is a journalism project — speak in journalism terms.
- Don't add tracking, analytics, or third-party scripts to the HTML.
- Don't refactor working code "just because." The HTML is intentionally single-file.


<claude-mem-context>
# Recent Activity

<!-- This section is auto-generated by claude-mem. Edit content outside the tags. -->

*No recent activity*
</claude-mem-context>