import telegram
from telegram.ext import run_async

from util.const import (
    BREAKFAST,
    DINNER
)
from util.messages import settings_msg, notification_view_msg
from util.kb_mark_up import settings_kb, hidden_cuisine_kb, notification_kb
from util.util import parse_callback
from database.database import (
    get_hidden_cuisines,
    get_subscribe_setting,
    update_hidden_cuisine,
    update_subscribe_setting
)
from util.messages import (
    no_hidden_cuisine_msg,
    hidden_cuisine_msg,
)


# settings menu
@run_async
def handle_settings(update, context):
    if update.callback_query is not None:
        context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                      message_id=update.callback_query.message.message_id,
                                      text=settings_msg(),
                                      reply_markup=settings_kb(),
                                      parse_mode=telegram.ParseMode.HTML)
        context.bot.answer_callback_query(update.callback_query.id)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=settings_msg(),
                                 reply_markup=settings_kb(),
                                 parse_mode=telegram.ParseMode.HTML)


# hidden cuisine panel
@run_async
def handle_hidden_cuisine(update, context):
    hidden_cuisine = get_hidden_cuisines(update.effective_chat.id)
    msg = no_hidden_cuisine_msg() if not hidden_cuisine else hidden_cuisine_msg(update.effective_chat.first_name)

    if update.callback_query is not None:
        context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                      message_id=update.callback_query.message.message_id,
                                      text=msg,
                                      reply_markup=hidden_cuisine_kb(hidden_cuisine),
                                      parse_mode=telegram.ParseMode.HTML)
        context.bot.answer_callback_query(update.callback_query.id)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=msg,
                                 reply_markup=hidden_cuisine_kb(hidden_cuisine),
                                 parse_mode=telegram.ParseMode.HTML)


# update keyboard markup after updating hide cuisine panel
def handle_hide_cuisine(update, context):
    if update.callback_query is not None:
        context.bot.answer_callback_query(update.callback_query.id)
    cuisine_to_hide = parse_callback(update.callback_query.data)[1]
    updated_hidden_cuisine = update_hidden_cuisine(update.effective_chat.id, cuisine_to_hide)

    update.callback_query.edit_message_reply_markup(reply_markup=hidden_cuisine_kb(updated_hidden_cuisine))


@run_async
def handle_notification(update, context):
    chat_id = update.effective_chat.id
    bf_sub, dn_sub = get_subscribe_setting(chat_id)
    if update.callback_query is not None:
        context.bot.edit_message_text(chat_id=chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      text=notification_view_msg(),
                                      reply_markup=notification_kb(bf_sub=bf_sub, dn_sub=dn_sub))
        context.bot.answer_callback_query(update.callback_query.id)
    else:
        context.bot.send_message(chat_id=chat_id,
                                 text=notification_view_msg(),
                                 reply_markup=notification_kb(bf_sub=bf_sub, dn_sub=dn_sub))


def handle_subscribe(meal):
    assert meal == BREAKFAST or meal == DINNER, "Meal input is incorrect."

    def toggle_subscribe(update, context):
        chat_id = update.effective_chat.id
        bf_sub, dn_sub = update_subscribe_setting(chat_id=chat_id, meal=meal)
        if update.callback_query is None:
            handle_notification(update, context)
        else:
            update.callback_query.edit_message_reply_markup(reply_markup=notification_kb(bf_sub=bf_sub, dn_sub=dn_sub))

        if update.callback_query is not None:
            context.bot.answer_callback_query(update.callback_query.id)

    return toggle_subscribe
