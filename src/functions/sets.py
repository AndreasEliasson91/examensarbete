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
        results.append([
            # f'set_merge_{str(amount)}',
            'set_merge_{0}'.format(str(amount)),
            set_merge(set(random.randint(0,amount*2) for _ in range(amount)), set(random.randint(0,amount*2) for _ in range(amount))),
            version
        ])

    # utils.write_to_csv('set', results)


# def set_merge(set_one: set, set_two: set) -> float:
def set_merge(set_one, set_two):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('Start set_merge() on sets with %s and %s elements', len(set_one), len(set_two))

        set_one.update(set_two)
        
        logging.info('Finalizing set_merge()')

    logging.info('Result:\t%s seconds\n', timer.runtime)

    utils.devnull(set_one)
    return timer.runtime

