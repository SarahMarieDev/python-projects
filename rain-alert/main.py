import requests
import json

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "221fa2ea7381120da8cbd10ab2c16889"
my_lat = 45.180809
my_long = -89.683159

weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
