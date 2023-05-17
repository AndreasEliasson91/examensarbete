import json
import logging
import random
from copy import copy
from datetime import datetime

import utils
from utils import Timer

random.seed(42)
AMOUNT = 10000000
NUM_ROUNDS = 100

def get_dict_keys(data_dir, amount):
    with open(data_dir + '{0}_dict_keys.json'.format(str(amount)), 'r', encodin='utf-8') as in_file:
        keys = json.load(in_file)

    return keys, [i for i in range(amount)]

def run(version):
    total_timer = Timer()
    results = list()

    keys, values = get_dict_keys('../data/', AMOUNT)
    shuffled_keys = copy(keys)
    random.shuffle(shuffled_keys)

    dict_one, dict_two = {k: v for k, v in zip(keys, values)}, {v: k for k, v in zip(keys, values)}

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START DICTIONARY TEST CASES FOR V. %s\n', version)
    with total_timer:
        for i in range(NUM_ROUNDS):
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))

            results.append(['dictionary_comprehension', AMOUNT, dictionary_comprehension(keys, values), version])
            results.append(['dictionary_insert', AMOUNT, dictionary_insert(keys, values, shuffled_keys), version])
            results.append(['dictionary_merge', AMOUNT, dictionary_merge(dict_one, dict_two), version])
            results.append(['read_dictionary_values', AMOUNT, read_dictionary_values(dict_one), version])
        
        logging.info('FINALIZING DICTIONARY TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    utils.write_to_csv('dictionary', results)

def dictionary_comprehension(keys, values):
    timer = Timer()

    with timer:
        dict_ = {key: value for key, value in zip(keys, values)}

    utils.devnull(dict_)
    return timer.runtime

def dictionary_insert(keys, values, shuffled_keys):
    timer = Timer()

    dict_ = {key: None for key in keys}

    with timer:
        for key, value in zip(shuffled_keys, values):
            dict_[key] = value

    utils.devnull(dict_)
    return timer.runtime

def dictionary_merge(dict_one, dict_two):
    timer = Timer()

    with timer:
        dict_one.update(dict_two)

    utils.devnull(dict_one)
    return timer.runtime

def read_dictionary_values(dict_):
    timer = Timer()

    with timer:
        for key in dict_.keys():
            value = dict_[key]
            utils.devnull(value)

    return timer.runtime
