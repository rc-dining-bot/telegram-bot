import json
import os.path
from util.const import (
    BREAKFAST, BREAKFAST_TEMPLATE,
    DINNER, DINNER_TEMPLATE
)
from util.util import parse_menu
from database import connect
import psycopg2.extras


def breakfast(update, context):
    """Send the user breakfast menu"""
    with open(os.path.dirname(__file__) + '/../mock/breakfast.json', 'r') as bf:
        data = json.load(bf)
    menu = parse_menu(data)
    update.message.reply_text(menu, parse_mode='HTML')


def dinner(update, context):
    """Send the user dinner menu"""
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM menu")
    menu = parse_menu(DINNER_TEMPLATE, cur.fetchone())
    print(menu)
    update.message.reply_text(menu, parse_mode='HTML')
