import logging
from datetime import datetime

import utils
from utils import Timer


def list_comprehension(amount: int) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start list_comprehension() with %s elements', amount)

        list_ = [x for x in range(amount)]

        logging.info('Finalizing list_comprehension()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(list_)
    return timer.runtime

def list_append(values: list) -> float:
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


def list_sort(list_: list) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start list_sort() with list containing %s elements', len(list_))

        sorted_list = sorted(list_)

        logging.info('Finalizing list_sort()')
    
    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(sorted_list)
    return timer.runtime
