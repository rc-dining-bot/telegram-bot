from util.const import COMMAND_LIST


# general messages
def welcome_msg(user_first_name):
    return f'<b>Hello, {user_first_name}! Welcome back! What do you like to check?</b>\n\n' \
           f'<i>Press help button or use /help command to view different commands.</i>'


def help_msg():
    return f'<b>Hello, these are RC Dining Bot\'s commands:</b>\n{COMMAND_LIST}'


# menu messages
def no_menu_msg(meal):
    return f'Sorry, OHS has not provided the {meal} menu for this day.'


def menu_msg(date, meal, menu):
    return f'{meal.capitalize()} - {date.strftime("%A, %d %b %Y")}\n\n{menu}'


def failed_to_parse_date_msg(entered_date):
    return f'Sorry, I don\'t understand the date {entered_date} :('


# setting messages
def settings_msg():
    return '<b>Hi, here is the menu for settings:</b>\n'


def no_hidden_cuisine_msg():
    return '<b>You do not have any hidden cuisines.</b>'


def hidden_cuisine_msg(name):
    return f'<b>Hi, {name}, you hid the following cuisines</b>\n'


def favorites_msg(favorites):
    return f'<b>These are your current favorites:</b>\n{favorites}'


def added_favorites_msg(favorites):
    return f'<b>You have updated your favorites.</b> {favorites_msg(favorites)}'


def menu_has_favorite_msg(favorite):
    return f'<b>Hey! This meal contains</b> {favorite}'


def notification_view_msg():
    return f'You have subscribed to the following meal broadcast:'
