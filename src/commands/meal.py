import logging

import telegram
from telegram.ext import run_async

from util.const import (
    BREAKFAST,
    DINNER
)
from util.messages import no_menu_msg, menu_msg, failed_to_parse_date_msg
from util.util import parse_menu, localized_date_today
from database.database import get_raw_menu, get_hidden_cuisines
from util.kb_mark_up import start_button_kb
from dateparser import parse


def handle_menu(meal):
    assert meal == BREAKFAST or meal == DINNER, "Meal input is incorrect."

    # in this function, parsed_date returns date in Singapore time. As such, no conversion is required.
    @run_async
    def get_breakfast_or_dinner_menu(update, context):
        chat_id = update.effective_chat.id
        # send the user menu
        entered_date = ''
        if update.callback_query is None:
            entered_date = ' '.join(context.args)
        parsed_date = get_menu_query_date(entered_date)

        if parsed_date is None:
            context.bot.send_message(chat_id=chat_id,
                                     text=failed_to_parse_date_msg(entered_date))
            return

        menu = get_raw_menu(meal, parsed_date)
        hidden_cuisines = get_hidden_cuisines(update.effective_chat.id)

        if menu is None:  # if no menu, reply with no menu message
            if update.callback_query is not None:
                context.bot.edit_message_text(chat_id=chat_id,
                                              message_id=update.callback_query.message.message_id,
                                              text=no_menu_msg(meal),
                                              reply_markup=start_button_kb())
            else:
                context.bot.send_message(chat_id=chat_id,
                                         text=no_menu_msg(meal),
                                         reply_markup=start_button_kb())

        else:  # else reply user of the menu
            menu = menu_msg(parsed_date, meal, parse_menu(menu, hidden_cuisines))
            # send formatted menu to client
            if update.callback_query is not None:
                context.bot.edit_message_text(chat_id=chat_id,
                                              message_id=update.callback_query.message.message_id,
                                              text=menu,
                                              parse_mode=telegram.ParseMode.HTML,
                                              reply_markup=start_button_kb())
            else:
                context.bot.send_message(chat_id=chat_id, text=menu,
                                         parse_mode=telegram.ParseMode.HTML, reply_markup=start_button_kb())
        logging.info(f"{chat_id}: {meal} menu sent to chat")

        if update.callback_query is not None:
            context.bot.answer_callback_query(update.callback_query.id)

    def get_menu_query_date(entered_date):
        if entered_date == '':
            return localized_date_today()

        parsed_date = parse(entered_date)
        if parsed_date is None:
            return None
        return parsed_date.date()

    return get_breakfast_or_dinner_menu
