import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("../../EnvVar/.env.txt")

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
OWM_api_key = os.getenv("OWM_API_KEY")

parameters = {
    "lat": 41.013000,
    "lon": 28.974800,
    "exclude": "current,minutely,daily",
    "appid": OWM_api_key
}

url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url, params=parameters)
response.raise_for_status()

# Getting the next 12 hours weather data
hourly_weather = response.json()["hourly"]
next_12_hours = hourly_weather[:12]

rain = False

# Checking if it's going to rain in the next 12 hours
for weather in next_12_hours:
    id = weather["weather"][0]["id"]
    # In weather condition codes below 700 is all rain, snow and thunderstorm
    if id < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget to take your umbrella.",
        from_='+15038095584',
        to='+905438576254'
        )

    print(message.status)
