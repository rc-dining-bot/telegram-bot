from src.util.formatting import bold, italicize


def parse_menu(data):
    menu = ''
    for key in data.keys():
        if key == 'date':
            continue
        menu += bold(key.capitalize()) + '\n'
        for item in data[key]:
            if item == 'OR':
                menu += italicize(item) + '\n'
            else:
                menu += item + '\n'
        menu += '\n'
    return menu

