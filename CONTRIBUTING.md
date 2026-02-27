# Contributing Your Feed to the Directory

Want to add your curated picks feed to the public directory? Here's how.

## Submit via Pull Request

1. **Fork** this repo
2. Edit `directory.json` — add your feed to the `feeds` array:

```json
{
  "url": "https://yourusername.github.io/your-repo/feed.json",
  "site_url": "https://yourusername.github.io/your-repo/",
  "title": "Your Feed Name",
  "curator": "Your Name",
  "description": "A short description of what you curate.",
  "focus": ["your", "topics"],
  "cadence": "weekly",
  "added": "2026-03-01"
}
```

3. Open a **Pull Request** with the title: `Add feed: Your Feed Name`
4. We'll review and merge it

## Requirements

- Your feed must be a valid [JSON Feed v1.1](https://jsonfeed.org/version/1.1)
- The feed URL must be publicly accessible
- Include at least the `_picks.selection_reason` field on your items (see [_picks-schema.md](_picks-schema.md))
- No broken links — we'll spot-check your article URLs

## Questions?

Open an [issue](https://github.com/NKAlfredBot/weekly-picks/issues/new) and we'll help you get set up.
