# -*- coding: utf-8 -*-
from haversine import haversine


def distance_calculator(location1, location2, unit):
    distance = -1
    if unit == "miles":
        distance = haversine(location1,location2,miles=True)
        print ("Distance in miles between" ,location1,  "and" ,location2, "= %.2f" %distance, "miles" )
    elif unit == "kilometers":
        distance = haversine(location1, location2)
        print("Distance in kilometers between",location1,"and",location2, "= %.2f" %distance, "km")
    else:
        print("Error, unit is not valid - distance returned will be -1")
    return distance



