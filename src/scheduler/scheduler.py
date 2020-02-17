import os
from datetime import date
import logging

from database.database import (
    get_broadcast_subscribers,
    get_raw_menu,
    get_hidden_cuisines
)
from scheduler.scheduler_config import BREAKFAST_BROADCAST_TIME, DINNER_BROADCAST_TIME
from util.const import BREAKFAST, DINNER
from util.messages import menu_msg
from util.util import parse_menu, localized_date_today


def scheduler(job_queue):
    # schedule breakfast and dinner broadcasts

    job_queue.run_daily(callback=meal_broadcast(BREAKFAST),
                        time=BREAKFAST_BROADCAST_TIME)
    job_queue.run_daily(callback=meal_broadcast(DINNER),
                        time=DINNER_BROADCAST_TIME)


# meal broadcast function
def meal_broadcast(meal):
    def send_menu(context):
        # get menu today
        menu = get_raw_menu(meal, localized_date_today())

        if menu is None:
            return

        # get the subscribers before the broadcast
        subscribers = get_broadcast_subscribers(meal)

        logging.info("meal broadcast in progress")

        for user_id in subscribers:
            chat_id = user_id[0]  # extracts chat_id from nested [] from database
            hidden_cuisines = get_hidden_cuisines(chat_id)
            context.bot.send_message(chat_id=chat_id,
                                     text=menu_msg(date.today(),
                                                   meal,
                                                   parse_menu(menu, hidden_cuisines)),
                                     parse_mode='HTML')

        logging.info("meal broadcast finished")

    return send_menu
