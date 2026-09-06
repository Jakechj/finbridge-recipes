# 02 · Trend-template screen with an RS floor

**Prompt (en)**
> Screen the Korean market for names above RS 90 that pass the Minervini trend template, and show the top 10 with their distance from the 52-week high. Then tell me which of them are KOSDAQ listings.

**Prompt (ko)**
> 한국 시장에서 RS 90 이상이면서 미너비니 트렌드 템플릿을 통과하는 종목 상위 10개를 52주 고점 대비 거리와 함께 보여주고, 그중 코스닥 종목이 무엇인지 알려줘.

**Tools the model reaches for:** `screen_minervini` (market `kr`, `rs_min` 90) — the model narrows to KOSDAQ with a follow-up on the company pages or `screen_companies`

The screen runs nightly over every listing in Korea, the US and Taiwan with the published criteria (price above rising 50/150/200-day averages, within 25% of the 52-week high, RS percentile floor). Rows come with `page_url` so each name is one click from its filings.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "count": 10,
  "market": "kr",
  "criteria": {
    "rs_min": 90,
    "near_high_pct": 25,
    "above_low_pct": 25,
    "require_sma200_rising": true,
    "require_vcp": false
  },
  "rows": [
    {
      "name": "JW신약",
      "source": "dart",
      "page_url": "https://www.gronox.kr/companies/kr/067290",
      "stock_code": "067290",
      "as_of": "2026-09-03",
      "close": 3430,
      "sma50": 2051.48,
      "sma150": 1974.76,
      "sma200": 1909.89,
      "rs_pctile": 99,
      "rs_120d": 88.92,
      "pct_from_52w_hi": -10.21,
      "pct_from_52w_lo": 175.28,
      "ret_120d": 71.59
    },
    {
      "name": "자이에스앤디",
      "source": "dart",
      "page_url": "https://www.gronox.kr/companies/kr/317400",
      "stock_code": "317400",
      "as_of": "2026-09-03",
      "close": 11240,
      "sma50": 7112.4,
      "sma150": 5217.2,
      "sma200": 4931.1,
      "rs_pctile": 99,
      "rs_120d": 184,
      "pct_from_52w_hi": -5.7,
      "pct_from_52w_lo": 268.52,
      "ret_120d": 166.67
    },
    {
      "name": "아스플로",
      "source": "dart",
      "page_url": "https://www.gronox.kr/companies/kr/159010",
      "stock_code": "159010",
      "as_of": "2026-09-03",
      "close": 24950,
      "sma50": 18197.8,
      "sma150": 12614.9,
      "sma200": 10583.63,
      "rs_pctile": 99,
      "rs_120d": 408.47,
      "pct_from_52w_hi": -3.48,
      "pct_from_52w_lo": 628.47,
      "ret_120d": 391.14
    },
    {
      "name": "벡트",
      "source": "dart",
      "page_url": "https://www.gronox.kr/companies/kr/457600",
      "stock_code": "457600",
      "as_of": "2026-09-03",
      "close": 5270,
      "sma50": 3406.5,
      "sma150": 2523.19,
      "sma200": 2512.52,
      "rs_pctile": 99,
      "rs_120d": 190.67,
      "pct_from_52w_hi": -7.54,
      "pct_from_52w
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/minervini_kr.structured.json`](samples/minervini_kr.structured.json) · as the model saw it: [`samples/minervini_kr.md`](samples/minervini_kr.md)

## Notes
- `market` takes `kr`, `us`, `tw` or `all`; the screen has no exchange filter, so KOSDAQ-only is a second step (the model can do it).
- US price history starts 2023-03-28, so long-window figures are shallower there; Japan is not screenable (no redistributable prices).
- Liquidity floors are applied so illiquid micro-caps do not top the list by RS alone.
