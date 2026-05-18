# Next Steps — Colorado River Tracker

Queued tasks in rough priority order. Pick one, do it, mark it done.

---

## Priority 1 — Outreach for comment

(Moved up from Priority 4 — technical work complete)



**Task:** Refactor the reservoir section of `colorado-river-tracker.html` to:
1. Fetch `data.json` on page load
2. Update the reservoir % full numbers from the JSON
3. Update the "as of" timestamp visible to the reader
4. Fall back to the existing hardcoded values if the fetch fails
5. Show a small "Live data" badge when fresh data loads, vs. "Cached" when falling back

**Don't** introduce a build step or framework. Vanilla `fetch()` is fine.

---

## Priority 3 — Set up the cron job

Once scraper is tested in production, add a crontab entry:

```bash
# macOS / Linux
crontab -e

# Add (runs every 6 hours):
0 */6 * * * cd /path/to/colorado-tracker && /usr/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1
```

Verify it runs by checking `fetch.log` after the next scheduled time.

---

## Priority 4 — Outreach for comment

Standard journalism practice. Email each state's communications office:

- [ ] **Arizona DWR**: communications@azwater.gov
- [ ] **California CO River Board**: via crb.ca.gov contact
- [ ] **Nevada SNWA**: via snwa.com media contact
- [ ] **Colorado**: via cwcb.colorado.gov press contact
- [ ] **Utah**: via Utah Division of Water Resources
- [ ] **Wyoming**: via Wyoming State Engineer's Office
- [ ] **New Mexico**: via Interstate Stream Commission
- [ ] **UCRC media contacts** (from press release):
  - Matt Moseley: mmoseley@ignitionstrategygroup.com / 303-887-0826
  - Kendra Westerkamp: Kendra@C4Spark.com / 720-261-2300

**Template:**
> Hi [name], I'm preparing an accountability tracker on Colorado River post-2026 negotiations. Can you confirm your state's current position on [X] and the lead negotiator's contact for follow-up? Publication is scheduled for [date].
>
> Specific questions:
> 1. Is [negotiator name] still your state's lead representative on the post-2026 negotiations?
> 2. What is your state's response to the May 1, 2026 Lower Basin proposal?
> 3. Would you be available for a brief phone interview before [date]?
>
> Thank you for your time.

Track responses in `outreach_log.md` (create this file as responses come in). Include "declined to comment" — silence is publishable data.

---

## Priority 3 — Formal citations

Once reservoir scraping works:

1. **UCRC press releases.** Parse http://www.ucrcommission.com/blog/ for new posts. Extract date, headline, body. Save raw text to `scraper/data/ucrc/[date].txt`. Don't try to extract structured data automatically — that's Layer 4.

2. **Reclamation newsroom.** Parse https://www.usbr.gov/newsroom/ for Colorado River-related items.

3. **State water agency news pages.** Each state's primary water agency has a press releases page. Catalog the URLs, write scrapers for each.

When new content is detected, log it to `review_queue.md` for human review. The human (you) decides whether it's accountability-relevant before anything reaches the dashboard.

---

## Priority 4 — Publish

Once Priorities 1-3 are done:

1. Push to a GitHub repo
2. Enable GitHub Pages (free static hosting)
3. Or deploy to Netlify / Vercel (also free)
4. Add Open Graph tags to the HTML for social sharing
5. Pick a final headline
6. Write a 200-word "About this project" page explaining the sourcing standard

---

## Priority 5 — Live data wiring (Layer 1 polish)

Polish for credibility:

- Locate DOI for Richter et al. 2024 and add to methodology footer
- Locate full James et al. 2014 citation and add to methodology footer
- Verify the SJ-Chama Project reference
- Add a "How to cite this tracker" snippet at the bottom

---

## Archive — Already Completed

Once scraping works reliably:

- Add snowpack data from NRCS SNOTEL
- Add a small "What changed since last update" diff
- Add a sparkline showing reservoir levels over the last 12 months

---

## Done (don't redo)

- ✅ Initial draft HTML
- ✅ Tier-based fact-check audit
- ✅ Upper Basin commissioner names verified (UCRC press release)
- ✅ Upper Basin quotes verified (UCRC press release)
- ✅ Reservoir levels updated to USBR April 2026 data
- ✅ $1.4T economic figure traced to James et al. 2014
- ✅ SNWA 90% figure verified to primary source
- ✅ Federal 40% / 3M ac-ft figure verified (Reuters May 15, 2026)
- ✅ Methodology footer added
- ✅ State card hover/click background fix for Upper Basin cards
- ✅ **Python scraper built and tested** (May 17, 2026)
  - Fetches Lake Mead and Lake Powell elevations from USBR
  - Calculates % full, writes to `data.json`
  - **Initial test revealed 2 critical bugs** (both fixed):
    1. Lake Mead scraped 1936 historical data instead of current 2026
    2. Lake Powell failed due to comma separators in "3,527.99"
  - **Fixed with improved regex** + reverse search for recent data
  - **Verified output**: Powell 3,527.99 ft (47.9%), Mead 1,056.32 ft (48.3%)
  - See `scraper/TEST_RESULTS.md` for full test report
- ✅ **Scraper production improvements** (May 17, 2026)
  - Fixed User-Agent: github.com/colorado-river-accountability/tracker
  - Added validation layer: warns if elevation changes >±100 ft
  - Enhanced logging: shows `[+2.1 ft from previous]` change indicators
  - Ready for cron deployment
- ✅ **HTML to data.json integration** (May 17, 2026)
  - Vanilla JavaScript fetch on page load
  - Updates reservoir percentages dynamically (23%→48%, 30%→48%)
  - Shows "Cached" badge (will become "Live" after deployment)
  - Graceful fallback if JSON missing
  - See `DATA_INTEGRATION_NOTES.md` and `TESTING_GUIDE.md`
- ✅ **Pledged vs Delivered split implemented** (May 17, 2026)
  - **Most important editorial improvement** - distinguishes commitments from actions
  - State cards now show allocation context:
    - AZ: 760K (27.1% of 2.8M allocation)
    - CA: 440K (10.0% of 4.4M allocation)
    - NV: 50K (16.7% of 300K allocation)
  - Expanded details show full breakdown with "Delivered" scaffolding
  - Upper Basin shows "No mandatory cuts" with context about snowmelt argument
  - Section intro clarifies: "Pledged shows commitments; Delivered will track actual reductions"
- ✅ **Cron automation ready** (May 17, 2026)
  - Helper scripts created: `add_cron.sh`, `test_scraper.sh`
  - Comprehensive guide: `CRON_SETUP.md`
  - Configured for every 6 hours (12am, 6am, 12pm, 6pm)
  - User needs to run: `bash add_cron.sh` to activate
