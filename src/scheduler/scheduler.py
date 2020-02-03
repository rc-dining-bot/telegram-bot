from datetime import date

import schedule

from database.database import (
    get_broadcast_subscribers,
    get_raw_menu,
    get_hidden_cuisines
)
from scheduler.scheduler_config import BREAKFAST_BROADCAST_TIME, DINNER_BROADCAST_TIME
from util.const import BREAKFAST, DINNER
from util.messages import menu_msg
from util.util import parse_menu


def scheduler(bot):
    breakfast_subscribers = get_broadcast_subscribers(BREAKFAST)
    dinner_subscribers = get_broadcast_subscribers(DINNER)

    # schedule breakfast and dinner broadcasts
    schedule.every().day\
        .at(BREAKFAST_BROADCAST_TIME)\
        .do(broadcast(BREAKFAST, bot, breakfast_subscribers))
    schedule.every().day\
        .at(DINNER_BROADCAST_TIME)\
        .do(broadcast(DINNER, bot, dinner_subscribers))


def broadcast(meal, bot, subscribers):
    menu = get_raw_menu(meal, date.today())

    if menu is None:
        return do_nothing

    def send_menu():
        for user_id in subscribers:
            hidden_cuisines = get_hidden_cuisines(user_id)
            bot.send_message(user_id,
                             menu_msg(date.today(),
                                      meal,
                                      parse_menu(menu, hidden_cuisines)),
                             parse_mode='HTML')

    return send_menu


def do_nothing():
    return
