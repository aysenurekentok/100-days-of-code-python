from data_manager import DataManager
from flight_manager import FlightManager


sheety_data_list = DataManager().get_sheety_data()
for city in sheety_data_list:
    DataManager().find_iata_code(city)
    DataManager().update_iata(city)
    search = FlightManager().search_flight(city)
    FlightManager().find_cheaper(search, city)
