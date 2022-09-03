import requests

SHEETY_API_ENDPOINT = "https://api.sheety.co/6258a68c32d814c078e411077b77a2fd/flightDeals/prices"
API_ENDPOINT = "https://tequila-api.kiwi.com/"

location_header = {
    "apikey": "CZKVTo6K8c9gWjbBu0v9wFLRgnDHt-0M"
}


class DataManager:

    def __init__(self):
        self.get_sheety_data()

    def get_sheety_data(self):
        response = requests.get(SHEETY_API_ENDPOINT)
        data = response.json()["prices"]
        return data

    def find_iata_code(self, city):
        locations_query = {
            "term": city["city"],
            "location_types": "city",
            "limit": 1
        }
        response = requests.get(f"{API_ENDPOINT}locations/query", params=locations_query, headers=location_header)
        location_data = response.json()
        city["iataCode"] = location_data["locations"][0]["code"]

    def update_iata(self, row):
        sheety_iata_code = {
            "price": {
                "iataCode": f"{row['iataCode']}"
            }
        }
        requests.put(url=f"{SHEETY_API_ENDPOINT}/{row['id']}", json=sheety_iata_code)
