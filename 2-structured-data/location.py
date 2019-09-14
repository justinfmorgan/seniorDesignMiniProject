from datetime import datetime
import os
import pytz
import requests
import math
import json
import uuid

API_KEY = 'AIzaSyDzVaKkWBGoCnwxjoeg_ifZ3dUfowZlQAQ'
API_URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDzVaKkWBGoCnwxjoeg_ifZ3dUfowZlQAQ'

# after each 2 digits, join elements of getnode().
macAddress = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))

#print(str(macAddress))
payload =         {
  "considerIp": "false",
  "wifiAccessPoints": [
    {
        "macAddress": "00:25:9c:cf:1c:ac",
        "signalStrength": -43,
        "signalToNoiseRatio": 0
    },
    {
        "macAddress": "00:25:9c:cf:1c:ad",
        "signalStrength": -55,
        "signalToNoiseRatio": 0
    }
  ],
  'key': API_KEY
}

r = requests.post(API_URL, json=payload)

data = (json.loads(r.text))

myLat = float(data['location']['lat'])
myLon = float(data['location']['lng'])

#print("MY COORDS ARE: " + str(myLat) + str(myLon) + "\n")

def query_location():
    #print(r.text)
    return (myLat, myLon)