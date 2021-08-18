import json
import requests

history_url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+'BTCUSDT'+'&interval='+'5m'+'&limit=10'

r = requests.get(history_url)
print(r.json())
