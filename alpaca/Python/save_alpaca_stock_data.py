import requests
import alpaca_trade_api as tradeapi
import pandas as pd
import os
import json
from dotenv import load_dotenv
load_dotenv()

# authentication and connection details
api_key = os.getenv('ALPACA_API_KEY')
api_secret = os.getenv('ALPACA_SECRET_KEY')
base_url = os.getenv('ALPACA_ENDPOINT')

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
aapl = api.get_barset('AAPL', 'day')

# obtain account information
account = api.get_account()

print(account)

json_data = aapl._raw

with open('alpaca_aapl.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
