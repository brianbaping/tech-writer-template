#!/bin/bash
# Word Count Tracker Hook
# Tracks word counts in markdown files and provides progress indicators
# Runs after Write tool to show writing progress

# Parse tool parameters
FILE_PATH=$(echo "$TOOL_PARAMS" | jq -r '.file_path // empty')
CONTENT=$(echo "$TOOL_PARAMS" | jq -r '.content // empty')

# Only process markdown files
if [[ ! "$FILE_PATH" =~ \.md$ ]]; then
  exit 0
fi

# Skip meta files (CLAUDE.md, README.md, etc.)
FILENAME=$(basename "$FILE_PATH")
if [[ "$FILENAME" =~ ^(README|SETUP|HOW-TO-USE|CLAUDE|LICENSE)\.md$ ]]; then
  exit 0
fi

# Count words in the content (excluding front matter, code blocks, and markdown syntax)
word_count=$(echo "$CONTENT" | \
  # Remove YAML front matter
  sed '/^---$/,/^---$/d' | \
  # Remove code blocks
  sed '/^```/,/^```$/d' | \
  # Remove inline code
  sed 's/`[^`]*`//g' | \
  # Remove markdown links [text](url)
  sed 's/\[([^]]*)\]([^)]*)/\1/g' | \
  # Remove markdown images ![alt](url)
  sed 's/!\[[^]]*\]([^)]*)//g' | \
  # Remove headings markers
  sed 's/^#\+\s\+//g' | \
  # Remove bold/italic markers
  sed 's/[*_]\+//g' | \
  # Remove list markers
  sed 's/^[*+-]\s\+//g' | \
  sed 's/^[0-9]\+\.\s\+//g' | \
  # Count words
  wc -w | tr -d ' ')

# Count sections (headings)
section_count=$(echo "$CONTENT" | grep -c "^#" || echo "0")

# Get file size
file_size=$(echo "$CONTENT" | wc -c | tr -d ' ')
file_size_kb=$((file_size / 1024))

# Store word count for tracking changes
CACHE_DIR=".claude/cache"
CACHE_FILE="$CACHE_DIR/wordcount-$(echo "$FILE_PATH" | md5sum | cut -d' ' -f1).txt"

# Read previous word count if exists
previous_count=0
if [[ -f "$CACHE_FILE" ]]; then
  previous_count=$(cat "$CACHE_FILE")
fi

# Calculate change
word_diff=$((word_count - previous_count))

# Save current count
mkdir -p "$CACHE_DIR"
echo "$word_count" > "$CACHE_FILE"

# Determine document type and progress
doc_type="Document"
target_words=5000
progress_desc=""

# Estimate document type based on word count
if [[ $word_count -lt 1000 ]]; then
  doc_type="Blog post / Short article"
  target_words=1000
elif [[ $word_count -lt 3000 ]]; then
  doc_type="Technical article"
  target_words=3000
elif [[ $word_count -lt 8000 ]]; then
  doc_type="White paper"
  target_words=8000
elif [[ $word_count -lt 15000 ]]; then
  doc_type="Comprehensive white paper"
  target_words=15000
else
  doc_type="Research paper / Book chapter"
  target_words=20000
fi

# Calculate progress percentage
progress=$((word_count * 100 / target_words))
if [[ $progress -gt 100 ]]; then
  progress=100
fi

# Create progress bar
bar_length=20
filled=$((progress * bar_length / 100))
empty=$((bar_length - filled))
bar=$(printf '█%.0s' $(seq 1 $filled))$(printf '░%.0s' $(seq 1 $empty))

# Reading time estimate (average 200 words per minute)
reading_minutes=$((word_count / 200))
if [[ $reading_minutes -eq 0 ]]; then
  reading_time="<1 min"
elif [[ $reading_minutes -lt 60 ]]; then
  reading_time="${reading_minutes} min"
else
  hours=$((reading_minutes / 60))
  mins=$((reading_minutes % 60))
  reading_time="${hours}h ${mins}m"
fi

# Generate output message
echo ""
echo "📊 Word Count Tracker"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 File: $(basename "$FILE_PATH")"
echo ""
echo "Word Count:    $word_count words"

if [[ $previous_count -gt 0 ]]; then
  if [[ $word_diff -gt 0 ]]; then
    echo "Change:        +$word_diff words ⬆"
  elif [[ $word_diff -lt 0 ]]; then
    echo "Change:        $word_diff words ⬇"
  else
    echo "Change:        No change"
  fi
fi

echo "Sections:      $section_count headings"
echo "File Size:     ${file_size_kb} KB"
echo "Reading Time:  ~${reading_time}"
echo ""
echo "Document Type: $doc_type"
echo "Progress:      [$bar] ${progress}% to ${target_words} words"
echo ""

# Show milestones
if [[ $word_count -ge 1000 && $previous_count -lt 1000 ]]; then
  echo "🎉 Milestone: 1,000 words!"
elif [[ $word_count -ge 3000 && $previous_count -lt 3000 ]]; then
  echo "🎉 Milestone: 3,000 words!"
elif [[ $word_count -ge 5000 && $previous_count -lt 5000 ]]; then
  echo "🎉 Milestone: 5,000 words!"
elif [[ $word_count -ge 8000 && $previous_count -lt 8000 ]]; then
  echo "🎉 Milestone: 8,000 words! (Typical white paper length)"
elif [[ $word_count -ge 10000 && $previous_count -lt 10000 ]]; then
  echo "🎉 Milestone: 10,000 words!"
elif [[ $word_count -ge 15000 && $previous_count -lt 15000 ]]; then
  echo "🎉 Milestone: 15,000 words!"
fi

# Section-level word counts (if document has sections)
if [[ $section_count -gt 1 ]]; then
  echo "Section Breakdown:"
  echo ""

  # Parse sections and count words in each
  section_num=0
  current_section=""
  section_content=""

  while IFS= read -r line; do
    if [[ "$line" =~ ^#[[:space:]] ]]; then
      # New section found
      if [[ -n "$current_section" ]]; then
        # Count words in previous section
        section_words=$(echo "$section_content" | \
          sed '/^```/,/^```$/d' | \
          sed 's/`[^`]*`//g' | \
          wc -w | tr -d ' ')

        section_title=$(echo "$current_section" | sed 's/^#\+\s\+//')
        if [[ ${#section_title} -gt 50 ]]; then
          section_title="${section_title:0:47}..."
        fi

        printf "  %-50s %6s words\n" "$section_title" "$section_words"
      fi

      # Start new section
      current_section="$line"
      section_content=""
    else
      section_content+="$line"$'\n'
    fi
  done <<< "$CONTENT"

  # Handle last section
  if [[ -n "$current_section" ]]; then
    section_words=$(echo "$section_content" | \
      sed '/^```/,/^```$/d' | \
      sed 's/`[^`]*`//g' | \
      wc -w | tr -d ' ')

    section_title=$(echo "$current_section" | sed 's/^#\+\s\+//')
    if [[ ${#section_title} -gt 50 ]]; then
      section_title="${section_title:0:47}..."
    fi

    printf "  %-50s %6s words\n" "$section_title" "$section_words"
  fi

  echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Always exit 0 (informational only, never block)
exit 0
