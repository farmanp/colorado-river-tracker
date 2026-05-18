#!/usr/bin/env python3
"""
fetch_reservoirs.py — Pulls current Lake Mead and Lake Powell elevations from USBR.

Run manually:    python3 scraper/fetch_reservoirs.py
Run via cron:    0 */6 * * * cd /path/to/repo && /usr/bin/python3 scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1

Outputs:
  - data.json         Project-root JSON with current reservoir state (consumed by the HTML page)
  - scraper/fetch.log Append-only log of fetches and errors

Dependencies: Python 3.9+, requests (pip install requests)

Sourcing: This script pulls from publicly available USBR endpoints.
  - Lake Mead: https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html
  - Lake Powell: https://www.usbr.gov/uc/water/crsp/cs/gcd.html

If the page structures change (likely over time), update the parsing logic.
Always preserve previous good data if a fetch fails — never overwrite with errors.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


# Reference values for percentage-full calculation
RESERVOIRS = {
    "lake_powell": {
        "name": "Lake Powell",
        "url": "https://www.usbr.gov/uc/water/crsp/cs/gcd.html",
        "full_pool_ft": 3700,
        "dead_pool_ft": 3370,
    },
    "lake_mead": {
        "name": "Lake Mead",
        "url": "https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html",
        "full_pool_ft": 1229,
        "dead_pool_ft": 895,
    },
}

USER_AGENT = (
    "Mozilla/5.0 (compatible; ColoradoRiverTracker/0.1; "
    "+https://github.com/colorado-river-accountability/tracker)"
)

HEADERS = {"User-Agent": USER_AGENT}
TIMEOUT = 30  # seconds

# Where to write outputs (relative to repo root)
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data.json"
LOG_FILE = REPO_ROOT / "scraper" / "fetch.log"


def log(msg: str) -> None:
    """Append a timestamped message to the log file and print to stdout."""
    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"[{timestamp}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a") as f:
        f.write(line + "\n")


def extract_elevation_ft(html: str, reservoir_name: str) -> float | None:
    """
    Extract a reservoir elevation in feet from a USBR HTML page.

    USBR pages embed elevations in tables and prose. This uses improved
    regex patterns that handle comma separators and searches in reverse
    order to avoid historical data tables.

    Known issues fixed (2026-05-17):
    - Lake Powell: Numbers formatted as "3,527.99" with comma separator
    - Lake Mead: Historical table from 1936-present; need recent data only
    """
    # Pattern handles both "3527.99" and "3,527.99" formats
    # Matches 4-digit elevations with optional comma after first digit
    candidates = re.findall(r"\b([1-3],?\d{3}\.\d{1,2})\b", html)

    # Lake Mead page has historical table dating back to 1936.
    # Recent data appears later in the document, so search in reverse.
    if "mead" in reservoir_name.lower():
        candidates = reversed(candidates)

    for c in candidates:
        # Remove comma before converting to float
        val = float(c.replace(",", ""))
        if 800 <= val <= 3800:
            return val
    return None


def fetch_reservoir(key: str, meta: dict, previous_data: dict | None = None) -> dict:
    """Fetch a single reservoir's current elevation and compute % full."""
    try:
        resp = requests.get(meta["url"], headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as e:
        log(f"FETCH ERROR for {meta['name']}: {e}")
        return {"error": str(e)}

    elevation = extract_elevation_ft(resp.text, meta["name"])
    if elevation is None:
        log(f"PARSE ERROR for {meta['name']}: no elevation found in response")
        return {"error": "could not parse elevation"}

    full = meta["full_pool_ft"]
    dead = meta["dead_pool_ft"]
    pct_full = round(((elevation - dead) / (full - dead)) * 100, 1)

    # Validation: Check for suspicious changes if we have previous data
    if previous_data and "elevation_ft" in previous_data:
        prev_elev = previous_data["elevation_ft"]
        change_ft = elevation - prev_elev
        abs_change = abs(change_ft)

        if abs_change > 100:
            log(
                f"WARNING: {meta['name']} elevation change of {change_ft:+.2f} ft "
                f"exceeds ±100 ft threshold (prev: {prev_elev} ft, new: {elevation} ft). "
                f"Possible parsing bug. Writing data anyway for manual review."
            )

        # Log with change indicator
        log(f"{meta['name']}: {elevation} ft ({pct_full}% full) [{change_ft:+.2f} ft from previous]")
    else:
        # First run or no previous data
        log(f"{meta['name']}: {elevation} ft ({pct_full}% full)")

    return {
        "name": meta["name"],
        "elevation_ft": elevation,
        "pct_full": pct_full,
        "full_pool_ft": full,
        "dead_pool_ft": dead,
        "source_url": meta["url"],
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def load_previous() -> dict:
    """Load the existing data.json so we can preserve good data on partial failures."""
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open() as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        log(f"WARN: could not read previous data.json ({e}); starting fresh")
        return {}


def main() -> int:
    log("=== fetch_reservoirs.py starting ===")
    previous = load_previous()
    reservoirs_out = previous.get("reservoirs", {})

    any_success = False
    for key, meta in RESERVOIRS.items():
        # Pass previous data for this reservoir to enable change detection
        previous_reservoir = reservoirs_out.get(key) if key in reservoirs_out else None
        result = fetch_reservoir(key, meta, previous_reservoir)
        if "error" not in result:
            reservoirs_out[key] = result
            any_success = True
        else:
            # Keep previous good data if available, but log the failure
            if key in reservoirs_out:
                log(f"keeping previous data for {meta['name']}")
            else:
                reservoirs_out[key] = result  # write the error so the page can show "unavailable"

    output = {
        "last_run": datetime.now(timezone.utc).isoformat(),
        "reservoirs": reservoirs_out,
    }

    with DATA_FILE.open("w") as f:
        json.dump(output, f, indent=2)

    if any_success:
        log(f"wrote {DATA_FILE}")
        log("=== done ===\n")
        return 0
    else:
        log("ALL FETCHES FAILED — no fresh data written this run")
        log("=== done (with errors) ===\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
