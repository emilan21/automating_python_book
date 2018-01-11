#!/usr/bin/python3.5

# quick_weather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quick_weather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=e3db7950535161a4ce93f573462a5678' % (location)
response = requests.get(url)
response.raise_for_status()
# Load JSON data into a Python variable
weather_data = json.loads(response.text)

# Print weather descriptions.
w = weather_data['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])