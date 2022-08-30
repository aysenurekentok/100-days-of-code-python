import requests
from twilio.rest import Client

account_sid = "AC7f9edd29a4222509228fd33097692275"
auth_token = "0fe96b5d446744aac5bccd6263f1a312"

parameters = {
    "lat": 41.013000,
    "lon": 28.974800,
    "exclude": "current,minutely,daily",
    "appid": "69f04e4613056b159c2761a9d9e664d2"
}

url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url, params=parameters)
response.raise_for_status()

hourly_weather = response.json()["hourly"]
next_12_hours = hourly_weather[:12]

rain = False

for weather in next_12_hours:
    id = weather["weather"][0]["id"]
    if id < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget to take your umbrella.",
        from_='+15038095584',
        to=''
        )

    print(message.status)
