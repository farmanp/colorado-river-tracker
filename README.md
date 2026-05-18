# Colorado River Accountability Tracker

An investigative journalism accountability tracker for the seven-state Colorado River water crisis negotiations.

**Status:** Pre-publication (outreach phase) — all claims verified to primary sources, automated data pipeline operational.

**What makes this different:** Distinguishes between states' **pledged** cuts and **delivered** reductions. Shows percentage of each state's allocation. Updates reservoir levels automatically every 6 hours via USBR data.

## What's in this repo

### **Core Files**
| File | What it is |
|---|---|
| `colorado-river-tracker.html` | The dashboard — single-file HTML, no build step |
| `data.json` | Live reservoir data (auto-updated by scraper) |
| `scraper/fetch_reservoirs.py` | Production-ready scraper with validation |

### **Documentation**
| File | What it is |
|---|---|
| `PROJECT_CONTEXT.md` | Full project history and lessons learned |
| `fact-check-checklist.md` | Verification log — every claim, every source |
| `NEXT_STEPS.md` | Remaining priorities (outreach, publish, expand) |
| `CLAUDE.md` | Project guidelines and sourcing standards |

### **Outreach Materials**
| File | What it is |
|---|---|
| `outreach_emails.md` | Ready-to-send email templates (8 agencies) |
| `outreach_log.md` | Response tracking spreadsheet |
| `OUTREACH_GUIDE.md` | Complete outreach workflow |

### **Playbooks**
| Directory | What it is |
|---|---|
| `playbooks/` | Investigative journalism workflows (IRE/ProPublica standards) |

### **Automation**
| File | What it is |
|---|---|
| `add_cron.sh` | Helper script to set up automated scraping |
| `test_scraper.sh` | Test scraper before deployment |
| `CRON_SETUP.md` | Complete automation guide |

## Quick start

### View the dashboard

Just open `colorado-river-tracker.html` in any modern browser. No build step, no server needed.

### Run the scraper

```bash
# Test the scraper
bash test_scraper.sh

# Check the output
cat data.json | python3 -m json.tool
tail -20 scraper/fetch.log
```

**Expected output:**
- Lake Powell: ~3,528 ft (~48% full)
- Lake Mead: ~1,056 ft (~48% full)

### Set up automation

```bash
# Quick setup (recommended)
bash add_cron.sh

# Or manual setup - see CRON_SETUP.md for full guide
```

The scraper runs every 6 hours (12am, 6am, 12pm, 6pm) and updates `data.json` automatically. The HTML page reads from `data.json` on load.

## Handing off to Claude Code

In your terminal:

```bash
cd /path/to/this/repo
claude
```

Claude Code reads `CLAUDE.md` automatically and picks up the project context. The first thing to ask it: **"Read CLAUDE.md, PROJECT_CONTEXT.md, and NEXT_STEPS.md, then tell me what you understand about this project."**

If that summary matches reality, you're set up. Pick a task from `NEXT_STEPS.md` and go.

## Methodology

### Sourcing Standard

Every factual claim is verified using a three-tier system:

- **Tier 1 (Defensible):** Multiply confirmed by reputable sources OR primary source (USBR data, government filings, academic studies). Safe to publish.
- **Tier 2 (Needs Cross-Check):** Single reputable source. Attribute explicitly.
- **Tier 3 (Unverified):** DO NOT PUBLISH. If unverifiable, remove the claim.

See `fact-check-checklist.md` for full verification audit trail.

### Investigative Playbooks

Systematic workflows based on IRE, ProPublica, and ICIJ best practices:
- Claim intake & triage
- Source verification
- Contradiction protocols
- See `playbooks/` directory for complete methodology

### Automation

- **Scraper:** Validates data quality, logs changes, alerts on anomalies (>100ft jumps)
- **Live updates:** Every 6 hours via cron
- **Graceful degradation:** Falls back to hardcoded values if scraper fails
- **Audit trail:** All scraper runs logged to `scraper/fetch.log`

## Current Status

**✅ Complete:**
- HTML tracker with pledged vs delivered split
- Automated data pipeline (scraper + validation)
- Verification audit trail (all Tier 1 claims)
- Outreach materials ready

**⏳ In Progress:**
- Pre-publication outreach (7 states + UCRC)

**📝 Next:**
- Publish after outreach responses (2-3 weeks)
- Deploy to GitHub Pages / Netlify
- Expand Phase 2 scrapers (press releases)

## Contributing

This is an open journalism project. Contributions welcome:
- **Data verification:** Found an error? Open an issue with source documentation
- **Scraper improvements:** Better parsing, additional data sources
- **Documentation:** Playbook refinements, methodology clarifications

## License & Use

Built for accountability journalism. Use, remix, fork freely.

**Citation:** If you publish derivative work, cite the primary sources directly (USBR, UCRC, KJZZ, etc.) — not this tracker. See HTML source comments for exact attributions.

**Standards:** This project follows SPJ Code of Ethics and IRE investigative journalism best practices.
