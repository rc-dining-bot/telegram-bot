import os
import psycopg2
import logging
import sys

import psycopg2.extras

from database.queries import menu_query, settings_query, settings_insert, settings_update
from util.const import HIDE_CUISINE, FAVORITES

# global connection
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


def get_menu(meal, date):
    # get menu from database
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(menu_query(meal), (date,))
    menu = cursor.fetchone()
    cursor.close()
    return menu


def insert_default_user_pref(chat_id):
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(settings_insert(), (chat_id, '{}', '{}'))
    conn.commit()
    cursor.close()


def get_hidden_cuisines(chat_id):
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(settings_query(HIDE_CUISINE), (chat_id,))
    data = cursor.fetchone()

    if data is None:
        # insert default settings
        insert_default_user_pref(chat_id)
        hidden = []
    else:
        hidden = data[HIDE_CUISINE]

    cursor.close()
    return hidden  # returns hidden cuisines in user_pref


def update_hidden_cuisine(chat_id, cuisine_to_hide):
    hidden_cuisines = get_hidden_cuisines(chat_id)

    if cuisine_to_hide in hidden_cuisines:
        hidden_cuisines.remove(cuisine_to_hide)
    else:
        hidden_cuisines.append(cuisine_to_hide)

    # update database
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(settings_update(HIDE_CUISINE), (hidden_cuisines, chat_id))
    conn.commit()
    cursor.close()

    return hidden_cuisines


def get_favorite_foods(chat_id):
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(settings_query(FAVORITES), (chat_id,))
    data = cursor.fetchone()

    if data is None:
        insert_default_user_pref(chat_id)
        favorites = []
    else:
        favorites = data[FAVORITES]

    cursor.close()
    return favorites  # returns favorites in user_pref


def update_favorite_foods(chat_id, favorite_food, is_add=True):
    favorites = get_favorite_foods(chat_id)

    if favorite_food in favorites and is_add or favorite_food not in favorites and not is_add:
        return None
    elif favorite_food in favorites and not is_add:
        favorites.remove(favorite_food)
    else:
        favorites.append(favorite_food)

    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(settings_update(FAVORITES), (favorites, chat_id))
    conn.commit()
    cursor.close()

    return favorites
