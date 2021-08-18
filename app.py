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
	symbols = chart.get_symbols()
	return render_template('index.html', symbols=symbols)


@app.route("/history")
def history():
    return jsonify(chart.get_history_array())

@app.route("/testing")
def testing():
    symbols = chart.get_symbols()
    return render_template('index.html', symbols=symbols)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
