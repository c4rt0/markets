1. Create virtual env

```shell
python -m venv alpaca_venv
```

2. Activate venv :

```bash
alpaca_venv\Scripts\activate
```

3. Install the alpaca-trade-api

```zsh
pip3 install alpaca-trade-api
```

4. Install the dotenv for environment virables :

```bash
pip3 install python-dotenv
```

5. Call the API:

```sh
python alpaca_testing.py
```

6. You should receive response:

```
Account({   'account_blocked': False,
    'account_number': 'SomeAccountNumber',
    'accrued_fees': '0',
    'buying_power': '200000',
    'cash': '100000',
    'created_at': '2021-08-30T15:25:47.141933Z',
    'currency': 'USD',
    'daytrade_count': 0,
    'daytrading_buying_power': '0',
    'equity': '100000',
    'id': 'e76fa3c8-e31d-4f39-7146-3b6ae36e3b3c',
    'initial_margin': '0',
    'last_equity': '100000',
    'last_maintenance_margin': '0',
    'long_market_value': '0',
    'maintenance_margin': '0',
    'multiplier': '2',
    'non_marginable_buying_power': '100000',
    'pattern_day_trader': False,
    'pending_transfer_in': '0',
    'portfolio_value': '100000',
    'regt_buying_power': '200000',
    'short_market_value': '0',
    'shorting_enabled': True,
    'sma': '100000',
    'status': 'ACTIVE',
    'trade_suspended_by_user': False,
    'trading_blocked': False,
    'transfers_blocked': False})

```

ALSO DATA FROM REQUESTED AAPL STOCK:

```
{'AAPL': [Bar({   'c': 127.3521,
    'h': 127.44,
    'l': 126.1,
    'o': 126.53,
    't': 1623384000,
    'v': 46195695}), Bar({   'c': 130.49,
    'h': 130.49,
    'l': 127.07,
    'o': 127.82,
    't': 1623643200,
    'v': 73169843}), Bar({   'c': 129.74,
    'h': 130.6,
    'l': 129.39,
    'o': 129.88,
    't': 1623729600,
    'v': 53587032}), Bar({   'c': 130.14,
    'h': 130.89,
    'l': 128.461,
    'o': 130.29,
    't': 1623816000,
    'v': 81577235}) // and so on...
    ]}
```

Pandas dataframe:

```
AAPL

time     open     high       low     close     volume
2021-06-11 00:00:00-04:00  126.530  127.440  126.1000  127.3521   46195695
2021-06-14 00:00:00-04:00  127.820  130.490  127.0700  130.4900   73169843
2021-06-15 00:00:00-04:00  129.880  130.600  129.3900  129.7400   53587032
2021-06-16 00:00:00-04:00  130.290  130.890  128.4610  130.1400   81577235
2021-06-17 00:00:00-04:00  129.800  132.550  129.6500  131.7800   82434812
...                            ...      ...       ...       ...        ...
2021-10-26 00:00:00-04:00  149.320  150.840  149.0101  149.2600   51449318
2021-10-27 00:00:00-04:00  149.380  149.730  148.4900  148.8500   43201783
2021-10-28 00:00:00-04:00  149.860  153.165  149.7200  152.4766   77772052
2021-10-29 00:00:00-04:00  147.190  149.940  146.4128  149.8000  104258290
2021-11-01 00:00:00-04:00  148.985  149.700  147.8000  148.9900   57758481

[100 rows x 5 columns]
```

RAW DATA FORMAT:

```
{
  "AAPL": [
    {
      "t": 1623384000,
      "o": 126.53,
      "h": 127.44,
      "l": 126.1,
      "c": 127.3521,
      "v": 46195695
    },
    {
      "t": 1623643200,
      "o": 127.82,
      "h": 130.49,
      "l": 127.07,
      "c": 130.49,
      "v": 73169843
    },
    {
      "t": 1623729600,
      "o": 129.88,
      "h": 130.6,
      "l": 129.39,
      "c": 129.74,
      "v": 53587032
    },
    {
      "t": 1623816000,
      "o": 130.29,
      "h": 130.89,
      "l": 128.461,
      "c": 130.14,
      "v": 81577235
    } //... and so on
  ]
}
```
