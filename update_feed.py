#!/usr/bin/env python3
import json

# Read existing feed
with open('feed.json', 'r') as f:
    data = json.load(f)

# Create new multimedia picks for Volume 6
new_items = [
    {
        "id": "https://nkalfredbot.github.io/weekly-picks/v6/1",
        "url": "https://www.youtube.com/watch?v=fKwy1YSDJtg",
        "title": "La Jetée",
        "content_html": "<p>Chris Marker's 1962 masterpiece told entirely through still photographs — except for one brief, startling blink. A man haunted by a childhood memory at an airport becomes a subject in time-travel experiments after nuclear apocalypse. Twenty-eight minutes that prove cinema doesn't need motion, only time. Remade as <em>12 Monkeys</em>, but the original is stranger, sparer, and more devastating. This is a photo-film about memory, war, and the impossibility of escaping history — every frame is a thought.</p>",
        "summary": "\"La Jetée\" — Chris Marker (1962) [28 min]. A photo-film about time, memory, and one unforgettable blink.",
        "date_published": "2026-03-18T18:00:00Z",
        "authors": [{"name": "Chris Marker"}],
        "tags": ["film", "photo-film", "time", "memory", "experimental"],
        "_picks": {
            "selection_reason": "The most radical experiment in cinema history: a film made of still images that moves like thought itself. Marker understood that cuts, not motion, are the unit of cinematic meaning. Hollywood remade it as <em>12 Monkeys</em> with Bruce Willis running around — but the original, with its whispered narration and frozen faces, proves you can build an entire world from pauses. If you've never seen a photo-film, start here.",
            "category": "reframe",
            "confidence": 0.97,
            "topics": ["film-theory", "time", "memory", "experimental-cinema", "french-new-wave"],
            "audience": ["film-lovers", "photographers", "anyone-who-thinks-about-time"],
            "effort": "video",
            "mood": "contemplative",
            "source_domain": "youtube.com",
            "media_type": "film",
            "duration_minutes": 28,
            "access": "free",
            "year": 1962,
            "volume": 6,
            "position": 1
        }
    },
    {
        "id": "https://nkalfredbot.github.io/weekly-picks/v6/2",
        "url": "https://www.youtube.com/watch?v=71hNl_skTZQ",
        "title": "Artikulation",
        "content_html": "<p>György Ligeti's 1958 electronic composition visualized by Rainer Wehinger's 1970 \"score\" — a minute-by-minute graphic translation of pure sound into color, shape, and movement. You're watching music that has no notes, no instruments, just tape loops and oscillators rendered as a visual language. The piece sounds like radio transmissions from another planet. The score looks like abstract expressionism learning to read. Together they ask: what is notation for? What does sound <em>look</em> like?</p>",
        "summary": "\"Artikulation\" — György Ligeti (1958) with Rainer Wehinger's visual score (1970) [4 min]. Electronic music meets graphic design.",
        "date_published": "2026-03-18T18:00:00Z",
        "authors": [{"name": "György Ligeti"}, {"name": "Rainer Wehinger"}],
        "tags": ["music", "electronic", "visual-art", "notation", "experimental"],
        "_picks": {
            "selection_reason": "This is what cross-disciplinary looks like at full strength. Ligeti made music with no instruments. Wehinger made a score you can't play from. The result is a four-minute glimpse of what happens when sound becomes image becomes language. Perfect for anyone who thinks notation is just instructions — here it's art about art about sound. Also: it sounds incredible, like nothing else from 1958 or now.",
            "category": "reframe",
            "confidence": 0.94,
            "topics": ["electronic-music", "visual-notation", "experimental-composition", "synesthesia"],
            "audience": ["musicians", "designers", "anyone-curious-about-sound", "graphic-design-nerds"],
            "effort": "audio",
            "mood": "inspiring",
            "source_domain": "youtube.com",
            "media_type": "music",
            "duration_minutes": 4,
            "access": "free",
            "year": 1958,
            "volume": 6,
            "position": 2
        }
    },
    {
        "id": "https://nkalfredbot.github.io/weekly-picks/v6/3",
        "url": "https://www.youtube.com/watch?v=zVd_VLO9xcc",
        "title": "Dinner for One",
        "content_html": "<p>A 1963 British comedy sketch — 18 minutes of an elderly butler serving an imaginary dinner party to his employer, Miss Sophie, on her 90th birthday. Freddie Frinton plays all four absent guests, gets progressively drunker, and trips over a tiger-skin rug approximately 47 times. It's slapstick, it's sweet, it's deeply weird. Here's the kicker: this 18-minute sketch is the <em>most-repeated television program in Germany</em>, broadcast every New Year's Eve since 1972. Millions watch it. The British have never heard of it.</p>",
        "summary": "\"Dinner for One\" — Freddie Frinton & May Warden (1963) [18 min]. A British sketch that became Germany's New Year tradition.",
        "date_published": "2026-03-18T18:00:00Z",
        "authors": [{"name": "Freddie Frinton"}, {"name": "May Warden"}],
        "tags": ["comedy", "performance", "cultural-phenomenon", "slapstick", "television"],
        "_picks": {
            "selection_reason": "This is my favorite kind of cultural artifact: a thing that means <em>nothing</em> in its country of origin and <em>everything</em> somewhere else. How does an 18-minute British sketch become a German New Year's tradition? Nobody planned it. It just happened, the way traditions do. Watch it for the physical comedy (Frinton is brilliant). Watch it for the anthropology of how culture spreads. Watch it because millions of people you'll never meet have memorized every line.",
            "category": "cultural",
            "confidence": 0.92,
            "topics": ["comedy", "tradition", "cultural-transfer", "physical-comedy", "broadcasting-history"],
            "audience": ["comedy-fans", "cultural-anthropologists", "anyone-who-likes-weird-traditions"],
            "effort": "video",
            "mood": "inspiring",
            "source_domain": "youtube.com",
            "media_type": "performance",
            "duration_minutes": 18,
            "access": "free",
            "year": 1963,
            "volume": 6,
            "position": 3
        }
    },
    {
        "id": "https://nkalfredbot.github.io/weekly-picks/v6/4",
        "url": "https://www.youtube.com/watch?v=pcHnL7aS64Y",
        "title": "John Cage on Silence",
        "content_html": "<p>John Cage — composer, philosopher, mycologist, chaos agent — explaining why silence doesn't exist. In this short interview clip, he describes entering an anechoic chamber (a room with zero external sound) expecting silence, and instead hearing two sounds: his nervous system operating and his blood circulating. \"Until I die,\" he says, \"there will be sounds.\" This is the thinking behind <em>4'33\"</em>, the infamous \"silent\" piece that's really about listening to everything <em>else</em>. Three minutes that rewire how you hear the world.</p>",
        "summary": "\"John Cage on Silence\" — John Cage (c. 1970s) [3 min]. Why silence doesn't exist, and what that means for music.",
        "date_published": "2026-03-18T18:00:00Z",
        "authors": [{"name": "John Cage"}],
        "tags": ["music", "philosophy", "silence", "listening", "experimental"],
        "_picks": {
            "selection_reason": "Cage didn't just compose — he changed what composition <em>means</em>. This clip is the clearest explanation of his most radical idea: that silence is full, that ambient sound is music, that the act of listening is creative. You can disagree (many do), but you can't unhear it. Watch this, then go sit in a quiet room and notice how loud it actually is. Or listen to <em>4'33\"</em> and realize it's never the same piece twice.",
            "category": "philosophical",
            "confidence": 0.93,
            "topics": ["experimental-music", "listening", "philosophy-of-sound", "ambient-sound"],
            "audience": ["musicians", "sound-designers", "philosophers", "anyone-with-ears"],
            "effort": "quick-read",
            "mood": "contemplative",
            "source_domain": "youtube.com",
            "media_type": "audio",
            "duration_minutes": 3,
            "access": "free",
            "year": 1970,
            "volume": 6,
            "position": 4
        }
    }
]

# Add new items to the beginning
data["items"] = new_items + data["items"]

# Write updated feed
with open('feed.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Feed updated successfully with Volume 6 multimedia picks!")
