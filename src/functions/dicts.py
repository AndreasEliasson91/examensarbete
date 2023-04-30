import logging
import random
from datetime import datetime

import utils
from utils import Timer


def run() -> None:
    pass


def dictionary_comprehension(keys: list, values: list) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start dictionary_comprehension() on dict with %s elements', len(keys))

        dict_ = {key: value for key, value in zip(keys, values)}

        logging.info('Finalizing dictionary_comprehension()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(dict_)
    return timer.runtime

def dictionary_insert(keys: list, values: list) -> float:
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

def dictionary_merge(dict_one: dict, dict_two: dict) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start dictionary_merge() on dicts with %s and %s elements', len(dict_one), len(dict_two))

        dict_one.update(dict_two)

        logging.info('Finalizing dictionary_merge()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(dict_one)
    return timer.runtime

def read_dictionary_values(dict_: dict) -> float:
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
