import requests
import logging

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
    if numPax is None:
        update.message.reply_text(unable_to_retrieve_information_msg())
    else:
        update.message.reply_text(str(numPax) + ' pax')
