#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_prices()


flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"]:
        pass
    else:
        row["iataCode"] = flight_search.get_iata_code(row["city"])
 
print(sheet_data)

for row in sheet_data:
    data_manager.update_iata_code(row["id"], row["iataCode"])
    
print("Sheet update complete")