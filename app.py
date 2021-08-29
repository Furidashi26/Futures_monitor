import json

from flask import Flask, render_template, redirect, jsonify
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config, csv
from binance.enums import *
import chart

interval = '15m'

app = Flask(__name__)

client = Client(config.API, config.API_SECRET)

@app.route("/")
def index():
	global interval
	int = interval
	symbols = chart.get_symbols(0, 999999)
	symbols_arr = json.loads(symbols)
	symbols_count = len(symbols_arr)
	return render_template('index.html', symbols=symbols, symbols_arr=symbols_arr, label='All symbols', market='F', symbols_count=symbols_count)

@app.route("/three")
def three():
	global interval
	int = interval
	symbols = chart.get_symbols(0, 3)
	symbols_arr = json.loads(symbols)
	symbols_count = len(symbols_arr)
	return render_template('index.html', symbols=symbols, symbols_arr=symbols_arr, label='0 - 3 USDT', market='F', symbols_count=symbols_count)

@app.route("/ten")
def ten():
	global interval
	int = interval
	symbols = chart.get_symbols(3, 10)
	symbols_arr = json.loads(symbols)
	symbols_count = len(symbols_arr)
	return render_template('index.html', symbols=symbols, symbols_arr=symbols_arr, label='3 - 10 USDT', market='F', symbols_count=symbols_count)

@app.route("/fifty")
def fifty():
	global interval
	int = interval
	symbols = chart.get_symbols(10, 50)
	symbols_arr = json.loads(symbols)
	symbols_count = len(symbols_arr)
	return render_template('index.html', symbols=symbols, symbols_arr=symbols_arr, label='10 - 50 USDT', market='F', symbols_count=symbols_count)

@app.route("/spot")
def spot():
	global interval
	int = interval
	symbols = chart.get_symbols_spot(0, 999999)
	symbols_arr = json.loads(symbols)
	symbols_count = len(symbols_arr)
	return render_template('index.html', symbols=symbols, symbols_arr=symbols_arr, label='All spot', market='S', symbols_count=symbols_count)

@app.route("/history")
def history():
	return jsonify(chart.get_history_array())

@app.route("/testing")
def testing():
	symbols = chart.get_symbols()
	return 'hello'

if __name__ == "__main__":
	app.run(host='0.0.0.0')
