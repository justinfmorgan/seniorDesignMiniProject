from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = 'b02385562c9b4596d5871527fd18508e'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&mode=json&units=metric&appid={}')

def query_api(lat, lon):
    try:
        print(API_URL.format(lat, lon, API_KEY))
        data = requests.get(API_URL.format(lat, lon, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data