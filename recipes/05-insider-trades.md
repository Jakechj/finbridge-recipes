# 05 · Check insider trades before you act

**Prompt (en)**
> Show the most recent insider share transactions for Samsung Electronics (DART) and NVIDIA (Form 4), and summarize whether executives were net buyers or sellers.

**Prompt (ko)**
> 삼성전자(DART)와 엔비디아(Form 4)의 최근 내부자 주식 거래를 보여주고, 임원들이 순매수였는지 순매도였는지 요약해줘.

**Tools the model reaches for:** `get_dart_insider_trades` · `get_edgar_insider_trades` (live reads from DART and SEC EDGAR)

Both tools read the primary filings at request time and summarise buys against sells. FinBridge provides insider net buying **point-in-time** (by disclosure date) as a research axis; it does not claim that insider buying predicts returns.

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "korea": {
    "company": {
      "corp_code": "00126380",
      "corp_name": "삼성전자"
    },
    "summary": {
      "buys": {
        "count": 3303,
        "shares": 3488719
      },
      "sells": {
        "count": 93,
        "shares": 92638
      }
    },
    "trades": [
      {
        "filedAt": "2026-08-31",
        "reporter": "김은용",
        "position": "상무",
        "registered_exec": false,
        "change": -80,
        "shares_after": 279,
        "change_rate": "0.00",
        "rcept_no": "20260831000066"
      },
      {
        "filedAt": "2026-08-28",
        "reporter": "포르치니마우로",
        "position": "사장",
        "registered_exec": false,
        "change": 530,
        "shares_after": 2822,
        "change_rate": "0.00",
        "rcept_no": "20260828001836"
      },
      {
        "filedAt": "2026-08-26",
        "reporter": "김경륜",
        "position": "상무",
        "registered_exec": false,
        "change": -173,
        "shares_after": 2250,
        "change_rate": "0.00",
        "rcept_no": "20260826000445"
      }
    ]
  },
  "us": {
    "company": {
      "cik": "0001045810",
      "name": "NVIDIA CORP",
      "ticker": "NVDA"
    },
    "summary": {
      "buys": {
        "count": 0,
        "shares": 0,
        "value": 0
      },
      "sells": {
        "count": 10,
        "shares": 1878501,
        "value": 417380185.6058
      }
    },
    "trades": [
      {
        "filedAt": "2026-09-04",
        "accessionNumber": "0001197647-26-000009",
        "owner": "COXE TENCH",
        "relationship": "Director",
        "url": "https://www.sec.gov/Archives/edgar/data/1045810/000119764726000009/wk-form4_1788555631.xml",
        "transactions": [
          {
            "date": "2026-09-02",
            "code": "G",
            "shares": 50
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/insider_kr.structured.json`](samples/insider_kr.structured.json) · as the model saw it: [`samples/insider_kr.md`](samples/insider_kr.md)

## Notes
- These are live upstream reads, which have a separate daily allowance on the free plan (20/day) alongside the 200-call quota.
- Korean reports list holdings changes by executive; US Form 4 rows carry transaction codes (P purchase, S sale).
- Sample for the US side: [`samples/insider_us.structured.json`](samples/insider_us.structured.json).
