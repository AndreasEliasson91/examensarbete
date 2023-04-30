import logging
from datetime import datetime

from utils import Timer


def iteration_test(iterable: iter) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()
    
    with timer:
        logging.info('Start iteration_test() on %s with %s elements', type(iterable), len(iterable))

        for _ in iterable:
            pass

        logging.info('Finalizing iteration_test()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    return timer.runtime
