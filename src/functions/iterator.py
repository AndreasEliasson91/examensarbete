import logging
from datetime import datetime

import utils
from utils import Timer

AMOUNT = 10000000
NUM_ROUNDS = 100

def run(version):
    total_timer = Timer()
    results = list()

    list_values = list(i for i in range(AMOUNT))
    set_values = set(i for i in range(AMOUNT))
    tuple_values = tuple(i for i in range(AMOUNT))

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START ITERATOR TEST CASES FOR V. %s\n', version)

    with total_timer:
        for i in range(NUM_ROUNDS):
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))

            results.append(['iteration_test_set', AMOUNT, iteration_test(set_values), version])
            results.append(['iteration_test_tuple', AMOUNT, iteration_test(tuple_values), version])
            results.append(['iteration_test_list', AMOUNT, iteration_test(list_values), version])

        logging.info('FINALIZING ITERATOR TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    utils.write_to_csv('iterator', results)

def iteration_test(iterable):
    timer = Timer()
    
    with timer:
        for _ in iterable:
            pass
        
    return timer.runtime
