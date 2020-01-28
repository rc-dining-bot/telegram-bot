from util.messages import welcome_msg, help_msg
import logging


def handle_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_msg(
        update.message.chat.first_name))


def handle_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg())


def handle_error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"',
                    update.update_id, context.error)
