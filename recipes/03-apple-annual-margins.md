# 03 · Four years of Apple's margins, with the filing behind each number

**Prompt (en)**
> Pull Apple's last four annual income statements and summarize how gross margin and operating margin moved, citing the 10-K each number comes from.

**Prompt (ko)**
> 애플의 최근 4개 연간 손익계산서를 가져와 매출총이익률과 영업이익률이 어떻게 움직였는지 요약하고, 각 숫자의 10-K를 출처로 붙여줘.

**Tools the model reaches for:** `get_edgar_financials` (`freq` annual, `periods` 4, four metrics)

Each period carries its fiscal year end and the date the 10-K was disclosed, so the model can cite the filing rather than a vendor table. The same call attaches the five nearest peers' ratios (`peer_comparison`, omitted here for length).

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "company": {
    "name": "Apple Inc.",
    "id": "0000320193",
    "source": "edgar",
    "ticker": "AAPL",
    "page_url": "https://www.gronox.kr/companies/us/AAPL"
  },
  "basis": "US-GAAP (10-K)",
  "periods": [
    {
      "period": "FY2025",
      "end": "2025-09-27",
      "disclosed": "2025-10-31",
      "metrics": {
        "revenue": 416161000000,
        "gross_profit": 195201000000,
        "operating_income": 133050000000,
        "net_income": 112010000000
      }
    },
    {
      "period": "FY2024",
      "end": "2024-09-28",
      "disclosed": "2024-11-01",
      "metrics": {
        "revenue": 391035000000,
        "gross_profit": 180683000000,
        "operating_income": 123216000000,
        "net_income": 93736000000
      }
    },
    {
      "period": "FY2023",
      "end": "2023-09-30",
      "disclosed": "2023-11-03",
      "metrics": {
        "revenue": 383285000000,
        "gross_profit": 169148000000,
        "operating_income": 114301000000,
        "net_income": 96995000000
      }
    },
    {
      "period": "FY2022",
      "end": "2022-09-24",
      "disclosed": "2022-10-28",
      "metrics": {
        "revenue": 394328000000,
        "gross_profit": 170782000000,
        "operating_income": 119437000000,
        "net_income": 99803000000
      }
    }
  ],
  "data_as_of": {
    "generated_at": "2026-09-06T13:30:09.747Z",
    "market": "US",
    "fetched": "SEC XBRL company facts fetched live at request time; each period carries its own filing date.",
    "refresh": "US prices load nightly from Databento after the close; SEC statements load within a day of filing."
  }
}
```

Full response: [`samples/apple_annual.structured.json`](samples/apple_annual.structured.json) · as the model saw it: [`samples/apple_annual.md`](samples/apple_annual.md)

## Notes
- Free plan returns the last 4 fiscal years; deeper history (Apple's statements go back to FY1967 in the database) needs a paid plan.
- For research that must not see restated numbers, the factor and backtest tools use the as-filed (point-in-time) history from SEC's DERA datasets; this statements tool returns the latest reported values.
- Quarterly: `freq: quarterly` returns discrete Q1–Q3 from 10-Q filings (no Q4 row — that is the 10-K).
