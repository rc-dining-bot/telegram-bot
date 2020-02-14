from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from util.formatting import capitalize, normalize

setting_button = InlineKeyboardButton("Back to Settings", callback_data="settings.home")


start_button = InlineKeyboardButton(text="Back to start", callback_data="start.home")


def start_kb():
    button_list = [
        InlineKeyboardButton(text="Breakfast Menu", callback_data="menu.breakfast"),
        InlineKeyboardButton(text="Dinner Menu",    callback_data="menu.dinner"),
        InlineKeyboardButton(text="Settings",       callback_data="settings.home"),
        InlineKeyboardButton(text="Help",           callback_data="start.help"),
    ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=1))


def start_button_kb():
    return InlineKeyboardMarkup(build_menu([start_button], n_cols=1))


def settings_kb():
    button_list = [
        InlineKeyboardButton(text="Toggle Menu Visibility",     callback_data="settings.hidden"),
        # InlineKeyboardButton(text="View Favourite Foods",       callback_data="settings.favorite"),
        InlineKeyboardButton(text="Toggle Notification Settings", callback_data="settings.notification"),
        start_button
    ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=1))


def hidden_cuisine_kb(hidden_cuisine):
    # current selection of cuisines
    cuisines = [
        "self_service", "western", "dim_sum_congee_noodle", "asian",
        "asian_vegetarian", "malay", "halal_vegetarian", "grab_and_go",
        "noodle", "vegetarian", "soup", "indian",
    ]
    kb_markup = list(
        map(lambda c:
            InlineKeyboardButton(text=('❌ ' if c in hidden_cuisine else '✅ ') + capitalize(normalize(c)),
                                 callback_data="menu." + c),
            cuisines))
    return InlineKeyboardMarkup(build_menu(kb_markup, n_cols=2, footer_buttons=[setting_button, start_button]))


def notification_kb(bf_sub, dn_sub):
    kb_markup = [
        InlineKeyboardButton(('✅ ' if bf_sub else '❌ ') + "Breakfast notification",
                             callback_data="settings.breakfast_subscribe"),
        InlineKeyboardButton(('✅ ' if dn_sub else '❌ ') + "Dinner notification",
                             callback_data="settings.dinner_subscribe")
    ]
    return InlineKeyboardMarkup(build_menu(kb_markup, n_cols=1, footer_buttons=[setting_button, start_button]))


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    # builds the menu with:
    # array of buttons
    # number of rows
    # (optionally) array of header/footer buttons
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
