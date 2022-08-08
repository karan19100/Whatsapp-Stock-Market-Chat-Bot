# MARKETSTACK_KEY
# 1. explore the marketstack doc and find revelant url 
# 2. integrate API
# 3. import 

import os 
import requests 
import json 

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params = { 
            'access_key': "9816881087a64a9bc359e26e17ad4d71"
    }
    end_point = ''.join([BASE_URL,"tickers/", stock_symbol, "/intraday/latest"])
    api_result = requests.get(end_point, params)
    print(api_result)
    json_result = json.loads(api_result.text)
    return {
        "last_price": json_result["last"]
         }
