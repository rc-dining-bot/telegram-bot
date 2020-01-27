from src.util.const import COMMAND_LIST


# general messages
def welcome_msg(user_first_name):
    return f'Hello, {user_first_name}! Welcome! To get started, enter one of the following commands:\n\n' \
           f'{COMMAND_LIST}'


def help_msg():
    return f'Hello, these are RC Dining Bot\'s commands:\n{COMMAND_LIST}'


# menu messages
def no_menu_msg(meal):
    return f'Sorry, OHS has not provided the {meal} menu for this day.'


def menu_msg(date, meal, menu):
    return f'{meal} - {date}\n\n{menu}'


def failed_to_parse_date_msg(entered_date):
    return f'Sorry, I don\'t understand the date {entered_date} :('


# setting messages
def settings_msg():
    return 'Hi, here is the menu for settings:\n'


def no_hidden_cuisine_msg():
    return 'You do not have any hidden cuisine.'


def hidden_cuisine_msg(name):
    return f'Hi, {name}, you hid the following cuisines\n'


def favorites_msg(favorites):
    return f'These are your current favorites:\n{favorites}'


def added_favorites_msg(favorites):
    return f'You have updated your favorites. {favorites_msg(favorites)}'


def menu_has_favorite_msg(favorite):
    return f'Hey! This meal contains {favorite}'
