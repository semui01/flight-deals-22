# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from datetime import datetime,timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search =FlightSearch()
notification_manager=NotificationManager()

ORIGIN_CITY_IATA ='SIN'

if sheet_data[0]["iataCode"] == " ":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_code(city_names)
    sheet_data =data_manager.get_destination_data()
    data_manager.update_destination_codes()

today = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_email(message=f"Subject: Low price alert\n\nLow price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date} with{flight.airlines}{flight.flight_no}."
                )