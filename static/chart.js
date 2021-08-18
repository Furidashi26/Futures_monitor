var select_form = document.getElementById('change_tf')
interval = select_form.interval_select.value;
limit = 1000


function create_chart(element_id, interval, limit) {
	var chart = LightweightCharts.createChart(document.getElementById(element_id), {
		width: 450,
	  	height: 225,
		layout: {
			backgroundColor: '#272822',
			textColor: '#99d02b',
		},
		grid: {
			vertLines: {
				color: '#3c3f41',
			},
			horzLines: {
				color: '#3c3f41',
			},
		},
		crosshair: {
			mode: LightweightCharts.CrosshairMode.Normal,
		},
		rightPriceScale: {
			borderColor: '#5b5bc4',
		},
		timeScale: {
			borderColor: '#5b5bc4',
		},
	});
	var candleSeries = chart.addCandlestickSeries({
		upColor: '#4f7017',
		downColor: '#540e28',
		borderDownColor: '#f32672',
		borderUpColor: '#9ada2d',
		wickDownColor: '#f32672',
		wickUpColor: '#9ada2d',
	});

	// fetch('http://127.0.0.1:5000/history')
	// 	.then((r) => r.json())
	// 	.then((response) => {
	// 		console.log(response)
	// 	})
	//console.log(interval)
	var history_klines = []
	history_url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+element_id+'&interval='+interval+'&limit='+limit
	fetch(history_url)
		.then((r) => r.json())
		.then((response) => {
			//console.log(response.length - 1)
			for (let i = 0; i < response.length - 1; i++) {
					history_klines.push({
					time : response[i][0] / 1000,
					open : response[i][1],
					high : response[i][2],
					low : response[i][3],
					close : response[i][4]
				})
			}
			candleSeries.setData(history_klines)
		})


	var stream_url = 'wss://fstream.binance.com/ws/' + element_id.toLowerCase() + '@kline_' + interval
	var binanceSocket = new WebSocket(stream_url)

	binanceSocket.onmessage = function (event) {
		candleSeries.applyOptions({
			upColor: '#9ada2d',
	  		downColor: '#f32672',
	  		borderDownColor: '#f32672',
	  		borderUpColor: '#9ada2d',
	  		wickDownColor: '#f32672',
	  		wickUpColor: '#9ada2d',
		})


		var message = JSON.parse(event.data);
		var candlestick = message.k;
		candleSeries.update({
			time : candlestick.t,
			open : candlestick.o,
			high : candlestick.h,
			low : candlestick.l,
			close : candlestick.c
		})
	}
}

var symbols = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'YFIIUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'BZRXUSDT', 'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'AKROUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'LUNAUSDT', 'BTSUSDT', 'LITUSDT', 'UNFIUSDT', 'DODOUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'BTCSTUSDT', 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'BTTUSDT', 'NKNUSDT', 'SCUSDT', 'DGBUSDT', '1000SHIBUSDT', 'ICPUSDT', 'BAKEUSDT', 'GTCUSDT', 'BTCDOMUSDT', 'KEEPUSDT', 'TLMUSDT', 'IOTXUSDT']


for (item in symbols) {
	create_chart(symbols[item], interval, limit)
}


select_form.addEventListener('change', function (){
	//console.log(select_form.interval_select.value);
	interval = select_form.interval_select.value;
	console.log(interval)
	window.location.reload(false)
})



