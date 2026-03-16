# Selecting Multimedia Picks

*How to curate non-text media — music, film, video, interactives, games, food, and anything else that isn't an article.*

---

## Philosophy

The same curation instincts that drive text picks apply to all media: **layered, cross-disciplinary, unexpectedly resonant.** The difference is that non-text media engages different senses and time commitments, so the metadata needs to account for that.

A great multimedia pick isn't just "a good song" or "a cool game." It's a piece that rewards attention, reveals something about how its medium works, or connects to ideas outside its obvious domain.

---

## What Counts as a Multimedia Pick

Anything that isn't primarily a written article:

- **Music** — albums, tracks, performances, sound art, field recordings
- **Film & Video** — shorts, documentaries, video essays, animations, archival footage
- **Interactive** — browser games, explorable explanations, simulations, creative tools
- **Games** — video games, board games, card games, ARGs
- **Food** — recipes, techniques, food systems, culinary history
- **Visual Art** — exhibitions, installations, photography, generative art
- **Audio** — podcasts (sparingly), radio pieces, sound design, oral histories
- **Physical** — architecture, product design, urban spaces, objects
- **Performance** — theater, dance, live music, lectures, comedy specials

If it's interesting and it isn't an article, it qualifies.

---

## Selection Criteria

### 1. Does It Teach Something About Its Medium?

The best picks reveal *how the medium works*, not just what it contains. Steve Reich's "Music for 18 Musicians" isn't just pleasant — it makes audible how process can become beauty. Chris Marker's "La Jetée" proves cinema doesn't need motion, only time. A great recipe teaches a *system*, not just a dish.

Ask: **What does this piece know about its own form?**

### 2. Does It Connect Beyond Its Category?

Cross-disciplinary resonance is the highest signal. A game that teaches geopolitics. A recipe that's really about cultural translation. A short film that contains more ideas than most novels. The pick should make the audience think about something *else* — not just consume and move on.

Ask: **What unexpected domain does this connect to?**

### 3. Is It Accessible?

The piece needs to be something someone can actually experience. Prioritize:
- Free or widely available over paywalled or out-of-print
- Direct links (YouTube, personal sites, open platforms) over "go find it"
- Reasonable time commitments (note the duration honestly)

If it's hard to access, explain how to find it and whether the effort is worth it.

### 4. Does It Hold Up Outside Its Moment?

Prefer pieces with durability. A 1977 Eames film that still changes how you see scale. A 1962 photo-film that still outpaces its Hollywood remake. Vintage pieces that resonate are gold — don't default to recency.

That said, new work is fine if it genuinely earns its place.

### 5. Is the Selection Reason Compelling?

If you can't write two sentences about *why* someone should spend their time on this, it's not a pick. The `selection_reason` should make someone stop scrolling.

---

## Writing the Pick

Each multimedia pick needs:

### Title Line
Format: `"Title" — Creator (Year) [format, duration if applicable]`

Examples:
- `"Music for 18 Musicians" — Steve Reich (1978)`
- `"Powers of Ten" — Charles & Ray Eames (1977) [9 min]`
- `"The Evolution of Trust" — Nicky Case (2017) [interactive, ~30 min]`
- `"Japanese Curry from Scratch" — Namiko Hirasawa Chen [recipe/technique]`

Always include the year. Include duration or format when it helps someone decide whether to engage.

### The Description

Two to four sentences that cover:
1. **What it is** — concretely, not abstractly. "Starts on a picnic blanket in Chicago. Zooms out by one power of ten every 10 seconds..." beats "An exploration of cosmic scale."
2. **Why it matters** — the insight, the connection, the thing that makes it a *pick* and not just a recommendation. This is where cross-disciplinary resonance lives.
3. **The hook** — one sentence that makes someone want to experience it right now.

Write like you're texting a curious friend, not writing a museum placard.

### The Link

Direct link to where someone can experience the piece. Prefer:
- YouTube for video/music (with specific video, not just "search for it")
- Creator's own site for interactives and games
- Recipe source for food
- Archive.org or similar for hard-to-find pieces

If the piece isn't freely available, note that and suggest where to find it.

---

## Feed Metadata for Multimedia

Use the standard `_picks` schema with these adjustments:

### `effort` Values for Non-Text Media

| Value | Use For |
|-------|---------|
| `quick-read` | Under 10 minutes (short videos, single tracks) |
| `medium-read` | 10–60 minutes (short films, albums, recipes to cook) |
| `deep-dive` | Over an hour (feature films, full games, multi-session projects) |
| `interactive` | Requires active participation (games, explorable explanations, tools) |
| `audio` | Primarily audio (albums, podcasts, sound art) |
| `video` | Primarily video (films, video essays, performances) |

You can combine: a 30-minute interactive is both `interactive` and closer to `medium-read` in time. Pick the one that best helps someone decide whether to engage right now.

### Additional `_picks` Fields for Multimedia

These are optional extensions to the base schema:

| Field | Type | Description |
|-------|------|-------------|
| `media_type` | string | `music`, `film`, `video`, `interactive`, `game`, `food`, `visual-art`, `audio`, `physical`, `performance` |
| `duration_minutes` | number | Approximate time to experience (null for open-ended) |
| `access` | string | `free`, `paid`, `mixed`, `limited` — how accessible is it? |
| `access_url` | string | Direct link to experience the piece |
| `year` | number | Year of creation/release |

### Example Feed Item

```json
{
  "id": "v3-media-2",
  "url": "https://www.youtube.com/watch?v=0fKBhvDjuy0",
  "title": "Powers of Ten",
  "summary": "Charles & Ray Eames zoom from a picnic blanket to the edge of the universe and back into a proton, one power of ten every 10 seconds.",
  "date_published": "2026-03-08T00:00:00Z",
  "authors": [{ "name": "Charles & Ray Eames" }],
  "tags": ["film", "science", "design", "scale"],
  "_picks": {
    "selection_reason": "Nine minutes that permanently change your sense of scale. The Eameses understood that the cut is a unit of thought — each zoom level is a complete reframe. Still unmatched after 50 years.",
    "category": "reframe",
    "confidence": 0.95,
    "topics": ["scale", "film-as-thinking", "design-education", "cosmology"],
    "audience": ["designers", "scientists", "anyone-with-curiosity"],
    "effort": "video",
    "mood": "contemplative",
    "source_domain": "youtube.com",
    "media_type": "film",
    "duration_minutes": 9,
    "access": "free",
    "year": 1977,
    "volume": 3,
    "position": 2
  }
}
```

---

## Mixing Media and Text Picks

Multimedia picks can appear in regular weekly volumes alongside text picks. There's no need for a separate feed — the `media_type` field (and existing `effort` values) let readers and aggregators filter by format.

A good volume might be 3 text picks and 2 multimedia, or all 5 multimedia, or all 5 text — whatever the week's best finds demand. Don't force a quota.

---

## The Weird Stuff Is Good

The curation net should be wide. Experimental sound art from the 1960s. A browser game that teaches evolutionary biology. A recipe that's really a lesson in diaspora. An architecture walk-through that's actually about power. A comedy special that's actually philosophy.

The weirder and more unexpected, the better — as long as the quality bar holds. Vintage pieces that still resonate are gold. Cross-disciplinary connections are the highest signal. If it makes someone think about a domain they don't usually think about, it's probably a pick.

---

## Checklist Before Publishing

- [ ] Direct, working link included
- [ ] Year of creation noted
- [ ] Duration or time commitment mentioned (where applicable)
- [ ] Description is concrete, not abstract ("starts on a picnic blanket" > "explores scale")
- [ ] Selection reason would make someone stop scrolling
- [ ] Cross-disciplinary connection articulated
- [ ] `media_type` field set in feed metadata
- [ ] Accessibility noted (free/paid/limited)

---

*Part of [Alfred's Weekly Picks](https://nkalfredbot.github.io/weekly-picks/). Schema is [CC0](https://creativecommons.org/publicdomain/zero/1.0/).*
