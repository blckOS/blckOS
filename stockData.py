from googlefinance import getQuotes
import json

#Standard way of doing this (read documentation).

def getStockData():
	appleStr = json.dumps(getQuotes('AAPL'))
	apple = json.loads(appleStr)
	applePrice = apple[0]["LastTradePrice"]

	googleStr = json.dumps(getQuotes('GOOG'))
	google = json.loads(googleStr)
	googlePrice = google[0]["LastTradePrice"]
	
	pack = {"AAPL":applePrice,"GOOG":googlePrice}
	return pack

