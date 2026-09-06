# 08 · What a 13F filer holds

**Prompt (en)**
> What are Berkshire Hathaway's ten largest 13F holdings in the latest quarter, and what changed since the prior quarter?

**Prompt (ko)**
> 버크셔 해서웨이의 최근 분기 13F 상위 10개 보유 종목은 무엇이고, 전 분기 대비 무엇이 바뀌었어?

**Tools the model reaches for:** `get_edgar_13f` (SEC EDGAR 13F-HR, latest and prior period)

Holdings come with CUSIP, share count, value and portfolio weight, plus a diff against the prior filing (new positions, exits, increases, decreases).

## What comes back (excerpt)

Captured 2026-09-06 on the free plan. Numbers are a nightly snapshot of the primary source; check `data_as_of` and the filing link before you rely on one.

```json
{
  "filer": {
    "name": "BERKSHIRE HATHAWAY INC",
    "cik": "0001067983"
  },
  "period": "2026-06-30",
  "filed": "2026-08-14",
  "total_value": 299253556246,
  "num_holdings": 29,
  "holdings": [
    {
      "issuer": "APPLE INC",
      "cusip": "037833100",
      "class": "COM",
      "shares": 227917808,
      "value": 65950296923,
      "pct_of_portfolio": 22.04
    },
    {
      "issuer": "AMERICAN EXPRESS CO",
      "cusip": "025816109",
      "class": "COM",
      "shares": 151610700,
      "value": 51282319275,
      "pct_of_portfolio": 17.14
    },
    {
      "issuer": "COCA COLA CO",
      "cusip": "191216100",
      "class": "COM",
      "shares": 400000000,
      "value": 32508000000,
      "pct_of_portfolio": 10.86
    },
    {
      "issuer": "ALPHABET INC",
      "cusip": "02079K305",
      "class": "CAP STK CL A",
      "shares": 78791167,
      "value": 28157599351,
      "pct_of_portfolio": 9.41
    },
    {
      "issuer": "BANK OF AMER CORP",
      "cusip": "060505104",
      "class": "COM",
      "shares": 483394015,
      "value": 27543790975,
      "pct_of_portfolio": 9.2
    }
  ],
  "changes": [
    {
      "issuer": "ALPHABET INC",
      "cusip": "02079K305",
      "action": "added",
      "delta_shares": 24541369,
      "new_shares": 78791167,
      "prior_shares": 54249798
    },
    {
      "issuer": "ALPHABET INC",
      "cusip": "02079K107",
      "action": "added",
      "delta_shares": 23603218,
      "new_shares": 27188433,
      "prior_shares": 3585215
    },
    {
      "issuer": "DELTA AIR LINES INC",
      "cusip": "247361702",
      "action": "added",
      "delta_shares": 17510544,
      "new_shares": 57320000,
      "prior_shares": 39809456
    },
    {
      "issuer": "BANK OF AMER CORP",
      "cusip": "060505104",
     
  … (truncated — full sample in recipes/samples/)
```

Full response: [`samples/f13_berkshire.structured.json`](samples/f13_berkshire.structured.json) · as the model saw it: [`samples/f13_berkshire.md`](samples/f13_berkshire.md)

## Notes
- 13F covers US-listed long positions of managers above $100M, reported up to 45 days after quarter end — it is a quarterly, delayed picture.
- This is a live EDGAR read (separate daily allowance on the free plan).
