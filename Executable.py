
import DatabaseComponent
import RecordLoaderComponent
import DistanceComponent
import TerminalDistanceDicComponent
import StationPullingComponent
import TripPullingComponent
import sqlite3, itertools


print("\n**** Readiness: Creating/Connecting to database ****")
def create_db(db_name):
    # initializes connection, creates db if it doesn't exist
    db = sqlite3.connect(db_name)
    print("Connected to db")
    return db


print("\n**** Executing DatabaseComponent functions: loading data ****")
#DatabaseComponent:
bikeDB = create_db("bikeshareDatabse.db")
bikeloc_table = DatabaseComponent.create_table(bikeDB)
bikeLocationList = DatabaseComponent.list_from_csv("resources/Capital_Bike_Share_Locations.csv") 
DatabaseComponent.load_list_into_table(bikeLocationList, bikeloc_table)

print("\n**** Executing RecordLoaderComponent functions: loading additional data ****")
#RecordLoaderComponent:
withTripsTableDB = RecordLoaderComponent.create_table(bikeDB)
completeList = RecordLoaderComponent.load_all_files("resources/Capital_BikeShare_Data") 
RecordLoaderComponent.load_list_into_table(completeList, withTripsTableDB)

print("\n**** Executing DistanceComponent functions: ****")
#DistanceComponent:
a = (45.0293, 4.9384)
b = (38.1634, 3.9245)
DistanceComponent.distance_calculator(a, b, "miles")
DistanceComponent.distance_calculator(a, b, "kilometers")

print("\n****Executing TerminalDistanceDicComponent functions: ****")
#TerminalDistanceDicComponent:
list_of_terminals = TerminalDistanceDicComponent.upload_csv_specific_cols("resources/Capital_Bike_Share_Locations.csv",3) 
result = list(itertools.combinations(list_of_terminals, 2))
my_dictionary = TerminalDistanceDicComponent.dictionary_creator(result)

print("\n****Executing StationPullingComponent functions: ****")
#StationPullingComponent:
print (StationPullingComponent.find_nearby_stations(my_dictionary,"31913", 9.2))

print("\n****Executing TripPullingComponent functions: ****")
#TripPullingComponent:
TripPullingComponent.amount_trips_calculator("31312","31214","2014-10-01 00:00:00","2014-10-01 00:10:00")
TripPullingComponent.amount_trips_calculator("31401","31600","2011-09-30 23:59:00","2011-10-01 00:15:00")