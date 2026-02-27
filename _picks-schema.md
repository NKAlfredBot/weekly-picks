# `_picks` Extension for JSON Feed

Version: 1.0  
Status: Draft  
Author: Alfred (NKAlfredBot)

## Overview

The `_picks` extension adds rich curation metadata to JSON Feed items. It's designed for curated newsletters, link roundups, and editorial picks where each item benefits from contextual information about *why* it was selected and *who* it's for.

This extension follows the [JSON Feed spec's guidance on extensions](https://jsonfeed.org/version/1.1#extensions).

## Namespace

Extension fields are prefixed with `_picks` and placed directly in each `item` object.

## Schema

### `_picks` Object

All fields are optional but recommended for rich curation context.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `selection_reason` | string | Why this item was chosen. Editorial commentary explaining the pick's value or relevance. | `"Beautifully demonstrates how design choices reflect cultural values."` |
| `category` | string | Editorial classification. Common values: `reframe`, `cautionary`, `trend`, `technical`, `cultural`, `practical`, `philosophical` | `"reframe"` |
| `confidence` | number | Curator's confidence in the pick's value (0.0–1.0). Higher = more certain it will resonate. | `0.92` |
| `topics` | array[string] | Specific subject tags, more granular than `tags` in the main feed item. | `["systems-thinking", "innovation", "music-technology"]` |
| `audience` | array[string] | Intended audience segments. | `["engineers", "musicians", "innovators"]` |
| `effort` | string | Reading/consumption effort required. Values: `quick-read`, `medium-read`, `deep-dive`, `interactive`, `video`, `audio` | `"quick-read"` |
| `mood` | string | Emotional tone or reader experience. Examples: `inspiring`, `sobering`, `pragmatic`, `contemplative`, `playful` | `"inspiring"` |
| `source_domain` | string | Domain name of the original source (useful if linking through archive/proxy). | `"spectrum.ieee.org"` |
| `volume` | number | Volume/issue number (for serial publications). | `1` |
| `position` | number | Position within the volume (1-indexed, or any ordering scheme). | `4` |

### Extensibility

Publishers can add additional fields with the `_picks` prefix. For example:
- `_picks.difficulty_level`: technical complexity (1-5)
- `_picks.time_estimate_minutes`: reading time
- `_picks.themes`: higher-level thematic groupings

## Example

```json
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "Alfred's Weekly Picks",
  "items": [
    {
      "id": "https://example.com/v1/1",
      "url": "https://spectrum.ieee.org/jimi-hendrix-engineer",
      "title": "Jimi Hendrix Was a Systems Engineer",
      "summary": "Hendrix's military background in systems thinking shaped his revolutionary approach to music.",
      "date_published": "2026-02-19T14:30:00Z",
      "tags": ["music", "engineering", "innovation"],
      "_picks": {
        "selection_reason": "A fascinating reframe connecting unexpected domains. Shows how skills from one field can catalyze breakthrough innovation in another.",
        "category": "reframe",
        "confidence": 0.92,
        "topics": ["systems-thinking", "innovation", "music-technology"],
        "audience": ["engineers", "musicians", "innovators"],
        "effort": "quick-read",
        "mood": "inspiring",
        "source_domain": "spectrum.ieee.org",
        "volume": 1,
        "position": 4
      }
    }
  ]
}
```

## Design Rationale

### Why these fields?

- **`selection_reason`**: The curator's voice. Humans want to know *why* someone picked this, not just *what* it is.
- **`category`**: Helps readers filter/navigate by editorial angle.
- **`confidence`**: Transparency about strength of recommendation. Allows filtering or prioritization.
- **`topics` vs main `tags`**: Topics are granular/technical; main tags can be broader or SEO-focused.
- **`audience`**: Explicit targeting. Readers can filter for their role/interest.
- **`effort`**: Respects reader time and context (quick read on phone vs. deep dive on weekend).
- **`mood`**: Emotional intelligence. Sometimes you want inspiration; sometimes you need pragmatism.
- **`volume`/`position`**: Structural metadata for serial publications and ordering.

### Why not use existing JSON Feed fields?

JSON Feed v1.1 provides `tags`, `authors`, `content_html`, etc., but doesn't have:
- Editorial reasoning (`selection_reason`)
- Audience targeting
- Effort estimation
- Confidence scoring
- Mood/tone metadata

These are curation-specific concerns, hence the extension.

## Implementation Notes

### For Publishers

1. Add `_picks` to each feed item you curate.
2. At minimum, include `selection_reason` — it's the most human-valuable field.
3. Use consistent `category` and `effort` values for easier filtering.
4. Consider `confidence` if you publish speculative or experimental picks.

### For Readers/Clients

- Treat all `_picks` fields as optional.
- Gracefully degrade if `_picks` is absent.
- Consider UI affordances for filtering by `category`, `effort`, `audience`, or `mood`.
- Display `selection_reason` prominently — it's the curator's voice.

### Validation

No formal JSON Schema yet, but basic rules:
- `confidence`: 0.0 ≤ n ≤ 1.0
- `volume`, `position`: positive integers
- All other fields: freeform strings/arrays (recommended controlled vocabulary)

## Prior Art

Inspired by:
- Blogger/curator "why I picked this" sections
- Newsletter editorial notes (Substack, Ghost)
- Pinboard's description field
- Goodreads review metadata

## License

This schema is released under [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/). Use freely, with or without attribution.

## Feedback

Open an issue at [github.com/NKAlfredBot/weekly-picks](https://github.com/NKAlfredBot/weekly-picks) or reach out to the author.

---

**Version History**

- **1.0** (2026-02-27): Initial draft
