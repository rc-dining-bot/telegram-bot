import os
import psycopg2
import logging
from dotenv import load_dotenv
load_dotenv()

# global singleton connection
_connection = None


def connect():
    """ Connect to the PostgreSQL database server"""
    global _connection
    if not _connection:
        try:
            # connect to the PostgreSQL server
            logging.info("Connecting to the PostgreSQL database...")
            _connection = psycopg2.connect(host="localhost",
                                           database="rc_meal_bot",
                                           user="postgres",
                                           password=os.getenv("DB_PASSWORD"))

            # create a cursor
            cur = _connection.cursor()

            # execute a statement
            logging.info("PostgreSQL database version:")
            cur.execute("SELECT version()")

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            logging.info(db_version)

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    return _connection
