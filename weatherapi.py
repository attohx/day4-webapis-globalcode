from pprint import pprint
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={api_key}')
pprint(r.text)
