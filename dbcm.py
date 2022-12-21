"""
Contains the DBCM class which is a context manager for databases.
"""
import logging
import sqlite3

class DBCM():
    """
    A database context manager which handles setup and teardown code.
    """

    logger = logging.getLogger("main." + __name__)

    def __init__(self, db_name):
        """
        Initializes the database context manager and stores the databases name.
        """
        try:
            self.db_name = db_name
            self.conn = sqlite3.connect(self.db_name)
        except Exception as exception:
            print("DBCM:__init__:", exception)
            self.logger.error("DBCM:__init__:%s", exception)

    def __enter__(self):
        """
        Connects to the database
        """
        try:
            return self.conn
        except Exception as exception:
            print("DBCM:__enter__:", exception)
            self.logger.error("DBCM:__enter__:%s", exception)
        return None

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        Closes the connection to the database
        """
        try:
            self.conn.close()
        except Exception as exception:
            print("DBCM:__exit__:", exception)
            self.logger.error("DBCM:__exit__:%s", exception)
