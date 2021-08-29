import json

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config
import requests

client = Client(config.API, config.API_SECRET)

def fetch_last_history(symbol):
    #candlesticks = client.futures_historical_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_5MINUTE, limit=20)
    r = requests.get('https://fapi.binance.com/fapi/v1/klines')
    print(r)

    # processed_candlesticks = []
    #
    # for data in candlesticks:
    #     candlestick = {
    #         "time": data[0] / 1000,
    #         "open": data[1],
    #         "high": data[2],
    #         "low": data[3],
    #         "close": data[4],
    #     }
    #     processed_candlesticks.append(candlestick)
    # #print(processed_candlesticks)
    # return processed_candlesticks[:-1]

def get_symbols(start_price, end_price):
    symbols_list = ["BTCUSDT"]
    req = requests.get('https://fapi.binance.com/fapi/v1/ticker/24hr')
    req = req.json()
    # r = requests.get('https://fapi.binance.com/fapi/v1/exchangeInfo')
    # result = r.json()["symbols"]
    for item in req:
        if item["symbol"][-1] != "T":
            continue
        if item["symbol"] == "BTCUSDT":
            continue
        if float(item["lastPrice"]) < float(start_price) or float(item["lastPrice"]) > float(end_price):
            continue

        symbols_list.append(item["symbol"])
    json_symbols = json.dumps(symbols_list)
    print(json_symbols)
    return json_symbols

def get_symbols_spot(start_price, end_price):
    symbols_list = ["BTCUSDT"]
    req = requests.get('https://api.binance.com/api/v3/ticker/24hr')
    req = req.json()
    # r = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    # result = r.json()["symbols"]
    for item in req:
        if item["symbol"][-1] != "T":
            continue
        if item["symbol"] == "BTCUSDT":
            continue
        if float(item["lastPrice"]) < float(start_price) or float(item["lastPrice"]) > float(end_price):
            continue

        symbols_list.append(item["symbol"])

    json_symbols = json.dumps(symbols_list)
    return json_symbols

def get_history_array():
    history_array = []
    symbols = get_symbols()
    print(symbols)
    for item in symbols:
        #pass
        candlesticks = fetch_last_history(item)
        #print(candlesticks)
        history_array.append({
            item : candlesticks,
        })
    print(history_array)
    return history_array
get_symbols(0, 999999)




