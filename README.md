# FinBridge recipes

**The finance MCP for AI stock analysis.** FinBridge is a hosted data service that collects official financial data for **Korea, the United States, Japan and Taiwan** (plus European statements) every night, normalises it to one schema, and serves it to ChatGPT, Claude, Cursor or any MCP client — and to everything else over a REST API.

This repository is a set of **recipes**: questions that work, the tools the model reaches for, and **real responses** captured from the free plan on 2026-09-06. Copy a prompt, paste it into the model you already use with FinBridge connected, and compare what you get with the sample. **Three steps, not two**: connect once → in each new chat turn FinBridge on (Claude: + → FinBridge; ChatGPT: + → More → FinBridge) → ask.

- MCP endpoint: `https://mcp.gronox.kr/mcp` (Streamable HTTP, OAuth or Bearer key) — [connect in three steps](https://www.gronox.kr/connect)
- REST API: `https://mcp.gronox.kr/api/v1` — [OpenAPI 3.1](https://mcp.gronox.kr/api/v1/openapi.json)
- Free plan: 200 calls/day, every tool, the last 4 fiscal years and 130 trading sessions, no card. Paid plans add history depth.
- Tool reference: https://www.gronox.kr/docs · Prompt library: https://www.gronox.kr/prompts · Data sources and licences: https://www.gronox.kr/sources

## Recipes

| # | Recipe | Tools | Markets |
|---|---|---|---|
| 01 | [Compare a company with its five nearest peers](recipes/01-peers-valuation.md) | `get_valuation` | KR · US · TW |
| 02 | [Trend-template screen with an RS floor](recipes/02-trend-template-screen.md) | `screen_minervini` | KR · US · TW |
| 03 | [Four years of Apple's margins, with the filing behind each number](recipes/03-apple-annual-margins.md) | `get_edgar_financials` | US |
| 04 | [Korea vs US in one currency](recipes/04-kr-us-single-currency.md) | `compare_financials_kr_us` | KR · US |
| 05 | [Check insider trades before you act](recipes/05-insider-trades.md) | `get_dart_insider_trades` · `get_edgar_insider_trades` | KR · US |
| 06 | [Taiwan monthly revenue trend](recipes/06-taiwan-monthly-revenue.md) | `query_db` | TW |
| 07 | [Two-stock backtest with trading costs](recipes/07-two-stock-backtest.md) | `backtest_portfolio` | KR · US · TW |
| 08 | [What a 13F filer holds](recipes/08-13f-holdings.md) | `get_edgar_13f` | US |
| 09 | [Macro snapshot from FRED](recipes/09-fred-snapshot.md) | `get_fred_snapshot` | — |

Bonus: [business-mix peers for a Japanese conglomerate](recipes/samples/peers_toyota.md) (`get_peers`, `rank=segments`) — Japan carries statements and segments, not prices.

Every sample lives in [`recipes/samples/`](recipes/samples/) twice: the JSON the tool returned (`*.structured.json`) and the text the model saw (`*.md`).

## Clients

Configuration snippets in [`clients/`](clients/): Claude.ai / Claude Desktop, Claude Code, Cursor, Gemini CLI, ChatGPT developer mode, Cline. A Python example against the REST API is in [`python/rest_example.py`](python/rest_example.py).

## What to expect from the free plan

- Statements: the last **4 fiscal years** (annual, half or quarterly reports inside those years). Prices: the last **130 trading sessions**. Deeper history returns a note and a link instead of numbers.
- Every company answer carries `page_url` (a public page with the filing) and `data_as_of` (price session, snapshot date, latest reported period). Ratios are a nightly snapshot, not real-time.
- Peer sets: Korea, Japan and Taiwan use industry groups that match how those markets classify companies. **US peers come from SIC codes and are sometimes plainly wrong** (a chip-equipment maker can land among pharma names), and **Europe groups all IT and electronics into one bucket** — read US and EU peer lists as a starting point, not a classification you can rely on. Ratios computed over a wrong peer set are wrong in the same way.
- Coverage that shapes the answers: Japan and Europe have **no prices** (nothing redistributable), so no valuation, screens or backtests there. Taiwan statements are a current snapshot (no annual history yet), so ask Taiwan for prices, ratios and monthly revenue rather than multi-year growth. US prices start 2023-03-28. Details: https://www.gronox.kr/sources

## Licence

The recipes, prompts and code in this repository are MIT ([LICENSE](LICENSE)). The **data** in the samples comes from OpenDART, SEC EDGAR, EDINET, TWSE/TPEx, data.go.kr, Databento and FRED under each source's terms — see https://www.gronox.kr/sources for attribution obligations (TWSE/TPEx and EDINET require attribution; FRED requires its source line). Information only, not investment advice.
