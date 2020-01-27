from src.util.const import (
    BREAKFAST,
    DINNER
)
from src.util.messages import no_menu_msg, menu_msg
from src.util.util import parse_menu
from src.database.database import connect
from src.database.queries import menu_query
import psycopg2.extras
from datetime import date


def handle_menu(meal):
    assert meal == BREAKFAST or meal == DINNER, "Meal input is incorrect."

    def get_breakfast_or_dinner_menu(update, context):
        """Send the user menu"""
        # get menu from database
        conn = connect()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(menu_query(meal), (date.today(),))
        data = cur.fetchone()

        if data is None:  # if no menu, reply with no menu message
            update.message.reply_text(no_menu_msg(meal))
        else:  # else reply user of the menu
            menu = menu_msg(date.today(), meal, parse_menu(data))
            # send formatted menu to client
            update.message.reply_text(menu, parse_mode='HTML')

    return get_breakfast_or_dinner_menu
