# 01 · Compare a company with its five nearest peers

**Prompt (en)**
> Compare Samsung Electronics with its five nearest peers on P/E, ROE and revenue growth, and tell me which of the five is cheapest on P/E relative to its growth.

**Prompt (ko)**
> 삼성전자를 동종 5개사와 PER, ROE, 매출 성장률로 비교하고, 성장 대비 PER이 가장 싼 곳이 어디인지 알려줘.

**Tools the model reaches for:** `get_valuation` (one call — the five nearest same-industry peers and their medians ride along in `peer_comparison`)

One call is already a comparison. The snapshot carries annual ratios (latest full fiscal year) **and** a `ttm` block (trailing twelve months, built from the half-year and quarterly reports), plus same-market percentiles so the model can say "cheaper than 25% of Korean peers" without a second call.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "company": {
    "name": "삼성전자",
    "source": "dart",
    "page_url": "https://www.gronox.kr/companies/kr/005930",
    "stock_code": "005930"
  },
  "as_of": "2026-09-03",
  "fiscal_year": 2025,
  "currency": "KRW",
  "market_cap": 1461569652000000,
  "per": 37.861578070573984,
  "pbr": 3.349762841790251,
  "psr": 4.381126009813411,
  "roe": 10.360920902937423,
  "peer_context": {
    "market": "KR",
    "per_percentile": 0.7470153496304719,
    "roe_percentile": 0.16249559393725765
  },
  "ttm": {
    "end": "FY2026 Q2",
    "method": "annual+ytd",
    "revenue": 485272032000000,
    "net_income": 150717225000000,
    "per": 9.697429421222425,
    "psr": 3.0118563519440578,
    "roe": 26.016693876178238
  },
  "peer_comparison": {
    "basis": "same industry group, nearest by market cap",
    "sector": "Tech hardware",
    "peers": [
      {
        "name": "SK hynix Inc.",
        "code": "000660",
        "market_cap": 1165865814540000,
        "per": 26.43,
        "pbr": 9.66,
        "roe": 35.59,
        "page_url": "https://www.gronox.kr/companies/kr/000660"
      },
      {
        "name": "SAMSUNG ELECTRO-MECHANICS CO.,LTD",
        "code": "009150",
        "market_cap": 100687102208000,
        "per": 144.25,
        "pbr": 10.28,
        "roe": 7.46,
        "page_url": "https://www.gronox.kr/companies/kr/009150"
      },
      {
        "name": "LG ELECTRONICS INC.",
        "code": "066570",
        "market_cap": 32528062208600,
        "per": 26.65,
        "pbr": 1.14,
        "roe": 4.27,
        "page_url": "https://www.gronox.kr/companies/kr/066570"
      },
      {
        "name": "DOOSAN CO.,LTD",
        "code": "000150",
        "market_cap": 18218064375000,
        "per": 268.24,
        "pbr": 1.49,
        "roe": 2.04,
        "page_url":
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/valuation_samsung.structured.json`](samples/valuation_samsung.structured.json) · as the model saw it: [`samples/valuation_samsung.md`](samples/valuation_samsung.md)

## Notes
- Annual ratios and TTM ratios are different bases; peers and percentiles are on the annual basis — compare like with like.
- Works for KR, US and TW. Japan and Europe carry no prices, so there is no valuation snapshot there (ask for statements or business-mix peers instead).
- Free plan: the snapshot is complete; only the multi-year statement history behind it is capped at 4 fiscal years.
