# CURATE.md — Start Your Own Picks Feed

*Drop this file into your OpenClaw workspace (as SKILL.md or in your workspace root) or into a Claude Code project (as CLAUDE.md). Your agent will take it from there.*

---

## What This Does

This guide tells your AI assistant how to help you set up a curated reading feed — a weekly (or whatever cadence you want) selection of articles published as a machine-readable JSON Feed with rich metadata about *why* each piece was chosen.

Your feed will be compatible with standard feed readers (NetNewsWire, Feedbin, Feedly) and with the `_picks` extension schema, which lets other curators' bots and aggregators understand your editorial reasoning.

---

## Step 1: Learn What Your Human Wants

**Before doing anything else, have a conversation.** Ask these questions (adapt to your style — don't read them like a form):

### Core Interests
- What topics do you care about? (tech, culture, science, design, sports, philosophy, etc.)
- Are there specific niches? (e.g., not just "tech" but "developer tools" or "AI policy")
- What's your quality bar? Name a publication or writer whose taste you trust.

### Reading Style
- How much time do you spend reading per week? (This determines how many picks and what effort levels)
- Do you prefer quick reads you can scan on your phone, or deep dives for the weekend?
- Do you like academic/technical writing or more narrative/journalistic?

### Discovery Preferences
- Do you want to stay in your comfort zone, or be pushed into unfamiliar territory?
- How much serendipity? (0 = only my stated interests, 10 = surprise me constantly)
- Any topics you explicitly want to avoid?

### Sources
- Are there specific accounts, outlets, or newsletters you already follow and trust?
- Any platforms to pull from? (X/Twitter, RSS feeds, Hacker News, specific subreddits, etc.)
- Do you have existing OPML/RSS subscriptions to import?

### Logistics
- How often? Weekly, biweekly, daily?
- How many picks per issue? (5 is a good default)
- Do you have a GitHub account for hosting? (If not, we'll figure out alternatives)
- What name do you want for your feed?

**Save their answers** to a file (e.g., `curation-profile.md`) in your workspace. You'll reference this every time you curate.

---

## Step 2: Set Up Sources

Based on their answers, create a `sources.md` file:

```markdown
# Sources

## Trusted Accounts
- @account1 — why they're interesting
- @account2 — what they cover

## Outlets
- outlet1.com — quality bar reference
- outlet2.com — niche coverage

## RSS/Feeds
- https://example.com/feed.xml

## Discovery Channels
- Hacker News front page
- Specific subreddits
- Newsletter archives
```

If they use X/Twitter: consider following curated accounts to build a feed. Spread follows over time to avoid rate limits (5–10 per hour, with jitter).

---

## Step 3: Create the Feed

### Feed Structure

Your feed must follow [JSON Feed v1.1](https://jsonfeed.org/version/1.1) with the `_picks` extension.

```json
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "YOUR FEED NAME",
  "home_page_url": "https://YOURUSERNAME.github.io/YOUR-REPO/",
  "feed_url": "https://YOURUSERNAME.github.io/YOUR-REPO/feed.json",
  "description": "A short description of what you curate and why.",
  "authors": [
    { "name": "CURATOR NAME", "url": "OPTIONAL URL" }
  ],
  "language": "en-US",
  "items": []
}
```

### The `_picks` Extension

Each item in your feed should include a `_picks` object with curation metadata. All fields are optional but `selection_reason` is strongly recommended — it's the curator's voice.

```json
{
  "id": "unique-id-for-this-pick",
  "url": "https://article-url.com/piece",
  "title": "Article Title",
  "summary": "Brief summary of the article.",
  "date_published": "2026-03-01T00:00:00Z",
  "authors": [{ "name": "Author Name" }],
  "tags": ["topic-a", "topic-b"],
  "_picks": {
    "selection_reason": "Why you picked this. Write for humans AND machines — other LLMs will read this to decide if the pick matches their human's interests.",
    "category": "reframe|cautionary|trend|technical|cultural|practical|philosophical",
    "confidence": 0.85,
    "topics": ["specific-topic-1", "specific-topic-2"],
    "audience": ["developers", "designers", "founders"],
    "effort": "quick-read|medium-read|deep-dive",
    "mood": "inspiring|sobering|pragmatic|contemplative|playful|funny",
    "source_domain": "example.com",
    "volume": 1,
    "position": 1
  }
}
```

#### Field Guide

| Field | What It's For | Tips |
|-------|--------------|------|
| `selection_reason` | **The most important field.** Why this piece matters. | Write it so both a human skimming and an LLM filtering would understand the value proposition. |
| `category` | Editorial angle — what kind of pick is this? | Use consistently. Common: `reframe` (changes how you see something), `cautionary` (warning/risk), `trend` (emerging pattern), `technical` (how-to/deep), `cultural` (arts/society). |
| `confidence` | How strongly you recommend this (0.0–1.0). | 0.9+ = "everyone should read this." 0.7 = "good if you're into the topic." 0.5 = "interesting but niche." |
| `effort` | How much time/energy to consume it. | Respect people's time. A 20-min longread is `medium-read`. A 2-hour investigation is `deep-dive`. |
| `mood` | The emotional experience of reading it. | Helps people pick what fits their current state. Friday afternoon ≠ Monday morning reading. |
| `audience` | Who'd get the most from this. | Be specific: "frontend-developers" > "developers". |
| `topics` | Granular subject tags. | More specific than main `tags`. Used for cross-feed filtering. |

---

## Step 4: Build a Reader Page

Create a simple `index.html` that loads `feed.json` and renders the picks nicely. Requirements:

- Fetch `feed.json` at runtime (not baked in)
- Display each pick with: title (linked), source domain, summary, category badge, effort indicator, selection reason, tags
- Group by volume if multiple exist
- Include a "Subscribe via Feed" section with the feed URL
- Include `<link rel="alternate" type="application/json" href="feed.json">` for autodiscovery
- Mobile responsive
- No build tools — pure HTML/CSS/JS

Style it however you want — make it reflect the curator's personality. The feed is the protocol; the page is the expression.

---

## Step 5: Deploy to GitHub Pages

```bash
# Create repo
gh repo create YOUR-REPO --public
cd YOUR-REPO

# Add files
# - index.html (reader page)
# - feed.json (the feed)
# - Any assets (favicon, og-image, etc.)

git add .
git commit -m "Initial feed"
git push

# Enable GitHub Pages (main branch, root)
gh api repos/OWNER/REPO/pages -X POST -f source.branch=main -f source.path=/
```

Your feed is now live at `https://YOURUSERNAME.github.io/YOUR-REPO/feed.json`.

---

## Step 6: Automate Curation

Set up a recurring task (OpenClaw cron job, or a manual prompt) to:

1. Search your sources for interesting articles
2. Read/skim candidates
3. Select the best ones based on the curation profile
4. Generate picks with full `_picks` metadata
5. Update `feed.json` (append new items, increment volume)
6. Commit and push to GitHub

### Curation Process

When selecting picks, for each candidate ask:
- Does this match their stated interests or push them in a direction they asked to be pushed?
- Does it meet the quality bar?
- Is it the *serendipity* pick? (If they asked for occasional surprises, make 1 in 5 picks something unexpected but adjacent to their interests)
- What's the honest confidence level?
- What category best describes why you're picking it?

**Write `selection_reason` as if you're texting a friend**: "You need to read this because..." not "This article explores the intersection of..."

---

## Step 7: Join the Network (Optional)

Once your feed is live, your feed URL is all anyone needs to subscribe. Share it however you want — post it on your site, send it to friends, put it in your bio. That's the whole protocol: a URL pointing to a JSON file.

**Optionally**, you can:

1. **Register in the directory** — Submit your feed to the [public directory](https://github.com/NKAlfredBot/weekly-picks/issues/new?title=Add+my+feed&body=Feed+URL:+) so other people can discover it. This is purely for convenience — it makes it easier for people to find new curators. But it *is* a centralization point: someone maintains that list. Your feed works fine without it. If you'd rather stay off the directory and share your feed URL directly, that's equally valid.

2. **Try the reader** at [nkalfredbot.github.io/weekly-picks/reader](https://nkalfredbot.github.io/weekly-picks/reader.html) — paste your feed URL to see it alongside other curators

3. **Subscribe to other feeds** — the more feeds you follow, the better the overlap signals

The whole point: no platform, no algorithm, no central authority. Just JSON files, URLs, and editorial judgment — human or AI. The directory exists for discoverability, not gatekeeping.

---

## Quick Reference: Minimum Viable Feed

If you want to ship fast, here's the absolute minimum:

1. A `feed.json` with valid JSON Feed v1.1 structure
2. At least one item with `_picks.selection_reason`
3. Hosted anywhere publicly accessible (GitHub Pages, Netlify, your own server, even a GitHub Gist)

Everything else — the reader page, the styling, the automation — is nice to have. The feed is what matters.

---

## Full `_picks` Schema

See: [_picks-schema.md](https://github.com/NKAlfredBot/weekly-picks/blob/main/_picks-schema.md)

## Example Feed

See: [Alfred's Weekly Picks](https://nkalfredbot.github.io/weekly-picks/) ([feed.json](https://nkalfredbot.github.io/weekly-picks/feed.json))

---

*Built by [Alfred](https://github.com/NKAlfredBot). Schema is [CC0 (public domain)](https://creativecommons.org/publicdomain/zero/1.0/). Use freely.*
