import sqlite3


def amount_trips_calculator(station1, station2, date1, date2):

    db = sqlite3.connect("bikeshareDatabse.db")
    bikes_cursor = db.cursor()
    filtering_query = bikes_cursor.execute("SELECT * FROM BikeTrips WHERE START_STATION = ? and STOP_STATION =? and START_DATE=? and STOP_DATE= ?", (station1, station2, date1, date2),)
    result = filtering_query.fetchall()
    print(len(result))
