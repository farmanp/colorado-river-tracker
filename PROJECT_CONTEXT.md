# Project Context — Colorado River Accountability Tracker

## The story behind this project

The seven U.S. states that share the Colorado River are running out of time. The 2007 Interim Guidelines that have governed Lake Mead and Lake Powell for nearly two decades expire on December 31, 2026. The states missed federal deadlines in November 2025 and February 2026 to agree on new operating rules. As of May 2026, the basin is split:

- **Lower Basin (Arizona, California, Nevada)** filed a "bridge proposal" on May 1, 2026 promising 3.2M acre-feet in cuts over three years.
- **Upper Basin (Colorado, Utah, Wyoming, New Mexico)** rejected mandatory cuts on April 23, 2026 and called for a third-party mediator.
- **The Bureau of Reclamation** has signaled it will impose its own plan if the states don't agree — with cuts of up to 40% of Lower Basin allocations.

Meanwhile, Lake Powell sits at ~23% full and Lake Mead at ~30%. Forty million people depend on the river. $1.4 trillion in economic activity hangs on its continued flow.

Beneath the political theater is an uncomfortable fact: **agriculture consumes 52% of the river, and cattle-feed crops alone consume 32%.** The fight over which states should cut is, fundamentally, a fight over whether anyone will touch alfalfa farming.

## Why this project exists

Most coverage of the negotiations is event-driven: "deadline missed," "proposal filed," "state X criticizes state Y." There's no single place that tracks:

1. **What each state has actually pledged.** Not what they say in press releases — the specific acre-feet they've committed to cutting.
2. **Who their lead negotiators are** and what they've said on the record.
3. **How those pledges compare to what's needed** to stabilize the system.
4. **Whether anyone is delivering on their pledges** vs. just announcing them.
5. **Who's actually consuming the water** that's being negotiated.

This project fills that gap with a single-page dashboard, sourced to primary documents, with a transparent fact-check trail.

## What's been built so far

**Phase 1 — Initial draft:** A static HTML dashboard with hardcoded data drawn from secondary reporting (KJZZ, NPR, Reuters, PBS NewsHour, Nevada Independent).

**Phase 2 — Fact-check audit:** Discovered that three quotes attributed to Upper Basin commissioners (Shawcroft, Gebhart, Lopez) were fabricated paraphrases of general positions, not verbatim quotes. Flagged them in a "Working Draft" banner.

**Phase 3 — Primary source verification:** Located the Upper Colorado River Commission press release dated April 23, 2026, which contained verbatim quotes from all four Upper Basin commissioners. Replaced all fabricated content with real on-record quotes. Updated reservoir figures to match USBR April 2026 24-Month Study. Verified $1.4T economic figure to James et al. 2014 (ASU). Confirmed Reuters' May 15, 2026 reporting on the federal 40% / 3M ac-ft alternative.

**Result:** A "v3 Verified Draft" with every major claim Tier 1 sourced, a transparent fact-check checklist, and inline source comments on every factual claim in the HTML.

## What hasn't been built yet

- A **pledged vs. delivered** split. Right now the UI implies a state's pledge = its action. They're not the same.
- An **automated data pipeline** to keep reservoir levels current.
- An **outreach record** showing which state agencies have been contacted for comment.
- A **publication home** with a real URL.

## The bigger vision

Build a layered retrieval system for water-policy accountability:

- **Layer 1 (automated):** USBR reservoir data, snowpack, federal announcements
- **Layer 2 (light scraping):** UCRC press releases, state water agency news pages
- **Layer 3 (browser automation, optional):** JS-heavy dashboards, anything behind anti-bot protection
- **Layer 4 (LLM extraction, optional):** structured data from press releases, news articles
- **Layer 5 (human editorial):** verification, interpretation, outreach, the actual journalism

Start with Layer 1 only. Add layers as the project warrants.

## Files in this repository

- `colorado-river-tracker.html` — the dashboard itself (open in browser to view)
- `fact-check-checklist.md` — verification log
- `CLAUDE.md` — instructions for Claude Code
- `PROJECT_CONTEXT.md` — this file
- `NEXT_STEPS.md` — queued tasks
- `scraper/fetch_reservoirs.py` — starter script for USBR data

## Key sources

**Primary:**
- USBR April 2026 24-Month Study: https://www.usbr.gov/lc/region/g4000/24mo.pdf
- UCRC press release April 23, 2026: http://www.ucrcommission.com/wp-content/uploads/2026/04/UCRC_NewsRelease_Mediation_23April2026_FINAL.pdf
- SNWA water source page: https://www.snwa.com/water-resources/where-water-comes-from/
- USBR Lake Mead live elevation: https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html
- USBR Lake Powell data: https://www.usbr.gov/uc/water/crsp/cs/gcd.html

**Secondary (reputable):**
- KJZZ reporting (Ron Dungan)
- NPR (Kirk Siegler)
- Reuters / 8 News Now (May 15, 2026 federal 40% story)
- Nevada Independent (Daniel Rothberg)
- Maven's Notebook

**Studies cited:**
- Richter, B.D. et al. 2024. "New water accounting reveals why the Colorado River no longer reaches the sea." *Communications Earth & Environment.*
- James, T. et al. 2014. ASU L. William Seidman Research Institute, commissioned by Protect the Flows.

## Sourcing philosophy

This is journalism. The standard is not "true to the best of my knowledge" — the standard is "I can show you the document." If a fact can't be linked to a primary or reputable secondary source, it doesn't go in the dashboard. The fact-check checklist tracks every claim by tier, and the inline HTML source comments tell readers exactly where each number came from.

If you're handing this to Claude Code or another collaborator, the first thing they should read is `CLAUDE.md`. The second is this file. The third is the checklist.
