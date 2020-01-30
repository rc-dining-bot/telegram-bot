from util.messages import settings_msg
from util.kb_mark_up import settings_kb, hidden_cuisine_kb
from util.util import parse_callback
from database.database import get_hidden_cuisines, update_hidden_cuisine
from util.messages import no_hidden_cuisine_msg, hidden_cuisine_msg


def handle_settings(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=settings_msg(), reply_markup=settings_kb())


def handle_hidden_cuisine(update, context):
    hidden_cuisine = get_hidden_cuisines(update.effective_chat.id)
    msg = no_hidden_cuisine_msg() if not hidden_cuisine else hidden_cuisine_msg(update.effective_chat.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, reply_markup=hidden_cuisine_kb(hidden_cuisine))


def handle_hide_cuisine(update, context):
    cuisine_to_hide = parse_callback(update.callback_query.data)[1]
    updated_hidden_cuisine = update_hidden_cuisine(update.effective_chat.id, cuisine_to_hide)
    update.callback_query.edit_message_reply_markup(reply_markup=hidden_cuisine_kb(updated_hidden_cuisine))
