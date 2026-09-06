# 09 · Macro snapshot from FRED

**Prompt (en)**
> Give me a one-screen macro snapshot of US rates: policy rate, 2-, 10- and 30-year yields and the 3-month bill, with the date of each.

**Prompt (ko)**
> 미국 금리 한 화면 요약: 정책금리, 2년·10년·30년물 금리, 3개월물을 각 기준일과 함께 보여줘.

**Tools the model reaches for:** `get_fred_snapshot` (`set` rates; also `us_core`, `inflation`, `labor`) · `get_fred_series` for a single series over time

A fixed set of series in one call, each with its latest and previous value and observation date. FRED's attribution line is part of the response by design.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "set": "rates",
  "as_of": "2026-09-06T13:27:30.712Z",
  "indicators": [
    {
      "id": "FEDFUNDS",
      "title": "Federal Funds Effective Rate",
      "value": 3.63,
      "prev": 3.63,
      "date": "2026-08-01",
      "units": "Percent"
    },
    {
      "id": "DGS2",
      "title": "Market Yield on U.S. Treasury Securities at 2-Year Constant Maturity, Quoted on an Investment Basis",
      "value": 4.34,
      "prev": 4.39,
      "date": "2026-09-03",
      "units": "Percent"
    },
    {
      "id": "DGS10",
      "title": "Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis",
      "value": 4.77,
      "prev": 4.79,
      "date": "2026-09-03",
      "units": "Percent"
    },
    {
      "id": "DGS30",
      "title": "Market Yield on U.S. Treasury Securities at 30-Year Constant Maturity, Quoted on an Investment Basis",
      "value": 5.25,
      "prev": 5.27,
      "date": "2026-09-03",
      "units": "Percent"
    },
    {
      "id": "T10Y2Y",
      "title": "10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity",
      "value": 0.41,
      "prev": 0.43,
      "date": "2026-09-04",
      "units": "Percent"
    },
    {
      "id": "MORTGAGE30US",
      "title": "30-Year Fixed Rate Mortgage Average in the United States",
      "value": 6.71,
      "prev": 6.66,
      "date": "2026-09-03",
      "units": "Percent"
    },
    {
      "id": "SOFR",
      "title": "Secured Overnight Financing Rate",
      "value": 3.66,
      "prev": 3.65,
      "date": "2026-09-03",
      "units": "Percent"
    }
  ],
  "source": "Source: FRED® API, Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org). This product uses the FRED API but is not endorsed or certified by the Federal Reserve Bank of 
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/fred_rates.structured.json`](samples/fred_rates.structured.json) · as the model saw it: [`samples/fred_rates.md`](samples/fred_rates.md)

## Notes
- Series like the S&P 500 or NASDAQ Composite are third-party copyright even inside FRED and are not served; rates and FX are.
- Live read; counts against the free plan's upstream allowance (20/day).
