from telegram import InlineKeyboardButton, InlineKeyboardMarkup


start_button = InlineKeyboardButton(text="Back to start", callback_data="start.home")


def start_button_kb():
    return InlineKeyboardMarkup(build_menu([start_button], n_cols=1))


def settings_kb():
    button_list = [
        InlineKeyboardButton(text="Toggle Menu Visibility",     callback_data="settings.hidden"),
        InlineKeyboardButton(text="View Favourite Foods",       callback_data="settings.favorite"),
        InlineKeyboardButton(text="View Notification Settings", callback_data="settings.notification"),
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
            InlineKeyboardButton(text=('❌ ' if c in hidden_cuisine else '✅ ') + c,
                                 callback_data="menu." + c),
            cuisines))
    setting_button = InlineKeyboardButton(text="settings",
                                          callback_data="settings.home")
    return InlineKeyboardMarkup(build_menu(kb_markup,
                                           n_cols=2,
                                           footer_buttons=[setting_button]))


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
