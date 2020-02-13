from telegram import InlineKeyboardButton, InlineKeyboardMarkup

setting_button = InlineKeyboardButton("settings", callback_data="settings.home")


def settings_kb():
    button_list = [
        InlineKeyboardButton("Toggle Menu Visibility", callback_data="settings.hidden"),
        InlineKeyboardButton("View Favourite Foods", callback_data="settings.favorite"),
        InlineKeyboardButton("View Notification Settings", callback_data="settings.notification"),
        InlineKeyboardButton("Back to start", callback_data="start.home")
    ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=1))


def hidden_cuisine_kb(hidden_cuisine):
    cuisines = [
        "self_service", "western", "dim_sum_congee_noodle", "asian",
        "asian_vegetarian", "malay", "halal_vegetarian", "grab_and_go",
        "noodle", "vegetarian", "soup", "indian",
    ]
    kb_markup = list(
        map(lambda c: InlineKeyboardButton(('❌ ' if c in hidden_cuisine else '✅ ') + c, callback_data="menu." + c),
            cuisines))
    return InlineKeyboardMarkup(build_menu(kb_markup, n_cols=2, footer_buttons=[setting_button]))


def notification_kb(bf_sub, dn_sub):
    kb_markup = [
        InlineKeyboardButton(('✅ ' if bf_sub else '❌ ') + "Breakfast notification",
                             callback_data="settings.breakfast_subscribe"),
        InlineKeyboardButton(('✅ ' if dn_sub else '❌ ') + "Dinner notification",
                             callback_data="settings.dinner_subscribe")
    ]
    return InlineKeyboardMarkup(build_menu(kb_markup, n_cols=1, footer_buttons=[setting_button]))


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
