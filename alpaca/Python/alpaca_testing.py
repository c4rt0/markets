import alpaca_trade_api as tradeapi
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


# authentication and connection details
api_key = os.getenv('ALPACA_API_KEY')
api_secret = os.getenv('ALPACA_SECRET_KEY')
base_url = os.getenv('ALPACA_ENDPOINT')
# crypto_url = os.getenv('ALPACA_CRYPTO_ENDPOINT')

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
aapl = api.get_barset('AAPL', 'day')

# obtain account information
account = api.get_account()

# Remove pandas rows limit
pd.set_option('display.max_rows', None)

print(account)
# print('Now the data: ')
# print(f'{aapl}')
# print('Pandas dataframe: ')
# print(aapl.df)
# print('Raw data format: ')
# print(aapl._raw)

active_assets = api.list_assets(status='active')

print(active_assets)
