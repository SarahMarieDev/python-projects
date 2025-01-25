import requests
import smtplib
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

MY_LAT = 45.180523
MY_LNG = -89.683456
EMAIL = os.getenv('GMAIL')
PASSWORD = os.getenv('PASSWORD')

def send_email():
    global EMAIL, PASSWORD
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="sarahmarie73@gmail.com",
            msg="Subject:ISS is overhead\n\nLook up!"
        )


def is_iss_overhead():
    global MY_LAT, MY_LNG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    delta_lat = abs(MY_LAT - iss_latitude)
    delta_long = abs(MY_LNG - iss_longitude)

    if delta_lat <= 5 and delta_long <= 5:
        return True


def is_night():
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

    if current_hour > sunset or current_hour < sunrise:
        return True


if is_iss_overhead() and is_night():
    send_email()

# BONUS: run the code every 60 seconds.
