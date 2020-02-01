from util.const import (
    BREAKFAST,
    DINNER
)
from util.messages import no_menu_msg, menu_msg
from util.util import parse_menu
from database.database import get_menu, get_hidden_cuisines
from datetime import date


def handle_menu(meal):
    assert meal == BREAKFAST or meal == DINNER, "Meal input is incorrect."

    def get_breakfast_or_dinner_menu(update, context):
        # send the user menu
        menu = get_menu(meal, date.today())

        hidden_cuisines = get_hidden_cuisines(update.effective_chat.id)

        if menu is None:  # if no menu, reply with no menu message
            context.bot.send_message(chat_id=update.effective_chat.id, text=no_menu_msg(meal))
        else:  # else reply user of the menu
            menu = menu_msg(date.today(), meal, parse_menu(menu, hidden_cuisines))
            # send formatted menu to client
            update.message.reply_text(menu, parse_mode='HTML')

    return get_breakfast_or_dinner_menu
