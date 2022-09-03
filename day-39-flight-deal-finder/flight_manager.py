import datetime as dt
import requests
from sms_manager import SmsManager

API_ENDPOINT = "https://tequila-api.kiwi.com/"

location_header = {
    "apikey": "CZKVTo6K8c9gWjbBu0v9wFLRgnDHt-0M"
}


class FlightManager:

    def __init__(self):
        self.date = dt.date.today() + dt.timedelta(days=1)
        self.tomorrow = self.date.strftime("%d/%m/%Y")
        self.date2 = dt.date.today() + dt.timedelta(days=180)
        self.six_months_later = self.date2.strftime("%d/%m/%Y")

    def search_flight(self, c):
        c_list = []
        search_query = {
            "fly_from": "LON",
            "fly_to": c["iataCode"],
            "date_from": self.tomorrow,
            "date_to": self.six_months_later,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        response = requests.get(url=f"{API_ENDPOINT}v2/search", params=search_query, headers=location_header)
        result = response.json()["data"]
        for item in result:
            c_list.append(item)
        return c_list

    def find_cheaper(self, search_result, c):
        for item in search_result:
            if item["price"] < c["lowestPrice"]:
                SmsManager().send_sms(search_result)
