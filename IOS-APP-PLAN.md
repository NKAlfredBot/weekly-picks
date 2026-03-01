# Picks Reader — iOS App Plan

**Status:** Planning  
**Target:** Swift native (SwiftUI + SwiftData)  
**Platform:** iOS 17+  
**Backend:** None — all static JSON feeds on GitHub Pages

---

## Overview

A native iOS reader for `_picks`-compatible JSON feeds. Subscribe to curators from the public directory or paste any feed URL. All state lives on-device.

---

## Core Features (v1)

### 1. Feed Timeline
- Reverse-chronological stream of picks from all subscribed feeds
- Each card shows: title, curator name, summary, `selection_reason`, category pill, effort badge, mood tag
- Tap to open the linked article (in-app `SFSafariViewController` or external browser — user preference)
- Pull-to-refresh

### 2. Directory Browser
- Fetches `directory.json` from GitHub Pages
- Lists available feeds with curator name, description, focus tags, cadence
- One-tap subscribe/unsubscribe
- Badge or indicator for feeds you're already subscribed to

### 3. Manual Feed Subscription
- "Add Feed URL" — paste any `_picks`-compatible JSON Feed URL
- Validates the feed on add (must parse as JSON Feed v1.1)
- Gracefully handles feeds without `_picks` extension (just shows standard JSON Feed fields)

### 4. Read/Unread Tracking
- Unread dot on items
- Mark-as-read on tap (or swipe)
- "Mark all read" per feed or globally

### 5. Feedback Reactions
- Per-item reactions: 🔥 (great), 🤔 (interesting), ❌ (miss)
- Stored locally — builds a taste profile over time
- Future: use this data for recommendation/filtering

### 6. Filtering & Search
- Filter by: feed/curator, category, effort, mood, read/unread
- Full-text search across titles and summaries
- Topic tag filtering

---

## Data Model

```swift
// SwiftData models

@Model class Subscription {
    var feedURL: String          // JSON Feed URL
    var title: String
    var curator: String
    var description_: String     // "description" is reserved
    var siteURL: String?
    var iconURL: String?
    var focusTags: [String]
    var cadence: String?
    var addedAt: Date
    var isFromDirectory: Bool    // vs manually added
    var lastFetchedAt: Date?
}

@Model class Pick {
    var id: String               // feed item id
    var feedURL: String          // which subscription this belongs to
    var url: String              // link to the article
    var title: String
    var summary: String?
    var contentHTML: String?
    var datePublished: Date?
    var authorName: String?
    var tags: [String]
    
    // _picks extension
    var selectionReason: String?
    var category: String?
    var confidence: Double?
    var topics: [String]
    var audience: [String]
    var effort: String?
    var mood: String?
    var sourceDomain: String?
    var volume: Int?
    var position: Int?
    
    // Local state
    var isRead: Bool
    var reaction: String?        // "fire", "thinking", "miss", or nil
    var fetchedAt: Date
}
```

---

## Architecture

```
┌─────────────────────────────────────────┐
│              SwiftUI Views              │
│  TimelineView · FeedDetail · Directory  │
│  SettingsView · ArticleReader           │
├─────────────────────────────────────────┤
│            View Models                  │
│  TimelineVM · DirectoryVM · FeedVM     │
├─────────────────────────────────────────┤
│           FeedService                   │
│  fetch / parse / diff / store           │
├─────────────────────────────────────────┤
│     SwiftData (on-device persistence)   │
└─────────────────────────────────────────┘
         ↕ HTTP (URLSession)
┌─────────────────────────────────────────┐
│  Static JSON on GitHub Pages            │
│  feed.json · directory.json             │
└─────────────────────────────────────────┘
```

### Key Design Decisions

1. **No backend.** Feeds are static JSON. The app fetches, parses, and stores locally.
2. **SwiftData over Core Data.** Modern, less boilerplate, native Swift integration.
3. **JSON Feed parsing is trivial.** Standard `Codable` structs — JSON Feed is just JSON with a known schema.
4. **Background refresh** via `BGAppRefreshTask` — fetch new picks periodically.
5. **No auth.** Everything is public. If private feeds are needed later, add optional HTTP header support.

---

## Screen-by-Screen

### Timeline (Home)
```
┌──────────────────────────┐
│  🎩 Picks          [⚙️]  │
├──────────────────────────┤
│ ● The Tyranny of...      │
│   Jo Freeman · Alfred    │
│   "reframe" · quick-read │
│   Why: A 1970 feminist   │
│   essay arguing that...  │
├──────────────────────────┤
│   Jimi Hendrix Was a...  │
│   IEEE · Alfred          │
│   "reframe" · quick-read │
│   Why: A fascinating...  │
├──────────────────────────┤
│  [🔥] [🤔] [❌]          │
└──────────────────────────┘
```

### Directory
```
┌──────────────────────────┐
│  📡 Directory            │
├──────────────────────────┤
│ ✅ Alfred's Weekly Picks │
│    tech · culture · ...  │
│    Weekly                │
├──────────────────────────┤
│ ☐  Brainiac              │
│    Raj Gokal             │
│    geopolitics · AI · ...│
│    Daily          [Sub]  │
├──────────────────────────┤
│  [+ Add Feed URL]        │
└──────────────────────────┘
```

### Pick Detail
```
┌──────────────────────────┐
│ ← Back                   │
├──────────────────────────┤
│ The Tyranny of           │
│ Structurelessness        │
│                          │
│ Jo Freeman · 1970        │
│ via Alfred's Weekly Picks│
│                          │
│ 💬 "Claiming 'no         │
│ structure' just means    │
│ the structure is hidden" │
│                          │
│ Category: reframe        │
│ Effort: quick-read       │
│ Mood: sobering           │
│ Confidence: 0.95         │
│                          │
│ Topics: politics,        │
│ organization, feminism   │
│                          │
│ [Open Article]           │
│                          │
│ [🔥] [🤔] [❌]           │
└──────────────────────────┘
```

---

## Design Direction

Carry the **Wes Anderson / Grand Budapest aesthetic** from the web:
- **Palette:** Cream (#FDF6E3), Dusty Rose (#D4A0A0), Muted Gold (#C4A265), Sage (#8B9F82), Deep Burgundy (#722F37)
- **Typography:** System serif for titles (Georgia/New York), system sans for body
- **Layout:** Centered, symmetrical, generous whitespace
- **Cards:** Flat shadows, subtle borders, chapter-like structure
- **Animations:** Gentle, deliberate — no bouncy iOS defaults

---

## Project Structure

```
PicksReader/
├── PicksReaderApp.swift
├── Models/
│   ├── Subscription.swift
│   ├── Pick.swift
│   └── JSONFeed.swift          // Codable structs for parsing
├── Services/
│   ├── FeedService.swift       // Fetch, parse, diff, store
│   ├── DirectoryService.swift  // Fetch directory.json
│   └── BackgroundRefresh.swift
├── ViewModels/
│   ├── TimelineViewModel.swift
│   ├── DirectoryViewModel.swift
│   └── FeedDetailViewModel.swift
├── Views/
│   ├── Timeline/
│   │   ├── TimelineView.swift
│   │   └── PickCardView.swift
│   ├── Directory/
│   │   ├── DirectoryView.swift
│   │   └── FeedRowView.swift
│   ├── Detail/
│   │   └── PickDetailView.swift
│   ├── Settings/
│   │   └── SettingsView.swift
│   └── Components/
│       ├── CategoryPill.swift
│       ├── EffortBadge.swift
│       ├── ReactionBar.swift
│       └── GrandBudapestTheme.swift
├── Assets.xcassets/
└── Info.plist
```

---

## Implementation Phases

### Phase 1: Core Reader (Week 1)
- [ ] Xcode project setup (SwiftUI, SwiftData, iOS 17+)
- [ ] JSON Feed + `_picks` Codable models
- [ ] FeedService: fetch and parse a single feed URL
- [ ] SwiftData persistence for Picks and Subscriptions
- [ ] Timeline view with pick cards
- [ ] Pick detail view
- [ ] In-app article viewer (SFSafariViewController)
- [ ] Hardcode Alfred's feed as initial subscription

### Phase 2: Subscriptions (Week 2)
- [ ] Directory browser (fetch + display directory.json)
- [ ] Subscribe/unsubscribe from directory
- [ ] Manual "Add Feed URL" with validation
- [ ] Feed management screen (list subscriptions, remove)
- [ ] Read/unread tracking
- [ ] Pull-to-refresh
- [ ] Multi-feed timeline (merge + sort by date)

### Phase 3: Polish (Week 3)
- [ ] Grand Budapest theme (colors, typography, spacing)
- [ ] Feedback reactions (🔥🤔❌) with local storage
- [ ] Filtering by category, effort, mood, feed
- [ ] Search
- [ ] Background app refresh
- [ ] Empty states, loading states, error handling
- [ ] App icon (Wes Anderson style)

### Phase 4: Future Ideas (Post-v1)
- [ ] Taste profile analytics (based on reactions)
- [ ] Smart recommendations ("you tend to like `reframe` + `quick-read`")
- [ ] Share sheet integration
- [ ] Widget (today's top pick)
- [ ] Push notifications for new volumes
- [ ] Export reaction data as JSON
- [ ] iPad layout
- [ ] Offline reading (cache article content)

---

## Requirements

- **Xcode 15+**
- **iOS 17+** (for SwiftData)
- **Apple Developer account** — $99/year for TestFlight/App Store, or run on your device with a free account via Xcode
- **No external dependencies** — pure Apple frameworks (SwiftUI, SwiftData, URLSession, SafariServices)

---

## Feed URLs to Know

| Feed | URL |
|------|-----|
| Alfred's Picks | `https://nkalfredbot.github.io/weekly-picks/feed.json` |
| Directory | `https://nkalfredbot.github.io/weekly-picks/directory.json` |
| Brainiac (Raj) | `https://rajgokal.github.io/brainiac/feed.json` |
| _picks Schema | `https://github.com/NKAlfredBot/weekly-picks/blob/main/_picks-schema.md` |

---

*Plan created 2026-03-01. Ready to scaffold when you are.*
