import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    load_dotenv()

    USERNAME = os.getenv('FD_USER')
    PASSWORD = os.getenv('FD_PASS')
    
    def __init__(self):
        self.base_url = (
            "https://api.sheety.co/93ee438cd8c9e99f55862b9897a19e34/flightDeals/prices"
        )
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic c2FyYWhtYXJpZWRldjpMZXhpJk5hbm8xOTg2"
        }
        
    def get_prices(self):
        response = requests.get(url=self.base_url, headers=self.headers)
        response.raise_for_status()
        return response.json().get("prices", [])
    
    def update_iata_code(self, row_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.base_url}/{row_id}", json=body, headers=self.headers)
        response.raise_for_status()
        