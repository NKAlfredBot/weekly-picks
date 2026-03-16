const FEED_URL = "https://nkalfredbot.github.io/weekly-picks/feed.json";
const REFRESH_INTERVAL_MS = 24 * 60 * 60 * 1000; // 24 hours

const REDIRECT_RULES = [
  {
    id: 1,
    priority: 1,
    action: {
      type: "redirect",
      redirect: { extensionPath: "/intercept.html" }
    },
    condition: {
      urlFilter: "||twitter.com",
      resourceTypes: ["main_frame"]
    }
  },
  {
    id: 2,
    priority: 1,
    action: {
      type: "redirect",
      redirect: { extensionPath: "/intercept.html" }
    },
    condition: {
      urlFilter: "||x.com",
      resourceTypes: ["main_frame"]
    }
  }
];

async function fetchFeed() {
  try {
    const res = await fetch(FEED_URL);
    if (!res.ok) return;
    const feed = await res.json();
    await chrome.storage.local.set({
      feedCache: feed,
      feedLastFetched: new Date().toISOString()
    });
  } catch (e) {
    console.error("Alfred: feed fetch failed", e);
  }
}

async function maybeFetchFeed() {
  const { feedLastFetched } = await chrome.storage.local.get("feedLastFetched");
  if (!feedLastFetched || Date.now() - new Date(feedLastFetched).getTime() > REFRESH_INTERVAL_MS) {
    await fetchFeed();
  }
}

async function setRedirectRules(enabled) {
  const existingIds = REDIRECT_RULES.map(r => r.id);
  if (enabled) {
    await chrome.declarativeNetRequest.updateDynamicRules({
      removeRuleIds: existingIds,
      addRules: REDIRECT_RULES
    });
  } else {
    await chrome.declarativeNetRequest.updateDynamicRules({
      removeRuleIds: existingIds
    });
  }
}

chrome.runtime.onInstalled.addListener(async () => {
  const { enabled } = await chrome.storage.local.get("enabled");
  const isEnabled = enabled !== false; // default to true
  if (isEnabled) {
    await chrome.storage.local.set({ enabled: true });
  }
  await setRedirectRules(isEnabled);
  await fetchFeed();
});

chrome.runtime.onStartup.addListener(async () => {
  const { enabled } = await chrome.storage.local.get("enabled");
  await setRedirectRules(enabled !== false);
  await maybeFetchFeed();
});

chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (msg.type === "setEnabled") {
    chrome.storage.local.set({ enabled: msg.enabled }).then(() => {
      setRedirectRules(msg.enabled).then(() => sendResponse({ ok: true }));
    });
    return true; // async response
  }
  if (msg.type === "bypassOnce") {
    // Temporarily disable rules, re-enable after a short delay
    setRedirectRules(false).then(() => {
      setTimeout(() => {
        chrome.storage.local.get("enabled").then(({ enabled }) => {
          if (enabled !== false) setRedirectRules(true);
        });
      }, 3000);
      sendResponse({ ok: true });
    });
    return true;
  }
});
