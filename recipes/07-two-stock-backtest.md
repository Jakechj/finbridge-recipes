# 07 · Two-stock backtest with trading costs

**Prompt (en)**
> Backtest an equal-weight portfolio of Samsung Electronics and SK hynix from 2026-03-02, rebalanced monthly, with Korean trading costs, against KOSPI.

**Prompt (ko)**
> 삼성전자와 SK하이닉스 동일비중 포트폴리오를 2026-03-02부터 월별 리밸런싱, 한국 거래비용 포함으로 백테스트하고 코스피와 비교해줘.

**Tools the model reaches for:** `backtest_portfolio` (signal at close → fill at next open, commission + slippage + sell-side tax, benchmark from the benchmarks table)

Costs are deducted from asset value at every rebalance, the benchmark pays the same costs, and fills happen at the next session's open — so the numbers are what a real order book would have allowed, not a closing-price fantasy. Runs are saved; `get_backtest_runs` lists them later.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "period": {
    "from": "2026-03-03",
    "to": "2026-09-03",
    "trading_days": 126
  },
  "currency": "KRW",
  "rebalance": "monthly",
  "initial": 10000,
  "final_value": 15049.19,
  "assets": [
    {
      "symbol": "005930",
      "name": "삼성전자",
      "market": "KR",
      "weight_pct": 50,
      "first_date": "2026-03-03",
      "dividend_adjusted": false,
      "converted": false
    },
    {
      "symbol": "000660",
      "name": "SK하이닉스",
      "market": "KR",
      "weight_pct": 50,
      "first_date": "2026-03-03",
      "dividend_adjusted": false,
      "converted": false
    }
  ],
  "metrics": {
    "total_return_pct": 50.49,
    "cagr_pct": 125.1,
    "vol_annual_pct": 99.81,
    "sharpe": 1.28,
    "mdd_pct": -48.48,
    "mdd_peak_date": "2026-06-25",
    "mdd_trough_date": "2026-07-30",
    "best_year": {
      "year": "2026",
      "ret_pct": 50.49188122516304
    },
    "worst_year": {
      "year": "2026",
      "ret_pct": 50.49188122516304
    }
  },
  "benchmark": {
    "symbol": "KOSPI",
    "from": "2026-03-03",
    "to": "2026-09-03",
    "total_return_pct": 13.6,
    "cagr_pct": 28.8,
    "excess_return_pct": 36.89
  },
  "costs": [
    "Simulation on historical data — not investment advice. Commission, one-way slippage and sell-side tax ARE deducted on the initial purchase and every rebalance (set costs=false for a gross view); dividends on KR stocks and all ETFs are not. KR stocks are price-return only (no distributions). US stocks are total-return where SEC-reported dividends exist (see dividend_adjusted per asset; ex-dates are approximated by fiscal-quarter end), otherwise price-return. ⚠ETFs are price-return only in every market right now — distributions are not in the data, so bond, REIT and high-dividend ETFs are understated. ⚠US 
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/backtest_2.structured.json`](samples/backtest_2.structured.json) · as the model saw it: [`samples/backtest_2.md`](samples/backtest_2.md)

## Notes
- Free plan history is 130 trading sessions, so start dates earlier than roughly six months back are trimmed with a note; paid plans use the full stored history (KR from 2020, TW from 2004, US from 2023-03-28).
- Korean securities transaction tax is a per-year table inside the tool (0.15% in 2025, 0.20% in 2026); slippage is an assumption exposed as `slippage_bps`.
- Survivorship: the backtest reads `prices_daily`, so delisted names stay in the sample.
