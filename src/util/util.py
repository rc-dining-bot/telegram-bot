from datetime import datetime, date, time, timedelta
from util.formatting import bold, italicize, normalize


def parse_menu(data, hidden_cuisines):
    menu = ''
    for key in data.keys():
        if key == 'date' or key in hidden_cuisines:
            continue
        menu += bold(normalize(key)) + '\n'
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


def localize_time(hour, minute, second):
    return (datetime.combine(date.today(), time(hour=hour, minute=minute, second=second)) + timedelta(hours=-8)).time()
