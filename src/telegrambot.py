import logging
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from util.const import (
    START, HELP, BREAKFAST,
    DINNER
)
from commands.meal import breakfast, dinner
from commands.general import start, handle_help
from database import connect

load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Set use_context=True to use the new context based callbacks
    updater = Updater(token=os.getenv('TOKEN'), use_context=True)

    # Get the dispatcher to
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler(START, start))
    dp.add_handler(CommandHandler(HELP, handle_help))
    dp.add_handler(CommandHandler(BREAKFAST, breakfast))
    dp.add_handler(CommandHandler(DINNER, dinner))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info("Bot is running")
    connect()
    main()
