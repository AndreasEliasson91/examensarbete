import json
import logging
import requests
from datetime import datetime

import utils


def generate_dict_keys(amount: int, reload: bool=False) -> list:
    if reload:
        logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logging.info('Reload keys for amount %s', amount)
        with open(f'src/data/json/dict_keys_{amount}.json', 'r') as in_file:
            return json.load(in_file)

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('Create new dict keys for amount: %s', amount)
    keys = list()

    if amount > 500:  # API has a max limit of 500 words at a time
        amounts = [a[1] - a[0] for a in utils.range_sequence(0, amount, 500)]
        
        for a in amounts:
            response = requests.get(
                f'https://random-word-api.vercel.app/api?words={a}',
                timeout=5
            )
            keys.extend(response.json())
    else:
        response = requests.get(
            f'https://random-word-api.vercel.app/api?words={amount}',
            timeout=5
        )
        keys = response.json()

    utils.devnull(keys)
    with open(f'src/data/json/dict_keys_{amount}.json', 'w') as out_file:
        out_file.write(json.dumps(keys))

    return keys
