import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv("../../EnvVar/.env.txt")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/6258a68c32d814c078e411077b77a2fd/myWorkouts/workouts"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")

NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}

SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

nutritionix_required = {
    "query": input("Today's exercises: "),
    "gender": "female",
    "weight_kg": 48,
    "height_cm": 161,
    "age": 25
}

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_required, headers=NUTRITIONIX_HEADERS)
nutritionix_response.raise_for_status()
result_list = nutritionix_response.json()["exercises"]

for result in result_list:
    sheety_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"]
        }
    }
    sheety_response = requests.post(SHEETY_URL, json=sheety_config, headers=SHEETY_HEADERS)
    print(sheety_response.text)
