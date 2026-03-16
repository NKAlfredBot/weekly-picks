const SITE_URL = "https://nkalfredbot.github.io/weekly-picks/";

async function getState() {
  return chrome.storage.local.get(["feedCache", "readArticleIds"]);
}

function pickNext(items, readIds) {
  const readSet = new Set(readIds || []);
  const unread = items.filter(i => !readSet.has(i.id));
  if (unread.length === 0) return null;
  // Sort: highest volume first, then lowest position first
  unread.sort((a, b) => {
    const va = a._picks?.volume ?? 0;
    const vb = b._picks?.volume ?? 0;
    if (vb !== va) return vb - va;
    return (a._picks?.position ?? 0) - (b._picks?.position ?? 0);
  });
  return unread[0];
}

async function markRead(id) {
  const { readArticleIds } = await chrome.storage.local.get("readArticleIds");
  const ids = readArticleIds || [];
  if (!ids.includes(id)) ids.push(id);
  await chrome.storage.local.set({ readArticleIds: ids });
}

function render(pick, totalUnread) {
  const el = document.getElementById("content");

  if (!pick) {
    el.innerHTML = `
      <div class="empty">
        <h2>You've read everything</h2>
        <p>Alfred has no more picks for you. Check back next week.</p>
        <a href="${SITE_URL}">Browse the archive</a>
      </div>
    `;
    return;
  }

  const p = pick._picks || {};
  const authors = (pick.authors || []).map(a => a.name).join(", ");
  const badges = [p.mood, p.effort, p.category].filter(Boolean);

  el.innerHTML = `
    <div class="header">Alfred intercepted your Twitter visit &middot; ${totalUnread} pick${totalUnread === 1 ? '' : 's'} remaining</div>
    <h1 class="title">${esc(pick.title)}</h1>
    ${authors ? `<div class="author">by ${esc(authors)}</div>` : ''}
    <div class="reason">${esc(p.selection_reason || pick.summary || '')}</div>
    <div class="badges">
      ${badges.map(b => `<span class="badge">${esc(b)}</span>`).join('')}
    </div>
    <div class="actions">
      <button class="btn btn-primary" id="readBtn">Read Article</button>
      <button class="btn btn-secondary" id="skipBtn">Skip</button>
    </div>
    <a class="bypass" id="bypassBtn">Let me through to Twitter</a>
  `;

  document.getElementById("readBtn").addEventListener("click", async () => {
    await markRead(pick.id);
    window.location.href = pick.url;
  });

  document.getElementById("skipBtn").addEventListener("click", async () => {
    await markRead(pick.id);
    await init(); // reload with next pick
  });

  document.getElementById("bypassBtn").addEventListener("click", async (e) => {
    e.preventDefault();
    await chrome.runtime.sendMessage({ type: "bypassOnce" });
    window.location.href = "https://twitter.com";
  });
}

function esc(str) {
  const d = document.createElement("div");
  d.textContent = str;
  return d.innerHTML;
}

async function init() {
  const { feedCache, readArticleIds } = await getState();
  if (!feedCache || !feedCache.items) {
    document.getElementById("content").innerHTML = `
      <div class="empty">
        <h2>Loading...</h2>
        <p>Alfred is fetching the feed. Try refreshing in a moment.</p>
      </div>
    `;
    return;
  }
  const readSet = new Set(readArticleIds || []);
  const totalUnread = feedCache.items.filter(i => !readSet.has(i.id)).length;
  const pick = pickNext(feedCache.items, readArticleIds);
  render(pick, totalUnread);
}

init();
