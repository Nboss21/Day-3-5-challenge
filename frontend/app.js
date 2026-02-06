async function fetchTrends() {
  const sourcesInput = document.getElementById("sources");
  const lookbackInput = document.getElementById("lookback");
  const statusEl = document.getElementById("status");
  const trendsEl = document.getElementById("trends");

  const sources = sourcesInput.value
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
  const lookback = Number(lookbackInput.value) || 24;

  const params = new URLSearchParams();
  for (const src of sources) {
    params.append("sources", src);
  }
  params.append("lookback_hours", String(lookback));

  statusEl.textContent = "Loading trends...";

  try {
    const res = await fetch(`/api/trends?${params.toString()}`);
    if (!res.ok) {
      throw new Error(`API error: ${res.status}`);
    }
    const data = await res.json();

    trendsEl.innerHTML = "";
    for (const item of data) {
      const card = document.createElement("article");
      card.className = "trend-card";

      const score = (item.credibility_score * 100).toFixed(0);

      card.innerHTML = `
        <h2 class="trend-title">${item.topic}</h2>
        <div class="trend-meta">
          <span>${item.velocity}</span>
          <span>Credibility: ${score}%</span>
        </div>
        <p class="trend-summary">${item.summary}</p>
        <div class="trend-links">
          ${(item.source_urls || [])
            .map((url) => `<a href="${url}" target="_blank" rel="noopener noreferrer">Source</a>`)
            .join(" ")}
        </div>
      `;

      trendsEl.appendChild(card);
    }

    statusEl.textContent = `Loaded ${data.length} trends.`;
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Failed to load trends. Check the backend server.";
  }
}

const refreshBtn = document.getElementById("refresh-btn");
refreshBtn.addEventListener("click", () => {
  fetchTrends();
});

// Initial load
fetchTrends();
