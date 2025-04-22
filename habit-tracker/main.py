import requests
import os
from dotenv import load_dotenv
from datetime import *

load_dotenv()

USERNAME = "sarahmarie"
TOKEN = os.getenv('PIXELA_TOKEN')
STEPS_GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_endpoint = f"https://pixe.la/@{USERNAME}"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{STEPS_GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_profile_params = {
    "timezone": "CST"
}


graph_config = {
    "id": STEPS_GRAPH_ID,
    "name": "Steps Graph",
    "unit": "steps",
    "type": "int",
    "color": "sora"
}

today = datetime.now().strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": input("How many steps did you take today? ")
}

## Create user
# response = requests.post(url=pixela_endpoint, json=user_params)

## Change token
# update_params = {
#     "newToken": TOKEN
# }
# response = requests.put(url=f'{pixela_endpoint}/{USERNAME}', headers=headers, json=update_params)

## Update user timezone
#response = requests.put(url=user_endpoint, json=user_profile_params, headers=headers)

## Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

## Update a graph
# response = requests.put(url=f"{graph_endpoint}/{STEPS_GRAPH_ID}", json=graph_config, headers=headers)

## Post a pixel
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

# Update/delete a pixel
#response = requests.delete(url=f"{pixel_endpoint}/20250420", headers=headers)

print(response.text)
