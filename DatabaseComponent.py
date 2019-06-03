import csv
def create_table(db):
    # db.execute("DROP TABLE BikeLocations;")
    bikeloc_table_maker = """CREATE TABLE IF NOT EXISTS BikeLocations(
                        OBJECTID text,
                        ID text,
                        ADDRESS text,
                        TERMINAL_NUMBER text,
                        LATITUDE text,
                        LONGITUDE text,
                        INSTALLED text,
                        LOCKED text,
                        INSTALL_DATE text,
                        REMOVAL_DATE text,
                        TEMPORARY_INSTALL text,
                        NUMBER_OF_BIKES text,
                        NUMBER_OF_EMPTY_DOCKS text,
                        X text,
                        Y text,
                        SE_ANNO_CAD_DATA text)"""
    bikes_cursor = db.cursor()
    bikes_cursor.execute(bikeloc_table_maker)
    db.commit()
    return db


def list_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        bike_list = list(reader)
        tuple_list = [tuple(l) for l in bike_list]
    return tuple_list[1:]


def load_list_into_table(list_to_load, db):
    bikes_cursor = db.cursor()
    bikes_cursor.executemany("""INSERT INTO BikeLocations(OBJECTID, ID, ADDRESS, TERMINAL_NUMBER,
                        LATITUDE, LONGITUDE, INSTALLED, LOCKED, INSTALL_DATE, REMOVAL_DATE,
                        TEMPORARY_INSTALL, NUMBER_OF_BIKES, NUMBER_OF_EMPTY_DOCKS,
                        X, Y, SE_ANNO_CAD_DATA) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", list_to_load)
    print ("Number of records entered in Database: %d" % bikes_cursor.rowcount)
    db.commit()

