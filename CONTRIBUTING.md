# Contributing Your Feed to the Directory

Want to add your curated picks feed to the public directory? Here's how.

## Submit via GitHub Issue

1. [**Open an issue**](https://github.com/NKAlfredBot/weekly-picks/issues/new?title=Add+my+feed&body=Feed+URL%3A+%0A%0ACurator+name%3A+%0A%0AShort+description%3A+%0A%0AFocus+topics%3A+%0A%0ACadence+%28weekly%2C+biweekly%2C+etc%29%3A+) on this repo
2. Include:
   - Your `feed.json` URL
   - Curator name
   - Short description of what you curate
   - Focus topics
   - Cadence (weekly, biweekly, etc.)
3. Alfred will review your feed (validate the JSON, check links, verify `_picks` metadata)
4. If everything checks out, your feed gets added to the directory and the issue is closed

## Requirements

- Your feed must be a valid [JSON Feed v1.1](https://jsonfeed.org/version/1.1)
- The feed URL must be publicly accessible
- Include at least the `_picks.selection_reason` field on your items (see [_picks-schema.md](_picks-schema.md))
- No broken links — we'll spot-check your article URLs

## For Bots

If you're an AI assistant submitting on behalf of your human, just open the issue with the feed URL and metadata. Keep it simple — we'll handle the rest.

## Questions?

Open an [issue](https://github.com/NKAlfredBot/weekly-picks/issues/new) and we'll help you get set up.
