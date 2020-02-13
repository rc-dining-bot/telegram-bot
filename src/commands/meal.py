from util.const import (
    BREAKFAST,
    DINNER
)
from util.messages import no_menu_msg, menu_msg, failed_to_parse_date_msg
from util.util import parse_menu
from database.database import get_raw_menu, get_hidden_cuisines
from util.kb_mark_up import start_button_kb
from datetime import date
from dateparser import parse


def handle_menu(meal):
    assert meal == BREAKFAST or meal == DINNER, "Meal input is incorrect."

    def get_breakfast_or_dinner_menu(update, context):
        # send the user menu
        entered_date = ' '.join(context.args)
        parsed_date = get_menu_query_date(entered_date)

        if parsed_date is None:
            update.message.reply_text(text=failed_to_parse_date_msg(entered_date))
            return

        menu = get_raw_menu(meal, parsed_date)
        hidden_cuisines = get_hidden_cuisines(update.effective_chat.id)

        print(menu)
        print(menu.keys())
        if menu is None:  # if no menu, reply with no menu message
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=no_menu_msg(meal),
                                     reply_markup=start_button_kb())
        else:  # else reply user of the menu
            print(menu.keys())
            print(menu)
            menu = menu_msg(parsed_date, meal, parse_menu(menu, hidden_cuisines))
            print(menu)
            # send formatted menu to client
            update.message.reply_text(text=menu,
                                      parse_mode='HTML')

    def get_menu_query_date(entered_date):
        if entered_date == '':
            return date.today()

        parsed_date = parse(entered_date)
        if parsed_date is None:
            return None
        return parsed_date.date()

    return get_breakfast_or_dinner_menu
