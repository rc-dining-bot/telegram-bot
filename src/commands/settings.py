from util.messages import settings_msg
from util.kb_mark_up import settings_kb, hidden_cuisine_kb, favorites_kb
from util.util import parse_callback
from database.database import get_hidden_cuisines, update_hidden_cuisine, get_favorite_foods, update_favorite_foods
from util.messages import (no_hidden_cuisine_msg, hidden_cuisine_msg, add_favorite_no_input_msg,
                           add_favorite_already_exists_msg, added_favorites_msg, no_favorites_msg, favorites_msg)
from util.formatting import normalize
import logging


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


def handle_add_favorite(update, context):
    food_to_add = ' '.join(context.args)
    if food_to_add == '':
        update.message.reply_text(add_favorite_no_input_msg())
        return

    food_to_add = normalize(food_to_add)
    favorites = update_favorite_foods(update.effective_chat.id, food_to_add)

    if favorites is None:
        update.message.reply_text(add_favorite_already_exists_msg())
        return

    update.message.reply_text(added_favorites_msg(favorites))


def handle_remove_favorite(update, context):
    favorites = get_favorite_foods(update.effective_chat.id)
    if len(favorites) == 0:
        update.message.reply_text(no_favorites_msg())
        return

    update.message.reply_text('Select your favorite food to remove:', reply_markup=favorites_kb(favorites))


def handle_remove_favorite_callback(update, context):
    food_to_remove = parse_callback(update.callback_query.data)[1]
    favorites = update_favorite_foods(update.effective_chat.id, food_to_remove, False)

    if favorites is None:
        update.callback_query.edit_message_text('You already removed that!')
        return

    if len(favorites) == 0:
        context.bot.edit_message_text(text=no_favorites_msg(), chat_id=update.effective_chat.id,
                                      message_id=update.callback_query.message.message_id, reply_markup=favorites_kb(favorites))
    else:
        context.bot.edit_message_text(text=favorites_msg(favorites), chat_id=update.effective_chat.id,
                                      message_id=update.callback_query.message.message_id, reply_markup=favorites_kb(favorites))
