#! /usr/bin/python3
#open weather man api key : 788b6de43561e5e0cde2ef5041863aef
# 
import pyowm 

myLat  =  5.1050
myLong =  -1.2427

myOwm = pyowm.OWM('788b6de43561e5e0cde2ef5041863aef')
locInfo = myOwm.weather_at_coords(myLat, myLong)


w = locInfo.get_weather()
l = locInfo.get_location()


print("Location : ", l, "\n")
print("Humidity : ",w.get_humidity(), "%")
print("Temperature : ", w.get_temperature(unit= 'celsius')['temp'], "celsius")
print("Wind Direction : ", w.get_wind()['deg'])
print("Wind speed : ", w.get_wind()['speed'])
