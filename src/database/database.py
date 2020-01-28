import os
import psycopg2
import logging
import sys

# global singleton connection
_connection = None


def connect():
    """ Connect to the PostgreSQL database server"""
    global _connection
    # if connection is already formed, return connection
    if _connection:
        return _connection

    try:
        # connect to the PostgreSQL server
        logging.info("Connecting to the PostgreSQL database...")
        _connection = psycopg2.connect(host=os.getenv("RC_DINING_BOT_HOST"),
                                       database=os.getenv("RC_DINING_BOT_DATABASE"),
                                       user=os.getenv("RC_DINING_BOT_DB_USER"),
                                       password=os.getenv("RC_DINING_BOT_DB_PASSWORD"),
                                       connect_timeout=10
                                       )

        # create a cursor
        cursor = _connection.cursor()

        # display the PostgreSQL database server version
        logging.info("PostgreSQL database version:")
        cursor.execute("SELECT version()")
        db_version = cursor.fetchone()
        logging.info(db_version)

        cursor.close()
    except Exception as error:
        logging.fatal(error)
        sys.exit(1)
