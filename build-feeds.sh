#!/bin/bash
# Build filtered feeds from the main feed.json

set -e

FEED_FILE="feed.json"
LONGFORM_FILE="feed-longform.json"
MULTIMEDIA_FILE="feed-multimedia.json"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed. Install with: brew install jq"
    exit 1
fi

# Check if feed.json exists
if [ ! -f "$FEED_FILE" ]; then
    echo "Error: $FEED_FILE not found"
    exit 1
fi

echo "📚 Building filtered feeds from $FEED_FILE..."

# Generate Long Form feed (media_type == "article")
echo "  → Creating $LONGFORM_FILE (articles only)..."
jq '{
  version,
  title: "Alfred'\''s Weekly Picks — Long Form",
  home_page_url,
  feed_url: (.feed_url | sub("feed.json"; "feed-longform.json")),
  description: "Long-form articles from Alfred'\''s Weekly Picks — thought-provoking reads across technology, culture, and innovation.",
  icon,
  authors,
  language,
  items: [.items[] | select(._picks.media_type == "article")]
}' "$FEED_FILE" > "$LONGFORM_FILE"

LONGFORM_COUNT=$(jq '.items | length' "$LONGFORM_FILE")
echo "    ✓ $LONGFORM_COUNT long-form items"

# Generate Multimedia feed (media_type != "article")
echo "  → Creating $MULTIMEDIA_FILE (multimedia only)..."
jq '{
  version,
  title: "Alfred'\''s Weekly Picks — Multimedia",
  home_page_url,
  feed_url: (.feed_url | sub("feed.json"; "feed-multimedia.json")),
  description: "Multimedia picks from Alfred'\''s Weekly Picks — music, film, video, interactives, and more.",
  icon,
  authors,
  language,
  items: [.items[] | select(._picks.media_type != "article")]
}' "$FEED_FILE" > "$MULTIMEDIA_FILE"

MULTIMEDIA_COUNT=$(jq '.items | length' "$MULTIMEDIA_FILE")
echo "    ✓ $MULTIMEDIA_COUNT multimedia items"

TOTAL_COUNT=$(jq '.items | length' "$FEED_FILE")
echo ""
echo "✅ Done! Generated filtered feeds:"
echo "   • $FEED_FILE: $TOTAL_COUNT total items"
echo "   • $LONGFORM_FILE: $LONGFORM_COUNT articles"
echo "   • $MULTIMEDIA_FILE: $MULTIMEDIA_COUNT multimedia"
