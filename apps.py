import pygame
from app import*
from weatherData.py import*

class weather(app):
	def __init__(self, width=300, height=400, x=0, y=0):
		color1 = (30,141,246)
		#color2 = (47,202,250)
        super().__init__(width,height,x,y,color1)#,color2)
        self.isSelected = False
        self.initialClick = None
        self.isOpen = False
        self.currentWeather = getCurrentWeatherData()

        self.forecastDay1 = getForecast(1)
        self.forecastDay2 = getForecast(2)
        self.forecastDay3 = getForecast(3)

    