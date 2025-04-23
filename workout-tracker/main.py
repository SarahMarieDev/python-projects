import requests
import os
from dotenv import load_dotenv
from datetime import *

load_dotenv()

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')

base_url = "https://trackapi.nutritionix.com"
exercise_endpoint = "/v2/natural/exercise"

user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

request_body = {
    "query": user_input
}


response = requests.post(url=f"{base_url}{exercise_endpoint}", json=request_body, headers=headers)
print(response.text)