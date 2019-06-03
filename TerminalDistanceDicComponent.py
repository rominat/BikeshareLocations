# -*- coding: utf-8 -*-
import sqlite3, csv, itertools
from haversine import haversine

bikeDB = sqlite3.connect("bikeshareDatabse.db")
my_dictionary = dict()


def upload_csv_specific_cols(file_path, col_included):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        cols_to_include = [col_included]
        content = list()
        for row in reader:
            content = content + list(row[i] for i in cols_to_include)
    final_content = content[1:]
    return final_content


def distance_calculator(location1, location2, unit):
    distance = -1
    if unit == "miles":
        distance = haversine(location1, location2, miles=True)
    elif unit == "kilometers":
        distance = haversine(location1, location2)
    return distance


def dictionary_creator(combinations_result):
    for i in combinations_result:
        first_tuple_value_terminalNumber = i[0]
        second_tuple_value_terminalNumber= i[1]
        dict_key = i

        db = sqlite3.connect("bikeshareDatabse.db")
        bikes_cursor = db.cursor()
        first_loc_queried = bikes_cursor.execute("SELECT LATITUDE, LONGITUDE FROM BikeLocations WHERE TERMINAL_NUMBER = (?)",(first_tuple_value_terminalNumber,))
        first_val = (first_loc_queried.fetchall())
        final_first_val = float((first_val[0])[0]), float((first_val[0])[1])

        second_loc_queried = bikes_cursor.execute("SELECT LATITUDE, LONGITUDE FROM BikeLocations WHERE TERMINAL_NUMBER = (?)",(second_tuple_value_terminalNumber,))
        second_val = second_loc_queried.fetchall()
        final_second_val = float((second_val[0])[0]),float((second_val[0])[1])

        dict_value = distance_calculator(final_first_val, final_second_val, "miles")
        my_dictionary[dict_key] = dict_value

    return my_dictionary


list_of_terminals = upload_csv_specific_cols("resources/Capital_Bike_Share_Locations.csv",3)
result = list(itertools.combinations(list_of_terminals, 2))

