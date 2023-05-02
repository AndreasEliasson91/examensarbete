import logging
import random
from datetime import datetime

import utils
from utils import Timer


# def run(version: str):
def run(version):
    random.seed(42)
    results = list()
    amounts = [10000, 500000, 1000000]

    for amount in amounts:
        # results.append([f'list_comprehension_{str(amount)}', list_comprehension(amount), version])
        results.append(['list_comprehension_{0}'.format(str(amount)), list_comprehension(amount), version])
        # results.append([f'list_append_{str(amount)}', list_append([i for i in range(amount)]), version])
        results.append(['list_append_{0}'.format(str(amount)), list_append([i for i in range(amount)]), version])
        # results.append([f'list_sort_{str(amount)}', list_sort([random.randint(0,100) for _ in range(amount)]), version])
        results.append(['list_sort_{0}'.format(str(amount)), list_sort([random.randint(0,100) for _ in range(amount)]), version])

    # utils.write_to_csv('list', results)

# def list_comprehension(amount: int) -> float:
def list_comprehension(amount):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start list_comprehension() with %s elements', amount)

        list_ = [x for x in range(amount)]

        logging.info('Finalizing list_comprehension()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(list_)
    return timer.runtime

# def list_append(values: list) -> float:
def list_append(values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start list_append() with list containing %s elements', len(values))
        list_ = []

        for val in values:
            list_.append(val)

        logging.info('Finalizing list_append()')
            
    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(list_)
    return timer.runtime


# def list_sort(list_: list) -> float:
def list_sort(list_):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start list_sort() with list containing %s elements', len(list_))

        sorted_list = sorted(list_)

        logging.info('Finalizing list_sort()')
    
    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(sorted_list)
    return timer.runtime
