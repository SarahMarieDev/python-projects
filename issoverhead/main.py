import requests
import smtplib
import os
from datetime import datetime
from dotenv import load_dotenv


MY_LAT = 45.180523
MY_LNG = -89.683456

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
email = os.getenv('GMAIL')
password = os.getenv('PASSWORD')

def send_email(email, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="sarahmarie73@gmail.com",
            msg="Subject:ISS is overhead\n\nLook up!"
        )

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
#print(iss_latitude, iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.

# testing
# MY_LAT = iss_latitude
# MY_LNG = iss_longitude

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

# testing
# sunrise = 7
# sunset = 12


if delta_lat <= 5 and delta_long <= 5:
    if current_hour > sunset or current_hour < sunrise:
        send_email(email, password)

# BONUS: run the code every 60 seconds.



