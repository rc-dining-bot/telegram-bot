# list of constants
START = 'start'
HELP = 'help'
BREAKFAST = 'breakfast'
DINNER = 'dinner'
MENU = 'menu'
SETTINGS = 'settings'
FAVORITE = 'favorite'
NOTIFICATION = 'notification'
HOME = 'home'
HIDE_CUISINE = 'hidden'

# menu messages
BREAKFAST_COMMAND = f'/{BREAKFAST}'
BREAKFAST_DESC = f'{BREAKFAST_COMMAND} - view breakfast menu today\n'
DINNER_COMMAND = f'/{DINNER}'
DINNER_DESC = f'{DINNER_COMMAND} - view dinner menu today\n'

# setting messages
SETTINGS_COMMAND = f'/{SETTINGS}'
SETTINGS_DESC = f'{SETTINGS_COMMAND} - customize menu visibility and display settings\n'
ADD_FAVORITE_COMMAND = '/add_favorite'
ADD_FAVORITE_DESC = f'{ADD_FAVORITE_COMMAND} [FOOD] - add favorite food for notifications\n'
REMOVE_FAVORITE_COMMAND = '/remove_favorite'
REMOVE_FAVORITE_DESC = f'{REMOVE_FAVORITE_COMMAND} - remove favorite food from notifications\n'
NO_FAVORITES_MSG = f'You have no favorite foods! Use {ADD_FAVORITE_COMMAND} [FOOD] to add one!'
HELP_COMMAND = '/help'
HELP_DESC = f'{HELP_COMMAND} - show the help message\n'
SET_BREAKFAST_NOTIFICATION_COMMAND = '/set_breakfast_time'
SET_BREAKFAST_NOTIFICATION_DESC = f'{SET_BREAKFAST_NOTIFICATION_COMMAND} - set breakfast notification time (HH:MM). ' \
                                  f'<i>Notifications after 09:30 will be for the next day\'s breakfast</i>\n '
SET_DINNER_NOTIFICATION_COMMAND = '/set_dinner_time'
SET_DINNER_NOTIFICATION_DESC = f'{SET_DINNER_NOTIFICATION_COMMAND} - set dinner notification time (HH:MM). ' \
                               f'<i>Notifications after 21:30 will be for the next day\'s dinner</i>\n '

COMMAND_LIST = \
    f'{BREAKFAST_DESC}' \
    f'{DINNER_DESC}' \
    f'{ADD_FAVORITE_DESC}' \
    f'{REMOVE_FAVORITE_DESC}' \
    f'{SET_BREAKFAST_NOTIFICATION_DESC}' \
    f'{SET_DINNER_NOTIFICATION_DESC}' \
    f'{SETTINGS_DESC}' \
    f'{HELP_DESC}' \
    f'\n' \
    f'<b>NOTE:</b> {BREAKFAST_COMMAND} (or {DINNER_COMMAND}) [DAY] - view the breakfast/dinner menu ' \
    f'for a particular day\n' \
    '<i>e.g. /breakfast tomorrow, /breakfast saturday, /dinner next tuesday</i>\n\n' \
    # 'Give feedback for the bot at https://github.com/rc-dining-bot/telegram-bot'
    # the line above generates a preview window which would likely reduce the user experience
