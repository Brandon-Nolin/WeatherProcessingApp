"""
Contains the DBOperations class which contains functions for handling database operations.
"""
import logging
from dbcm import DBCM

class DBOperations():
    """
    Contains methods to handle database operations, such as initializing table,
    saving data, purging data, and fetching data.
    """

    logger = logging.getLogger("main." + __name__)

    def __init__(self, db_name):
        """
        Initializes the DBOperations object with a given database name.
        """

        try:
            self.db_name = db_name
        except Exception as exception:
            print("DBOperations:__init__:", exception)
            self.logger.error("DBOperations:__init__:%s", exception)

    def initialize_db(self):
        """
        Initializes the database table if it hasnt already been created
        """
        try:
            with DBCM(self.db_name) as database:
                database.cursor().execute("""create table Weather(id integer primary key autoincrement not null,
                                    sample_date text not null unique,
                                    location text not null,
                                    min_temp real not null,
                                    max_temp real not null,
                                    avg_temp real not null);""")
                database.commit()
        except Exception as exception:
            print("DBOperations:initialize_db:", exception)
            self.logger.error("DBOperations:initialize_db:%s", exception)

    def fetch_data(self, start_date, end_date):
        """
        Fetches all data in a given date range.
        """
        try:
            data = {}
            with DBCM(self.db_name) as database:
                for row in database.cursor().execute("SELECT * FROM Weather WHERE sample_date BETWEEN '" + start_date + "' AND '" + end_date + "';"):
                    try:
                        data[row[1]] = {"min_temp" : row[3], "max_temp" :
                        row[4], "avg_temp" : row[5]}
                    except Exception as exception:
                        print("DBOperations:fetch_data::loop:", exception)
                        self.logger.error("DBOperations:fetch_data::loop:%s", exception)

            return data
        except Exception as exception:
            print("DBOperations:fetch_data:", exception)
            self.logger.error("DBOperations:fetch_data:%s", exception)

        return None

    def purge_data(self):
        """
        Removes all rows from the database.
        """
        try:
            with DBCM(self.db_name) as database:
                database.cursor().execute("DELETE FROM Weather;")
                database.commit()
        except Exception as exception:
            print("DBOperations:purge_data:", exception)
            self.logger.error("DBOperations:purge_data:%s", exception)

    def save_data(self, data):
        """
        Inserts data into the database.
        """

        self.initialize_db()

        try:
            with DBCM(self.db_name) as database:
                cur = database.cursor()

                for row, temps in data.items():
                    try:
                        data = (row, "Winnipeg, MB", temps["min_temp"],
                        temps["max_temp"], temps["avg_temp"])
                        sql = """INSERT OR IGNORE INTO Weather (sample_date, location, min_temp,
                        max_temp, avg_temp) values (?, ?, ?, ?, ?);"""

                        cur.execute(sql, data)
                    except Exception as exception:
                        print("DBOperations:save_data:loop:", exception)
                        self.logger.error("DBOperations:save_data:loop:%s", exception)
                database.commit()
        except Exception as exception:
            print("DBOperations:save_data:", exception)
            self.logger.error("DBOperations:save_data:%s", exception)

    def fetch_last_date(self):
        """
        Retrieves that last date of temperatures recorded
        """
        try:
            last_date = ""

            with DBCM(self.db_name) as database:
                for row in database.cursor().execute("SELECT MAX(sample_date) FROM Weather;"):
                    last_date = row[0]

            return last_date
        except Exception as exception:
            print("DBOperations:fetch_last_date:", exception)
            self.logger.error("DBOperations:fetch_last_date:%s", exception)
