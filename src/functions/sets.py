import logging
from datetime import datetime

import utils
from utils import Timer


def set_merge(set_one: set, set_two: set) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start set_merge() on sets with %s and %s elements', len(set_one), len(set_two))

        set_one.update(set_two)
        
        logging.info('Finalizing set_merge()')

    logging.info('Result:\t%s seconds\n', timer.runtime)

    utils.devnull(set_one)
    return timer.runtime

