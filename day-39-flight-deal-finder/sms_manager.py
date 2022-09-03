from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("../../EnvVar/.env.txt")


class SmsManager:

    def __init__(self):
        self.account_sid = os.getenv("ACCOUNT_SID")
        self.auth_token = os.getenv("AUTH_TOKEN")

    def send_sms(self, flight_data):
        for flight in flight_data:
            city_to = flight['cityTo']
            city_from = flight['cityFrom']
            airport_to = flight['cityCodeTo']
            airport_from = flight['cityCodeFrom']
            departure_date = flight['utc_departure'].split('T')[0]
            arrival_date = flight['utc_arrival'].split('T')[0]
            flight_price = flight['price']
            flight_link = flight['deep_link']

            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                body=f"Low price alert! Only ${flight_price} to fly from {city_from}-{airport_from} "
                     f"to {city_to}-{airport_to},\n\nfrom {departure_date} to {arrival_date}.\n\n "
                     f"Check out the offer now {flight_link}",
                from_='+15038095584',
                to=os.getenv("MY_NUMBER")
            )
            print(message.status)
