import requests
import os
import json
from dotenv import load_dotenv
from datetime import *

load_dotenv()

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')

base_url = "https://trackapi.nutritionix.com"
exercise_endpoint = "/v2/natural/exercise"

#user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

request_body = {
    "query": "I ran 5k and cycled 30 min"
}


response = requests.post(url=f"{base_url}{exercise_endpoint}", json=request_body, headers=headers)

exercise_data = json.loads(response.text)
print(json.dumps(exercise_data, indent=2))

sheety_url = "https://api.sheety.co/93ee438cd8c9e99f55862b9897a19e34/workoutTracking/workouts"

sheety_headers = {
    "Content-Type": "application/json"
}

current_date = datetime.now().strftime("%m/%d/%Y")
current_time = datetime.now().strftime("%X")

for exercise in exercise_data["exercises"]:
    exercise_name = f"{exercise['name']}".title()
    duration = f"{exercise['duration_min']}"
    calories = f"{exercise['nf_calories']}"
    
    row_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }
    
    response = requests.post(url=f"{sheety_url}", json=row_params, headers=sheety_headers)
    print(response.text)
    
    


