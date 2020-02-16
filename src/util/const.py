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
SET_BREAKFAST_NOTIFICATION = 'subscribe_breakfast'
SET_DINNER_NOTIFICATION = 'subscribe_dinner'
BROADCAST_SUBSCRIPTION = '_subscribed'
RV_COUNT = 'rvcount'

# start messages
START_COMMAND = f'/{START}'
START_DESC = f'{START_COMMAND} - welcome message\n'

# menu messages
BREAKFAST_COMMAND = f'/{BREAKFAST}'
BREAKFAST_DESC = f'{BREAKFAST_COMMAND} - view breakfast menu today. Breakfast is served 7:00-10:30AM daily.\n'
DINNER_COMMAND = f'/{DINNER}'
DINNER_DESC = f'{DINNER_COMMAND} - view dinner menu today. Dinner is served 5:30-9:30AM daily.\n'

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
SET_BREAKFAST_NOTIFICATION_COMMAND = '/subscribe_breakfast'
SET_BREAKFAST_NOTIFICATION_DESC = f'{SET_BREAKFAST_NOTIFICATION_COMMAND} ' \
                                  f'- subscribe to breakfast broadcast at <b>12AM</b> daily.\n'
SET_DINNER_NOTIFICATION_COMMAND = '/subscribe_dinner'
SET_DINNER_NOTIFICATION_DESC = f'{SET_DINNER_NOTIFICATION_COMMAND} ' \
                               f'- subscribe to dinner broadcast at <b>3PM</b> daily.\n'
CHECK_RVRC_DINING_COUNT_COMMAND = '/rvcount'
CHECK_RVRC_DINING_COUNT_DESC = f'{CHECK_RVRC_DINING_COUNT_COMMAND} ' \
                               f'- check RVRC dining hall occupancy ' \
                               f'(while the COVID-19 control measure is still in place.)\n'

COMMAND_LIST = \
    f'{START_DESC}' \
    f'{BREAKFAST_DESC}' \
    f'{DINNER_DESC}' \
    f'{SETTINGS_DESC}' \
    f'{SET_BREAKFAST_NOTIFICATION_DESC}' \
    f'{SET_DINNER_NOTIFICATION_DESC}' \
    f'{HELP_DESC}' \
    f'{CHECK_RVRC_DINING_COUNT_DESC}' \
    f'\n' \
    f'<b>NOTE:</b> {BREAKFAST_COMMAND} (or {DINNER_COMMAND}) [DAY] - view the breakfast/dinner menu ' \
    f'for a particular day\n' \
    '<i>e.g. /breakfast tomorrow, /breakfast saturday, /dinner next tuesday</i>\n\n' \
    'Give feedback for the bot at https://github.com/rc-dining-bot/telegram-bot'
