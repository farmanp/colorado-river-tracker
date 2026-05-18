#!/bin/bash
# Test the scraper command exactly as cron will run it

PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin/python3"
PROJECT_DIR="/Users/farman/Documents/investigations/colorado_river"

echo "Testing scraper command (exactly as cron will run it)..."
echo "=========================================="
echo ""

cd "$PROJECT_DIR" && "$PYTHON_PATH" scraper/fetch_reservoirs.py

EXIT_CODE=$?

echo ""
echo "=========================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ SUCCESS - Scraper ran successfully"
    echo ""
    echo "Check the output:"
    echo "  cat data.json"
    echo ""
    echo "Check the log:"
    echo "  tail -20 scraper/fetch.log"
else
    echo "❌ FAILED - Exit code: $EXIT_CODE"
    echo ""
    echo "Check the log for errors:"
    echo "  tail -50 scraper/fetch.log"
fi

exit $EXIT_CODE
