import psycopg2.extras
from src.util.formatting import bold, italicize
from src.util.const import HIDE_CUISINE
from src.database.database import connect
from src.database.queries import settings_query, settings_insert, settings_update


def parse_menu(data):
    menu = ''
    for key in data.keys():
        if key == 'date':
            continue
        menu += bold(key.capitalize()) + '\n'
        for item in data[key]:
            if item == 'OR':
                menu += italicize(item) + '\n'
            else:
                menu += item + '\n'
        menu += '\n'
    return menu


def parse_callback(data):
    split_data = data.split('.')
    return split_data[0], split_data[1]


def get_hidden_cuisines(chat_id):
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(settings_query(HIDE_CUISINE), (chat_id,))
    data = cursor.fetchone()

    if data is None:
        # insert default settings
        cursor.execute(settings_insert(), (chat_id, '{}', '{}'))
        cursor.execute(settings_query(HIDE_CUISINE), (chat_id,))
        data = cursor.fetchone()

    return data[0]


def hide_cuisine(chat_id, cuisine_to_hide):
    hidden_cuisines = get_hidden_cuisines(chat_id)
    print(cuisine_to_hide)
    print(hidden_cuisines)
    if cuisine_to_hide in hidden_cuisines:
        hidden_cuisines.remove(cuisine_to_hide)
    else:
        hidden_cuisines.append(cuisine_to_hide)
    print(cuisine_to_hide)
    print(hidden_cuisines)
    conn = connect()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(settings_update(HIDE_CUISINE), (hidden_cuisines, chat_id))
    cursor.execute(settings_query(HIDE_CUISINE), (chat_id,))
    data = cursor.fetchone()

    print(data[0])
    return data[0]
