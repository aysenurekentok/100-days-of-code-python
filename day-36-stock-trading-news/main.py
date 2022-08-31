import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("../../EnvVar/.env.txt")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = os.getenv("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("AUTH_TOKEN")

NEWS_API = os.getenv("NEWSAPI_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_PARAMS = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME
}

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
# Creating a list of closing numbers for every day
daily_list = [value["4. close"] for (key, value) in stock_data.items()]

# Closing prices for yesterday and day before yesterday
yesterday = float(daily_list[0])
day_before = float(daily_list[1])

percentage = abs(yesterday - day_before) / yesterday * 100

# If difference percentage is greater than 5 get articles related to the COMPANY_NAME
if percentage >= 5:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()
    # Slicing the list so that we can get the first 3 articles
    news_articles = news_data["articles"][:3]

    formatted_list = [f"Title: {article['title']}.\nDescription: {article['description']}.\n" for article in news_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_list:

        message = client.messages \
            .create(
            body=article,
            from_='+15038095584',
            to=''
            )

        print(message.status)
