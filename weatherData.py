#Using standard process of getting weather from wunderground API
#(I read the documentation)

import urllib.request as urllib2
import json

def getCurrentWeatherData(system="f"):
	if system == "c":
		units = "metric"
	else:
		units = "in"

	#Getting data
	f = urllib2.urlopen('http://api.wunderground.com/api/32398c47c8ba24e3/geolookup/conditions/q/PA/pittsburgh.json')
	jsonString = f.read().decode('utf-8')
	parsedJSON  = json.loads(jsonString)

	#Extracting relevant information
	location = parsedJSON['location']['city']
	temperature = parsedJSON["current_observation"]["temp"+"_"+system]
	feelsLike = parsedJSON['current_observation']["feelslike"+"_"+system]
	weather = parsedJSON['current_observation']["weather"]
	wind = parsedJSON["current_observation"]["wind_string"]
	precip = parsedJSON["current_observation"]["precip_today"+"_"+units]

	f.close()

	pack = {"location":location,"temp":temperature,"feelsLike":feelsLike,
	"weather":weather,"wind":wind,"precip":precip}
	return pack

print (getCurrentWeatherData())

def getForecast(day,system="f"):
	if system == "c":
		system = "celsius"
		units = "mm"
	else:
		system = "fahrenheit"
		units = "in"

	#Getting data
	f = urllib2.urlopen('http://api.wunderground.com/api/32398c47c8ba24e3/forecast/q/PA/pittsburgh.json')
	jsonString = f.read().decode('utf-8')
	parsedJSON  = json.loads(jsonString)

	#Extracting relevant information
	selectedDay = parsedJSON['forecast']["simpleforecast"]['forecastday'][day]
	conditions = selectedDay["conditions"]
	low = selectedDay["low"][system]
	high = selectedDay["high"][system]
	precip = selectedDay["qpf_allday"][units]
	dateTitle = selectedDay["date"]["weekday"]

	f.close()

	pack = {"day":dateTitle,"conditions":conditions,"low":low,
	"high":high,"dateTitle":dateTitle}

	return pack