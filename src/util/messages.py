from src.util.const import COMMAND_LIST


def help_msg():
    return f'Hello, these are RC Dining Bot\'s commands:\n{COMMAND_LIST}'


def welcome_msg(user_first_name):
    return f'Hello, {user_first_name}! Welcome! To get started, enter one of the following commands:\n\n' \
           f'{COMMAND_LIST}'


def no_menu_msg(meal):
    return f'Sorry, OHS has not provided the {meal} menu for this day.'


def menu_msg(date, meal, menu):
    return f'{meal} - {date}\n\n{menu}'


def failed_to_parse_date_msg(entered_date):
    return f'Sorry, I don\'t understand the date {entered_date} :('


def favorites_msg(favorites):
    return f'These are your current favorites:\n{favorites}'


def added_favorites_msg(favorites):
    return f'You have updated your favorites. {favorites_msg(favorites)}'


def menu_has_favorite_msg(favorite):
    return f'Hey! This meal contains {favorite}'
