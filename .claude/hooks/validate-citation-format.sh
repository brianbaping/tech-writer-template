#!/bin/bash
# Citation Format Validation Hook
# Runs before Write operations to validate citation formatting

# Get the file content from the tool parameters
# In PreToolUse hooks, $TOOL_PARAMS contains the JSON of the tool call

# Extract file path and content
FILE_PATH=$(echo "$TOOL_PARAMS" | jq -r '.file_path // empty')
CONTENT=$(echo "$TOOL_PARAMS" | jq -r '.content // empty')

# Only validate if writing to markdown files or main white paper files
if [[ ! "$FILE_PATH" =~ \.(md|txt)$ ]] && [[ ! "$FILE_PATH" =~ whitepaper ]] && [[ ! "$FILE_PATH" =~ white-paper ]]; then
  # Not a document file, skip validation
  exit 0
fi

# Check for common citation format issues
ISSUES=()

# Check for placeholder citations that shouldn't be in final draft
if echo "$CONTENT" | grep -q '\[SOURCE-[0-9X]\]'; then
  ISSUES+=("Found placeholder citations like [SOURCE-X] - these should be replaced with proper citations")
fi

if echo "$CONTENT" | grep -q '\[CITATION NEEDED'; then
  ISSUES+=("Found [CITATION NEEDED] markers - citations are missing")
fi

if echo "$CONTENT" | grep -q '\[TODO:.*cit'; then
  ISSUES+=("Found TODO markers related to citations")
fi

# Check for malformed IEEE citations (common errors)
if echo "$CONTENT" | grep -Eq '\[[0-9]+\]\.' && echo "$CONTENT" | grep -Eq '\[.*\]\.'; then
  # Citations should come before the period, not after
  ISSUES+=("Warning: Some citations appear after periods. IEEE style places citations before periods: 'text [1].' not 'text. [1]'")
fi

# Check for missing space before citation
if echo "$CONTENT" | grep -Eq '[a-zA-Z]\[[0-9]+\]' && ! echo "$CONTENT" | grep -q 'http'; then
  ISSUES+=("Warning: Some citations may be missing space before bracket: 'text [1]' not 'text[1]'")
fi

# If there are issues, print them as warnings (not blocking)
if [ ${#ISSUES[@]} -gt 0 ]; then
  echo "⚠️  Citation Format Warnings:"
  for issue in "${ISSUES[@]}"; do
    echo "  - $issue"
  done
  echo ""
  echo "These are warnings, not errors. The write will proceed."
  echo "Consider running the citation-validator agent to check all citations."
fi

# Always exit 0 (allow the write) - this is a warning system, not blocking
# To make it blocking, change to: exit 1 when issues found
exit 0
