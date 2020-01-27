import logging
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from src.util.const import (
    START,
    HELP,
    BREAKFAST,
    DINNER,
    SETTINGS
)
from src.commands.meal import handle_menu
from src.commands.general import (
    handle_start,
    handle_help,
    handle_error
)
from src.database.database import connect

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main():
    """Start the bot."""
    # Set use_context=True to use the new context based callbacks
    updater = Updater(token=os.getenv('RC_DINING_BOT_TOKEN'), use_context=True)

    # Get the dispatcher to
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler(START, handle_start))
    dispatcher.add_handler(CommandHandler(HELP, handle_help))
    dispatcher.add_handler(CommandHandler(BREAKFAST, handle_menu(meal=BREAKFAST)))
    dispatcher.add_handler(CommandHandler(DINNER, handle_menu(meal=DINNER)))

    # log all errors
    dispatcher.add_error_handler(handle_error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logging.info("Bot is running")
    load_dotenv()
    connect()
    main()
