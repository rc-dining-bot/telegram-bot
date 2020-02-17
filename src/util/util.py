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


def utc_time(hour, minute, second):
    # time input - 8 hours = utc time
    # assuming the users are in Asia/Singapore timezone
    return (datetime.combine(date.today(), time(hour=hour, minute=minute, second=second)) + timedelta(hours=-8)).time()


def localized_date_today():
    # localized date to Asia/Singapore, assuming the machine is running in utc timezone
    return (datetime.now() + timedelta(hours=8)).date()
