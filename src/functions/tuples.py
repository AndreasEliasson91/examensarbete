import logging
import random
from datetime import datetime

import utils
from utils import Timer


# def run(version: str):
def run(version):
    random.seed(42)
    results = list()
    amounts = [10000, 50000, 100000]

    for amount in amounts:
        # results.append([f'tuple_append_{str(amount)}', tuple_append([i for i in range(amount)]), version])
        results.append(['tuple_append_{0}'.format(str(amount)), tuple_append([i for i in range(amount)]), version])
        # results.append([f'tuple_sort_{str(amount)}', tuple_sort([random.randint(0,100) for _ in range(amount)]), version])
        results.append(['tuple_sort_{0}'.format(str(amount)), tuple_sort([random.randint(0,100) for _ in range(amount)]), version])

    # utils.write_to_csv('tuple', results)

# def tuple_append(values: list) -> float:
def tuple_append(values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start tuple_append() on tuple with %s elements', len(values))
        tuple_ = tuple()

        for val in values:
            tuple_ += (val,)

        logging.info('Finalizing tuple_append()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(tuple_)
    return timer.runtime

# def tuple_sort(tuple_: tuple) -> float:
def tuple_sort(tuple_):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start tuple_sort() on tuple with %s elements', len(tuple_))

        sorted_tuple = tuple(sorted(tuple_))

        logging.info('Finalizing tuple_sort()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(sorted_tuple)
    return timer.runtime
