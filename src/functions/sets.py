import logging
import random
from datetime import datetime

import utils
from utils import Timer

random.seed(42)
AMOUNT = 10000000
NUM_ROUNDS = 100

def run(version):
    total_timer = Timer()
    results = list()

    set_one = set(random.randint(0,AMOUNT*2) for _ in range(AMOUNT))
    set_two = set(random.randint(0,AMOUNT*2) for _ in range(AMOUNT))

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START SET TEST CASES FOR V. %s\n', version)
    with total_timer:
        for i in range(NUM_ROUNDS):
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))

            results.append(['set_merge', AMOUNT, set_merge(set_one, set_two), version])
        
        logging.info('FINALIZING SET TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    utils.write_to_csv('set', results)

def set_merge(set_one, set_two):
    timer = Timer()

    with timer:
        set_one.update(set_two)

    utils.devnull(set_one)
    return timer.runtime

