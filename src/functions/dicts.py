import json
import logging
import random
from datetime import datetime

import utils
from utils import Timer


# def get_dict_keys(amount: int) -> list:
def get_dict_keys(amount):
    # with open(f'c:/code/projects/master-thesis/src/data/json/{str(amount)}_dict_keys.json', 'r') as f:
    with open('c:/code/projects/master-thesis/src/data/json/{0}_dict_keys.json'.format(str(amount)), 'r') as f:
        keys = json.load(f)

    return keys, [i for i in range(amount)]

# def run(version: str) -> None:
def run(version):
    results = list()
    amounts = [10000, 500000, 1000000]

    for amount in amounts:
        keys, values = get_dict_keys(amount)
        # results.append([f'dictionary_comprehension_{str(amount)}', dictionary_comprehension(keys, values), version])
        results.append(['dictionary_comprehension_{0}'.format(str(amount)), dictionary_comprehension(keys, values), version])
        # results.append([f'dictionary_insert_{str(amount)}', dictionary_insert(keys, values), version])
        results.append(['dictionary_insert_{0}'.format(str(amount)), dictionary_insert(keys, values), version])
        results.append([
            # f'dictionary_merge_{str(amount)}',
            'dictionary_merge_{0}'.format(str(amount)),
            dictionary_merge({k: v for k, v in zip(keys, values)}, {v: k for k, v in zip(keys, values)}),
            version
        ])
        # results.append([f'read_dictionary_values_{str(amount)}', read_dictionary_values({k: v for k, v in zip(keys, values)}), version])
        results.append(['read_dictionary_values_{0}'.format(str(amount)), read_dictionary_values({k: v for k, v in zip(keys, values)}), version])

    # utils.write_to_csv('dictionary', results)



# def dictionary_comprehension(keys: list, values: list) -> float:
def dictionary_comprehension(keys, values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start dictionary_comprehension() on dict with %s elements', len(keys))

        dict_ = {key: value for key, value in zip(keys, values)}

        logging.info('Finalizing dictionary_comprehension()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(dict_)
    return timer.runtime

# def dictionary_insert(keys: list, values: list) -> float:
def dictionary_insert(keys, values):
    random.seed(42)

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    dict_ = {key: None for key in keys}
    random.shuffle(keys)

    with timer:
        logging.info('Start dictionary_insert() on dict with %s elements', len(dict_))

        for key, value in zip(keys, values):
            dict_[key] = value
        
        logging.info('Finalizing dictionary_insert()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(dict_)
    return timer.runtime

# def dictionary_merge(dict_one: dict, dict_two: dict) -> float:
def dictionary_merge(dict_one, dict_two):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start dictionary_merge() on dicts with %s and %s elements', len(dict_one), len(dict_two))

        dict_one.update(dict_two)

        logging.info('Finalizing dictionary_merge()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(dict_one)
    return timer.runtime

# def read_dictionary_values(dict_: dict) -> float:
def read_dictionary_values(dict_):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start read_dictionary_values() on dict with %s elements', len(dict_))

        for key in dict_.keys():
            value = dict_[key]
            utils.devnull(value)
        
        logging.info('Finalizing read_dictionary_values()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    return timer.runtime
