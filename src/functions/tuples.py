import logging
from datetime import datetime

import utils
from utils import Timer


def tuple_append(values: list) -> float:
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

def tuple_sort(tuple_: tuple) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start tuple_sort() on tuple with %s elements', len(tuple_))

        sorted_tuple = tuple(sorted(tuple_))

        logging.info('Finalizing tuple_sort()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(sorted_tuple)
    return timer.runtime
