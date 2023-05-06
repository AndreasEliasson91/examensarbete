import logging
import random
from datetime import datetime

import utils
from utils import Timer

random.seed(42)
AMOUNT = 1000000
NUM_ROUNDS = 100

# def run(version: str):
def run(version):
    total_timer = Timer()
    results = list()

    append_tuple = [i for i in range(AMOUNT)]
    sort_tuple = [random.randint(0,100) for _ in range(AMOUNT)]

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START SET TEST CASES FOR V. %s\n', version)
    with total_timer:
        for i in range(NUM_ROUNDS):
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))
            # results.append([f'tuple_append_{str(i+1)}', tuple_append(append_tuple), version])
            # results.append([date_time, 'tuple_append', AMOUNT, tuple_append(append_tuple), version])
            # results.append([f'tuple_sort_{str(amount)}', tuple_sort(sort_tuple), version])
            results.append([date_time, 'tuple_sort', AMOUNT, tuple_sort(sort_tuple), version])
        logging.info('FINALIZING SET TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    # utils.write_to_csv('tuple', results)

# def tuple_append(values: list) -> float:
def tuple_append(values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('tuple_append()')
        tuple_ = tuple()

        for val in values:
            tuple_ += (val,)

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(tuple_)
    return timer.runtime

# def tuple_sort(tuple_: tuple) -> float:
def tuple_sort(tuple_):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('tuple_sort()')
        sorted_tuple = tuple(sorted(tuple_))

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(sorted_tuple)
    return timer.runtime
