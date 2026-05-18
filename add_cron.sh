#!/bin/bash
# Helper script to add scraper to crontab
# Run with: bash add_cron.sh

PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin/python3"
PROJECT_DIR="/Users/farman/Documents/investigations/colorado_river"

echo "Colorado River Tracker - Cron Setup"
echo "===================================="
echo ""
echo "This will add the scraper to run every 6 hours (12am, 6am, 12pm, 6pm)"
echo ""
echo "Cron entry that will be added:"
echo "0 */6 * * * cd $PROJECT_DIR && $PYTHON_PATH scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Check if entry already exists
    if crontab -l 2>/dev/null | grep -q "fetch_reservoirs.py"; then
        echo "❌ Cron entry already exists!"
        echo ""
        echo "Current crontab entries for this project:"
        crontab -l | grep "fetch_reservoirs"
        echo ""
        echo "To modify, run: crontab -e"
        exit 1
    fi

    # Add new entry
    (crontab -l 2>/dev/null; echo "0 */6 * * * cd $PROJECT_DIR && $PYTHON_PATH scraper/fetch_reservoirs.py >> scraper/fetch.log 2>&1") | crontab -

    echo "✅ Cron job added successfully!"
    echo ""
    echo "Current crontab:"
    crontab -l
    echo ""
    echo "📋 Next steps:"
    echo "1. Test manually: bash test_scraper.sh"
    echo "2. Wait for next scheduled run (see CRON_SETUP.md for schedule)"
    echo "3. Monitor: tail -f scraper/fetch.log"
    echo ""
    echo "⚠️  macOS users: If it fails, grant Full Disk Access to /usr/sbin/cron"
    echo "   Settings → Privacy & Security → Full Disk Access → + → /usr/sbin/cron"
else
    echo "❌ Cancelled. No changes made."
    exit 0
fi
