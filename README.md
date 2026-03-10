# Oil vs Stock Tracker

Compare oil price movements with any stock — side by side, in real time.

**[Live Demo →](https://oil-vs-stock-tracker.onrender.com)**

![Dashboard screenshot](https://img.shields.io/badge/status-live-brightgreen)

## What it does

Enter a stock ticker and instantly see how it moves relative to crude oil prices. The dashboard fetches real market data from Yahoo Finance and overlays both on a single interactive chart.

- **Any stock ticker** — type a symbol (AAPL, TSLA, XOM, etc.) and hit Enter
- **Oil benchmarks** — WTI Crude or Brent Crude
- **Time ranges** — 1 month to 5 years
- **Two views:**
  - *% Change* — normalizes both to percentage change from start for direct comparison
  - *Absolute* — dual Y-axes showing actual dollar prices
- **Correlation** — Pearson correlation coefficient between the two, updated per query
- **Stats cards** — latest price and period return for both oil and your stock

## Run locally

No dependencies beyond Python 3:

```bash
git clone https://github.com/narendranag/oil-vs-stock-tracker.git
cd oil-vs-stock-tracker
python3 server.py
```

Open [http://localhost:3456](http://localhost:3456).

## How it works

- `index.html` — single-page dashboard built with [Chart.js](https://www.chartjs.org/)
- `server.py` — lightweight Python server that serves static files and proxies Yahoo Finance API requests (avoids CORS issues in the browser)

No npm, no build step, no external Python packages.

## Deploy your own

The app is configured for one-click deploy on [Render](https://render.com):

1. Fork this repo
2. Connect it on Render as a new **Web Service**
3. Render auto-detects `render.yaml` — just click Deploy

## License

MIT
