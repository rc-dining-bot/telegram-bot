"""List of constants"""
START = 'start'
HELP = 'help'
BREAKFAST = 'breakfast'
DINNER = 'dinner'
MENU = 'menu'
SETTINGS = 'settings'
FAVORITE = 'favorite'
NOTIFICATION = 'notification'
HOME = 'home'
"""Menu messages"""
BREAKFAST_COMMAND = f'/{BREAKFAST}';
BREAKFAST_DESC = f'{BREAKFAST_COMMAND} - view today\'s breakfast menu\n'
DINNER_COMMAND = f'DINNER'
DINNER_DESC = f'{DINNER_COMMAND} - view today\'s dinner menu\n';
"""Setting messages"""
SETTINGS_COMMAND = f'/{SETTINGS}'
SETTINGS_DESC = f'{SETTINGS_COMMAND} - customize menu visibility and display settings\n'
ADD_FAVORITE_COMMAND = '/add_favorite'
ADD_FAVORITE_DESC = f'{ADD_FAVORITE_COMMAND} <food> - add favorite food for notifications\n'
REMOVE_FAVORITE_COMMAND = '/remove_favorite'
REMOVE_FAVORITE_DESC = f'{REMOVE_FAVORITE_COMMAND} - remove favorite food from notifications\n'
NO_FAVORITES_MSG = f'You have no favorite foods! Use {ADD_FAVORITE_COMMAND} <food> to add one!'
HELP_COMMAND = '/help'
HELP_DESC = f'{HELP_COMMAND} - show the help message\n'
SET_BREAKFAST_NOTIFICATION_COMMAND = '/set_breakfast_time';
SET_BREAKFAST_NOTIFICATION_DESC = f'{SET_BREAKFAST_NOTIFICATION_COMMAND} - set breakfast notification time (HH:MM). ' \
                                  f'Notifications after 09:30 will be for the next day\'s breakfast\n '
SET_DINNER_NOTIFICATION_COMMAND = '/set_dinner_time';
SET_DINNER_NOTIFICATION_DESC = f'{SET_DINNER_NOTIFICATION_COMMAND} - set dinner notification time (HH:MM). ' \
                               f'Notifications after 21:30 will be for the next day\'s dinner\n '

COMMAND_LIST = \
    f'{BREAKFAST_DESC}{DINNER_DESC}' \
    f'{ADD_FAVORITE_DESC}{REMOVE_FAVORITE_DESC}{SET_BREAKFAST_NOTIFICATION_DESC}' \
    f'{SET_DINNER_NOTIFICATION_DESC}{SETTINGS_DESC}{HELP_DESC}\n' \
    f'{BREAKFAST_COMMAND} (or {DINNER_COMMAND}) <day> - view the breakfast/dinner menu for a particular day\n' \
    'e.g. /breakfast tomorrow, /breakfast saturday, /dinner next tuesday\n\n' \
    'Give feedback for the bot at https://github.com/rc-dining-bot/telegram-bot'


HELP_MSG = f'Hello, these are RC Dining Bot\'s commands:\n{COMMAND_LIST}'

NO_MENU_MSG = 'Sorry, today has no menu.'

BREAKFAST_TEMPLATE = ['self_service',
                      'western',
                      'dim_sum_congee_noodle',
                      'asian',
                      'asian_vegetarian',
                      'malay',
                      'halal_vegetarian',
                      'grab_and_go']
DINNER_TEMPLATE = ['self_service',
                   'western',
                   'noodle',
                   'asian',
                   'vegetarian',
                   'malay',
                   'indian',
                   'soup']


def WELCOME_MSG(user_first_name):
    return f'Hello, {user_first_name}! Welcome! To get started, enter one of the following commands:\n\n' \
           f'{COMMAND_LIST}'


def NO_MENU_MSG(meal):
    return f'Sorry, OHS does not have a {meal} menu for this day.'


def MENU_MSG(date, meal, menu):
    return f'{meal} - {date}\n\n{menu}'


def FAILED_TO_PARSE_DATE_MSG(entered_date):
    return f'Sorry, I don\'t understand the date {entered_date} :('


def FAVORITES_MSG(favorites):
    return f'These are your current favorites:\n{favorites}'


def ADDED_FAVORITES_MSG(favorites):
    return f'You have updated your favorites. {FAVORITES_MSG(favorites)}'


def MENU_HAS_FAVORITE_MSG(favorite):
    return f'Hey! This meal contains {favorite}'
