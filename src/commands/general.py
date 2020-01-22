from ..util.const import WELCOME_MSG, HELP_MSG


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME_MSG(update.message.chat.first_name))


def handle_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MSG)
