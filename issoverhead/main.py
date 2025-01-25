import requests
from datetime import datetime
import smtplib

MY_LAT = 45.180523
MY_LNG = -89.683456



response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.
delta_lat = abs(MY_LAT - iss_latitude)
delta_long = abs(MY_LNG - iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "America/Chicago"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

current_hour = datetime.now().hour


if delta_lat <= 5 and delta_long <= 5:
    if current_hour > sunset and current_hour < sunrise:
        send_email()

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



