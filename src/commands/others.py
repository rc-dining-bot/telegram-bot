import requests
import logging

from util.kb_mark_up import start_button_kb
from util.messages import unable_to_retrieve_information_msg


def get_rv_count():
    url = 'http://wwwapps.ehabitat.net/rvrcdh/api/v1/currentCount.php'
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError as error:
        logging.error('Failed to establish connection')
        logging.error(error)
        return None
    except requests.exceptions.Timeout:
        logging.error('Request to %s timed out', url)
        return None

    status_code = response.status_code
    if status_code != 200:
        logging.error('%s returned %d', url, status_code)
        logging.error('Response: %s', response.content)
        return None

    if response.json() and 'response' in response.json() and 'numberOfPax' in response.json()['response']:
        return response.json()['response']['numberOfPax']
    return None


def handle_rv_count(update, context):
    numPax = get_rv_count()
    chat_id = update.effective_chat.id
    if numPax is None:
        context.bot.send_message(chat_id=chat_id,
                                 text=unable_to_retrieve_information_msg(),
                                 reply_markup=start_button_kb())
    else:
        context.bot.send_message(chat_id=chat_id,
                                 text=f'{numPax} pax',
                                 reply_markup=start_button_kb())
