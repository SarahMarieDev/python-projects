import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.base_url = (
            "https://api.sheety.co/93ee438cd8c9e99f55862b9897a19e34/flightDeals/prices"
        )
        self.headers = {
            "Content-Type": "application/json"
        }
        
    def get_prices(self):
        response = requests.get(url=self.base_url, headers=self.headers)
        response.raise_for_status()
        return response.text