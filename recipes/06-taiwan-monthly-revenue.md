# 06 · Taiwan monthly revenue trend

**Prompt (en)**
> Show TSMC's monthly revenue for the last 12 months with month-over-month and year-over-year change, and the date each figure was disclosed.

**Prompt (ko)**
> TSMC의 최근 12개월 월매출을 전월 대비·전년 동월 대비 증감률, 공시일과 함께 보여줘.

**Tools the model reaches for:** `query_db` on the `monthly_revenue` table (Taiwanese issuers report monthly revenue to the exchange; FinBridge stores it with MoM/YoY)

Taiwan is the market where **monthly** revenue is public. The table is queryable with read-only SQL; the model writes the query after `get_db_schema`.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "columns": [
    "name",
    "year",
    "month",
    "revenue",
    "revenue_mom",
    "revenue_yoy",
    "cum_yoy",
    "disclosed_date"
  ],
  "rows": [
    [
      "台灣積體電路製造股份有限公司",
      2026,
      7,
      467580548000,
      5.624961765550318,
      44.68755126916978,
      37.01215713355301,
      "2026-08-17"
    ],
    [
      "台灣積體電路製造股份有限公司",
      2026,
      6,
      442679969000,
      null,
      null,
      null,
      null
    ],
    [
      "台灣積體電路製造股份有限公司",
      2025,
      7,
      323165707000,
      null,
      null,
      null,
      null
    ]
  ],
  "row_count": 3,
  "truncated": false
}
```

Full response: [`samples/tw_monthly.structured.json`](samples/tw_monthly.structured.json) · as the model saw it: [`samples/tw_monthly.md`](samples/tw_monthly.md)

## Notes
- The monthly-revenue history accumulates from September 2026 (TWSE OpenAPI publishes the current month, so earlier months arrive as they are re-published); expect the series to fill in over the coming months.
- Taiwan statements are a current snapshot (no annual history yet) — ask Taiwan for prices (22 years, from 2004), ratios and monthly revenue rather than multi-year statement growth.
- Attribution: TWSE/TPEx data must be credited (臺灣證券交易所) when republished.
