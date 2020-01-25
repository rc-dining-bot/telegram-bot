from src.util.const import (
    BREAKFAST, BREAKFAST_TEMPLATE,
    DINNER_TEMPLATE
)
from src.util.util import parse_menu
from src.database import connect
from src.util.const import NO_MENU_MSG
import psycopg2.extras
from datetime import date


def handle_menu(meal):
    def inner(update, context):
        """Send the user menu"""
        # get menu from database
        conn = connect()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(f"SELECT * FROM {meal} WHERE date = %s;", (date.today(),))
        data = cur.fetchone()

        if data is None:  # if no menu, reply with no menu message
            update.message.reply_text(NO_MENU_MSG)
        else:             # else reply user of the menu
            template = BREAKFAST_TEMPLATE if meal == BREAKFAST else DINNER_TEMPLATE
            menu = parse_menu(template, data)
            # send formatted menu to client
            update.message.reply_text(menu, parse_mode='HTML')
    return inner
