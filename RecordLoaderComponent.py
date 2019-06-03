import sqlite3, csv, os


def create_db(db_name):
    # initializes connection, creates db if it doesn't exist
    db = sqlite3.connect(db_name)
    print("Connected to db")
    return db


def create_table(db):
    # db.execute("DROP TABLE BikeTrips;")
    trips_table_maker = """CREATE TABLE IF NOT EXISTS BikeTrips(
                        TRIP_DURATION text,
                        START_DATE text,
                        START_STATION text,
                        STOP_DATE text,
                        STOP_STATION text,
                        BIKE_ID text,
                        USER_TYPE text)"""
    bikes_cursor = db.cursor()
    bikes_cursor.execute(trips_table_maker)
    db.commit()
    return db

def load_all_files(path):
    comprehensive_list = list()
    directory = os.path.join(path)
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                path_to_file = path + "/" + file
                with open(path_to_file, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    bike_list = list(reader)
                    tuple_list = [tuple(l) for l in bike_list]
                    prelim_list = tuple_list[1:]
                    print("Adding: %d records to database" % len(prelim_list))
                    comprehensive_list = comprehensive_list + prelim_list #this keeps adding records of prelim_list to comprehensive_list
                    #comprehensive_list = comprehensive_list.append(prelim_list) this keeps adding the prelim_list(tuples) into another list
                    #print("total records so far: %d" % len(comprehensive_list))
                    csv_file.close()
    return comprehensive_list


def load_list_into_table(list, db):
    bikes_cursor = db.cursor()
    bikes_cursor.executemany("""INSERT INTO BikeTrips(TRIP_DURATION, START_DATE, START_STATION, STOP_DATE,
                        STOP_STATION, BIKE_ID, USER_TYPE) VALUES(?,?,?,?,?,?,?);""", list)
    print ("Number of records entered in Database: %d" % bikes_cursor.rowcount)
    db.commit()

