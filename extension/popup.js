const toggle = document.getElementById("toggleSwitch");
const statusText = document.getElementById("statusText");
const statsEl = document.getElementById("stats");

async function load() {
  const { enabled, feedCache, readArticleIds } = await chrome.storage.local.get([
    "enabled", "feedCache", "readArticleIds"
  ]);

  const isEnabled = enabled !== false;
  toggle.checked = isEnabled;
  statusText.textContent = isEnabled ? "Alfred is watching" : "Alfred is sleeping";

  const total = feedCache?.items?.length ?? 0;
  const readCount = (readArticleIds || []).length;
  const remaining = Math.max(0, total - readCount);
  statsEl.textContent = `${readCount} read \u00b7 ${remaining} remaining`;
}

toggle.addEventListener("change", async () => {
  const enabled = toggle.checked;
  statusText.textContent = enabled ? "Alfred is watching" : "Alfred is sleeping";
  await chrome.runtime.sendMessage({ type: "setEnabled", enabled });
});

load();
