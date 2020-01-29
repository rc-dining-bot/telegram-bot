from util.formatting import bold, italicize


def parse_menu(data, hidden_cuisines):
    menu = ''
    for key in data.keys():
        if key == 'date' or key in hidden_cuisines:
            continue
        menu += bold(key.capitalize()) + '\n'
        for item in data[key]:
            if item == 'OR':
                menu += italicize(item) + '\n'
            else:
                menu += item + '\n'
        menu += '\n'
    return menu


def parse_callback(data):
    split_data = data.split('.', 1)
    return split_data[0], split_data[1]
