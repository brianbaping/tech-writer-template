#!/bin/bash
# Bibliography Tracking Hook
# Runs after WebFetch operations to automatically log sources for citation

# This hook tracks all web sources fetched during research
# It maintains a running bibliography file for easy citation later

# Get tool parameters
URL=$(echo "$TOOL_PARAMS" | jq -r '.url // empty')
PROMPT=$(echo "$TOOL_PARAMS" | jq -r '.prompt // empty')

# Skip if no URL (shouldn't happen, but be safe)
if [ -z "$URL" ]; then
  exit 0
fi

# Bibliography tracking file
BIBLIO_FILE=".claude/cache/bibliography-sources.txt"

# Ensure the file exists
touch "$BIBLIO_FILE"

# Check if this URL is already tracked
if grep -q "$URL" "$BIBLIO_FILE"; then
  # Already tracked, skip
  exit 0
fi

# Add entry to bibliography tracking
{
  echo "---"
  echo "Date: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "URL: $URL"
  echo "Context: $PROMPT"
  echo "Status: Fetched successfully"
  echo ""
} >> "$BIBLIO_FILE"

# Optional: Print confirmation (will show in hook output)
echo "📚 Source tracked for bibliography: $URL"

exit 0
