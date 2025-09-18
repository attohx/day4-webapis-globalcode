from dotenv import load_dotenv
import os
import requests
from pyowm.owm import OWM

load_dotenv()

api_key = os.getenv("API_KEY")

def weather_grabber():
    try: 

        owm = OWM(api_key)
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

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}. Please check your internet connection.")
    except KeyError as e:
        print(f"Missing data in the response: {e}. Please check the API response structure.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again later.")

location = str(input('Where are you located?: '))
weather_grabber()
