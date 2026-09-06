# 04 · Korea vs US in one currency

**Prompt (en)**
> Samsung Electronics vs Apple: revenue, operating income and net income for the last 3 fiscal years, converted to USD, with the exchange rate used.

**Prompt (ko)**
> 삼성전자와 애플의 최근 3개 회계연도 매출·영업이익·순이익을 달러로 환산해 비교하고, 사용한 환율도 알려줘.

**Tools the model reaches for:** `compare_financials_kr_us` (K-IFRS consolidated vs US-GAAP 10-K, FRED DEXKOUS annual average)

The tool does the currency conversion with FRED's KRW/USD annual averages and states them, so the model does not invent a rate. Both sides carry `page_url` and their accounting basis.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "kr": {
    "name": "삼성전자",
    "corp_code": "00126380",
    "stock_code": "005930",
    "basis": "consolidated (K-IFRS)",
    "page_url": "https://www.gronox.kr/companies/kr/005930"
  },
  "us": {
    "name": "Apple Inc.",
    "cik": "0000320193",
    "ticker": "AAPL",
    "basis": "US-GAAP (10-K)",
    "page_url": "https://www.gronox.kr/companies/us/AAPL"
  },
  "fx": {
    "series": "DEXKOUS (KRW per USD, annual avg)",
    "rates": {
      "2023": {
        "rate": 1306.76,
        "approx": false
      },
      "2024": {
        "rate": 1363.44,
        "approx": false
      },
      "2025": {
        "rate": 1421.4,
        "approx": false
      }
    }
  },
  "comparison": [
    {
      "metric": "revenue",
      "rows": [
        {
          "fiscal_year": 2025,
          "kr_krw": 333605938000000,
          "kr_usd": 234702362459.5469,
          "us_usd": 416161000000,
          "ratio_kr_over_us": 0.564
        },
        {
          "fiscal_year": 2024,
          "kr_krw": 300870903000000,
          "kr_usd": 220670438743.17902,
          "us_usd": 391035000000,
          "ratio_kr_over_us": 0.564
        },
        {
          "fiscal_year": 2023,
          "kr_krw": 258935494000000,
          "kr_usd": 198150765251.46164,
          "us_usd": 383285000000,
          "ratio_kr_over_us": 0.517
        }
      ]
    },
    {
      "metric": "operating_income",
      "rows": [
        {
          "fiscal_year": 2025,
          "kr_krw": 43601051000000,
          "kr_usd": 30674722808.49866,
          "us_usd": 133050000000,
          "ratio_kr_over_us": 0.231
        },
        {
          "fiscal_year": 2024,
          "kr_krw": 32725961000000,
          "kr_usd": 24002494425.86399,
          "us_usd": 123216000000,
          "ratio_kr_over_us": 0.195
      
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/compare_kr_us.structured.json`](samples/compare_kr_us.structured.json) · as the model saw it: [`samples/compare_kr_us.md`](samples/compare_kr_us.md)

## Notes
- Accounting standards differ (K-IFRS vs US-GAAP); the notes in the response say which lines are comparable.
- FX comes from FRED (DEXKOUS) — FRED's source line must stay with the numbers if you republish them.
