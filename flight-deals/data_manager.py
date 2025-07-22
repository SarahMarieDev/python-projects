import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/93ee438cd8c9e99f55862b9897a19e34/flightDeals/prices"

class DataManager:
    
    def __init__(self):
        TOKEN = os.getenv('FD_AUTH')
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": TOKEN
        }
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destinations_codes(self, row_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.base_url}/{row_id}", json=body, headers=self.headers)
        response.raise_for_status()
        