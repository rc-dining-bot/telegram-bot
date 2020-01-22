import json
import os.path
from src.util.const import (
    BREAKFAST, DINNER
)
from src.util.util import parse_menu


def breakfast(update, context):
    """Send the user breakfast menu"""
    with open(os.path.dirname(__file__) + '/../mock/breakfast.json', 'r') as bf:
        data = json.load(bf)
    menu = parse_menu(data)
    update.message.reply_text(menu, parse_mode='HTML')


def dinner(update, context):
    """Send the user dinner menu"""
    with open(os.path.dirname(__file__) + '/../mock/dinner.json', 'r') as dn:
        data = json.load(dn)
    menu = parse_menu(data)
    update.message.reply_text(menu, parse_mode='HTML')
