from src.util.formatting import bold, italicize


def parse_menu(template, data):
    menu = ''
    print(data.keys)
    for key in data.keys():
        menu += bold(key.capitalize()) + '\n'
        for item in data[key]:
            if item == 'OR':
                menu += italicize(item) + '\n'
            else:
                menu += item + '\n'
        menu += '\n'
    return menu

