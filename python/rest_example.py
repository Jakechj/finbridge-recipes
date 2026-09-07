#!/usr/bin/env python3
"""FinBridge REST v1 in 40 lines — the same data the MCP tools serve, over plain GET.

    export FINBRIDGE_API_KEY=smcp_...      # free key: https://www.gronox.kr/login (Google sign-in)
    python3 rest_example.py kr 005930      # Samsung Electronics
    python3 rest_example.py us AAPL

Endpoints (OpenAPI 3.1: https://mcp.gronox.kr/api/v1/openapi.json):
    /api/v1/companies/{market}/{symbol}              profile: key figures, annual results, segments, filings, peers
    /api/v1/companies/{market}/{symbol}/financials   statements, annual or quarterly (plan depth applies)
    /api/v1/companies/{market}/{symbol}/valuation    valuation snapshot + five nearest peers (+ ttm block)
    /api/v1/companies/{market}/{symbol}/peers        peers by industry+size or by business mix
      markets: kr, us, tw, jp, eu (Europe is addressed by ISIN, e.g. eu/NL0010273215; no prices there,
      so ratios are null). Peer quality differs by market: Korea, Japan and Taiwan use industry groups
      that hold up; US peers come from SIC codes and are sometimes plainly wrong, and Europe puts all
      IT and electronics in one group — read those two as a starting point, not a classification.
    /api/v1/companies/{market}/{symbol}/prices       daily OHLCV, adjusted, newest first (not Japan)
Every call counts 1 against the daily quota; the response headers carry X-RateLimit-Remaining.
"""
import json
import os
import sys
import urllib.request

API = "https://mcp.gronox.kr/api/v1"


def get(path: str, key: str) -> tuple[dict, dict]:
    req = urllib.request.Request(f"{API}{path}", headers={"Authorization": f"Bearer {key}", "User-Agent": "finbridge-recipes/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8")), dict(r.headers)


def main() -> None:
    key = os.environ.get("FINBRIDGE_API_KEY") or sys.exit("set FINBRIDGE_API_KEY (free key at https://www.gronox.kr/login)")
    market, symbol = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ("kr", "005930")

    profile, headers = get(f"/companies/{market}/{symbol}", key)
    c = profile["company"]
    print(f"{c['name']} ({c['symbol']}, {c['market']}) — source {c['source']} — {c['page_url']}")
    for row in profile["annual_results"]:
        print(f"  FY{row['fiscal_year']}: revenue {row['revenue']:,} {row['currency']}  net income {row['net_income']:,}")
    print("  as of:", profile["data_as_of"]["snapshot_as_of"], "| quota left today:", headers.get("X-RateLimit-Remaining"))

    fin, _ = get(f"/companies/{market}/{symbol}/financials?period=quarterly&limit=8", key)
    print(f"\nquarterly rows: {fin['count']} of {fin['rows_available']}" + (f" — {fin['plan_note']}" if fin.get("plan_note") else ""))
    for r in fin["rows"]:
        print(f"  FY{r['fiscal_year']} Q{r['quarter']}: revenue {r['revenue']:,}" if r.get("revenue") else f"  FY{r['fiscal_year']} Q{r['quarter']}: —")

    if market != "jp":
        val, _ = get(f"/companies/{market}/{symbol}/valuation", key)
        ttm = val.get("ttm") or {}
        print(f"\nP/E {val.get('per')}, P/B {val.get('pbr')} (FY{val.get('fiscal_year')}); TTM P/E {ttm.get('per')} ({ttm.get('end')})")
        peers = (val.get("peer_comparison") or {}).get("peers") or []
        print("peers:", ", ".join(f"{p['name']} P/E {p.get('per')}" for p in peers[:5]))


if __name__ == "__main__":
    main()
