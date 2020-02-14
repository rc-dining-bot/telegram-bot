def bold(text):
    return f'<b>{text}</b>'


def italicize(text):
    return f'<i>{text}</i>'


def normalize(text):
    return text.replace('_', ' ').title()


def capitalize(text):
    return ' '.join(list(map(lambda t: t.capitalize(), text.split())))
