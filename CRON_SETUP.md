# Cron Automation Setup

This guide sets up automated scraping every 6 hours using cron (macOS/Linux).

---

## Quick Setup

### 1. Open crontab editor

```bash
crontab -e
```

This opens your crontab file in your default editor (usually `vi` or `nano`).

### 2. Add this line

```cron
0 */6 * * * cd /Users/farman/Documents/investigations/colorado_river && /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1
```

**What this does:**
- `0 */6 * * *` — Run at minute 0 of every 6th hour (12am, 6am, 12pm, 6pm)
- `cd /Users/...` — Change to project directory
- `python3 scraper/fetch_reservoirs.py` — Run the scraper
- `>> scraper/fetch.log 2>&1` — Append output to log file

### 3. Save and exit

- **vi:** Press `Esc`, then type `:wq` and press Enter
- **nano:** Press `Ctrl+X`, then `Y`, then Enter

### 4. Verify cron job was added

```bash
crontab -l
```

You should see your new cron entry listed.

---

## macOS-Specific: Grant Cron Permissions

On macOS, cron needs permission to access files. If scraper fails with permission errors:

1. **Open System Settings** → **Privacy & Security** → **Full Disk Access**
2. Click the **+** button
3. Navigate to `/usr/sbin/cron` and add it
4. Restart your Mac (or reload cron: `sudo launchctl unload /System/Library/LaunchDaemons/com.vix.cron.plist && sudo launchctl load /System/Library/LaunchDaemons/com.vix.cron.plist`)

---

## Testing

### Test the command manually first

Run the exact cron command to verify it works:

```bash
cd /Users/farman/Documents/investigations/colorado_river && /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1
```

Check the log:
```bash
tail -20 scraper/fetch.log
```

You should see:
```
[2026-05-17T...] === fetch_reservoirs.py starting ===
[2026-05-17T...] Lake Powell: 3527.99 ft (47.9% full) [+0.00 ft from previous]
[2026-05-17T...] Lake Mead: 1056.32 ft (48.3% full) [+0.00 ft from previous]
[2026-05-17T...] wrote /Users/farman/Documents/investigations/colorado_river/data.json
[2026-05-17T...] === done ===
```

### Wait for next scheduled run

After adding to cron, the next run will be at the next 6-hour mark (12am, 6am, 12pm, or 6pm).

To verify it ran, check the log:
```bash
tail -50 scraper/fetch.log | grep "=== fetch_reservoirs"
```

---

## Alternative Schedule Options

### Every 4 hours
```cron
0 */4 * * * cd /Users/farman/Documents/investigations/colorado_river && /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1
```

### Every 12 hours (noon and midnight)
```cron
0 0,12 * * * cd /Users/farman/Documents/investigations/colorado_river && /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1
```

### Daily at 6am
```cron
0 6 * * * cd /Users/farman/Documents/investigations/colorado_river && /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1
```

---

## Monitoring

### Check recent runs
```bash
tail -100 scraper/fetch.log
```

### Count successful runs today
```bash
grep "=== done ===" scraper/fetch.log | grep "$(date +%Y-%m-%d)" | wc -l
```

### Check for errors
```bash
grep -i "error\|warning" scraper/fetch.log | tail -20
```

### See change trends
```bash
grep "from previous" scraper/fetch.log | tail -10
```

---

## Troubleshooting

### Cron not running?

**Check if cron is running:**
```bash
ps aux | grep cron
```

**Check system log for cron errors:**
```bash
log show --predicate 'process == "cron"' --last 1h
```

### Permission denied errors?

- Grant Full Disk Access to `/usr/sbin/cron` (see macOS section above)
- Verify file ownership: `ls -la scraper/`
- Make sure Python path is correct: `which python3`

### Scraper runs but fails?

**Test manually:**
```bash
cd /Users/farman/Documents/investigations/colorado_river
python3 scraper/fetch_reservoirs.py
```

**Check network:**
```bash
curl -s https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html | head -20
```

### Log file not updating?

- Verify log path in cron command matches: `scraper/fetch.log`
- Check disk space: `df -h`
- Ensure cron has write permission: `touch scraper/test.log && rm scraper/test.log`

---

## Disabling Cron

To temporarily disable without deleting:

```bash
crontab -e
```

Add `#` at start of line:
```cron
# 0 */6 * * * cd /Users/farman/Documents/investigations/colorado_river && ...
```

To remove entirely:
```bash
crontab -e
```
Delete the line, save and exit.

---

## Production Notes

**Before deploying publicly:**

1. ✅ Scraper tested and working (DONE)
2. ✅ Validation layer active (DONE)
3. ⏳ Update User-Agent if needed (currently points to github.com/colorado-river-accountability/tracker)
4. ⏳ Consider email alerts on failures (optional)
5. ⏳ Monitor log file size growth (rotate if needed)

**Log rotation** (if file gets too large):
```bash
# Add to crontab to rotate weekly
0 0 * * 0 cp /Users/farman/Documents/investigations/colorado_river/scraper/fetch.log /Users/farman/Documents/investigations/colorado_river/scraper/fetch.log.old && echo "" > /Users/farman/Documents/investigations/colorado_river/scraper/fetch.log
```

---

## Current Configuration

- **Python:** `/Library/Frameworks/Python.framework/Versions/3.11/bin/python3`
- **Project:** `/Users/farman/Documents/investigations/colorado_river`
- **Scraper:** `scraper/fetch_reservoirs.py`
- **Output:** `data.json` (project root)
- **Log:** `scraper/fetch.log` (append-only)
- **Frequency:** Every 6 hours
- **Dependencies:** `requests` library (already installed)

---

## Status

- [x] Scraper working correctly
- [x] Test run successful
- [ ] Cron job added (do this now!)
- [ ] Verified first automated run
- [ ] Monitoring established
