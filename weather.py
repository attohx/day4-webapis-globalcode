from pyowm.owm import OWM

location = str(input('Where are you located?: '))

API_KEY = "b92d4df77ac6623f9144d0f0d72d4630"

owm = OWM(API_KEY)
mgr = owm.weather_manager()

observation = mgr.weather_at_place(location)
w = observation.weather


forecast = mgr.forecast_at_place(location, '3h')
## answer = forecast.will_be_clear_at(timestamps.tomorrow())

winn = w.wind()
humi = w.humidity
cloudstat = w.detailed_status
temp = w.temperature('celsius')['temp']
## weatherf = forecastgh


print (f"Hi and welcome to the weather announcement for {location}")
print (f"The Humidity is at {humi}")
print (f"The Sky is filled with {cloudstat}")
print (f"The Temperature is at {temp}")
print (f"The Predicted forcast is {forecast}")


