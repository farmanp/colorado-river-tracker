# Publishing Checklist

Repository is currently **PRIVATE** on GitHub. This is correct during outreach phase.

---

## Current Status: Pre-Publication

**Repository:** https://github.com/farmanp/colorado-river-tracker (private)

**Testing:** Open `colorado-river-tracker.html` locally in browser
- Scraper runs every 6 hours automatically
- data.json updates in background
- HTML reads from local data.json

---

## When to Make Public

**After outreach is complete:**
- All 8 agencies contacted ✓ (send emails from `outreach_emails.md`)
- 14-day response window elapsed
- All responses logged in `outreach_log.md`
- Any corrections incorporated into tracker

**Timeline:** ~2-3 weeks from sending outreach emails

---

## Publication Steps

### Step 1: Make Repository Public

```bash
gh repo edit farmanp/colorado-river-tracker --visibility public
```

### Step 2: Enable GitHub Pages

```bash
gh api -X POST repos/farmanp/colorado-river-tracker/pages --input - <<'EOF'
{
  "source": {
    "branch": "gh-pages",
    "path": "/"
  }
}
EOF
```

### Step 3: Wait for Deployment (~2 minutes)

Check status:
```bash
gh api repos/farmanp/colorado-river-tracker/pages
```

### Step 4: Verify Live Site

Your site will be at:
```
https://farmanp.github.io/colorado-river-tracker/colorado-river-tracker.html
```

### Step 5: Announce

- Share URL with sources who responded
- Post to social media if desired
- Email colleagues/other journalists
- Submit to relevant journalism communities

---

## Pre-Publication Checklist

Before making public, verify:

- [ ] All 8 outreach emails sent
- [ ] 14-day response window complete
- [ ] All responses logged in `outreach_log.md`
- [ ] Any corrections incorporated
- [ ] Scraper running successfully (check `scraper/fetch.log`)
- [ ] data.json has recent data (last 6 hours)
- [ ] HTML tested locally and looks good
- [ ] All Tier 3 claims removed (nothing unverified)
- [ ] Methodology section accurate
- [ ] Attribution links work

---

## Post-Publication Monitoring

After going live:

**Daily (first week):**
- Check for responses from sources
- Monitor scraper logs for errors
- Watch for any corrections needed

**Weekly (ongoing):**
- Review data.json updates
- Check for new press releases
- Update if major developments

---

## Updating Live Site

After publication, any changes pushed to `main` or `gh-pages` automatically deploy:

```bash
# Make changes locally
git add colorado-river-tracker.html
git commit -m "update: Correct California allocation figure"
git push

# Pushes to gh-pages too (or manually)
git push origin main:gh-pages
```

Changes go live in 1-2 minutes.

---

## Emergency Takedown

If you need to remove the site immediately:

```bash
# Disable GitHub Pages
gh api -X DELETE repos/farmanp/colorado-river-tracker/pages

# Or make repo private
gh repo edit farmanp/colorado-river-tracker --visibility private
```

Only do this if there's a serious factual error or legal issue.

---

## Current Timeline

**Today (May 17):**
- ✅ Repository created (private)
- ✅ Code pushed
- ✅ Testing locally

**Next:**
1. Send outreach emails (use `outreach_emails.md`)
2. Wait 14 days for responses
3. Incorporate any feedback
4. Run publication steps above
5. Go live!

**Target publication:** ~June 1-5, 2026

---

## Quick Commands

**Test locally:**
```bash
open colorado-river-tracker.html
```

**Check scraper:**
```bash
tail -20 scraper/fetch.log
```

**See latest data:**
```bash
cat data.json | python3 -m json.tool
```

**When ready to publish:**
```bash
bash PUBLISH.sh  # (create this script with steps above)
```

---

You're set! Test locally during outreach, then make it public when ready to launch.
