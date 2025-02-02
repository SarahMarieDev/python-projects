import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get('OWM_API_KEY')
my_lat = 45.180809
my_long = -89.683159
account_sid = os.environ.get('TWILIO_ACCT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

weather_params = {
    "lat": 44.389072,
    "lon": -114.659375,
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Remember to bring an ☔️",
        to='whatsapp:+17153489399'
    )
    print(message.status)


