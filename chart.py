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

def get_symbols():
    symbols_list = []
    r = requests.get('https://fapi.binance.com/fapi/v1/exchangeInfo')
    result = r.json()['symbols']
    for item in result:
        if item['symbol'][-1] != 'T':
            continue
        symbols_list.append(item['symbol'])
    #print(symbols_list)
    return symbols_list

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




