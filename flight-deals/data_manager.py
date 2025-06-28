import requests
import os
import json
from dotenv import load_dotenv
from datetime import *

load_dotenv()

TOKEN = os.getenv('FLIGHT_DEALS_TOKEN')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    base_url = "https://api.sheety.co/93ee438cd8c9e99f55862b9897a19e34/flightDeals/prices"
    
    sheety_headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.get(url=base_url, headers=sheety_headers)
    print(response.text)