def get_first_name(update):
    return update.message.chat.first_name


def parse_menu(template, data):
    menu = ''
    for key in template:
        menu += bold(key.capitalize()) + '\n'
        for item in data[key]:
            if item == 'OR':
                menu += italicize(item) + '\n'
            else:
                menu += item + '\n'
        menu += '\n'
    return menu


def bold(text):
    return f'<b>{text}</b>'


def italicize(text):
    return f'<i>{text}</i>'
