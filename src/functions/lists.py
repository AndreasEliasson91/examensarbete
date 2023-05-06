import logging
import random
from datetime import datetime

import utils
from utils import Timer

random.seed(42)
AMOUNT = 10000000
NUM_ROUNDS = 100

# def run(version: str):
def run(version):
    total_timer = Timer()
    results = list()

    append_list = [i for i in range(AMOUNT)]
    sort_list = [random.randint(0,100) for _ in range(AMOUNT)]

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START LIST TEST CASES FOR V. %s\n', version)
    with total_timer:
        for i in range(NUM_ROUNDS):
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))
            # results.append([f'list_comprehension_{str(i+1)}', list_comprehension(AMOUNT), version])
            results.append([date_time, 'list_comprehension', AMOUNT, list_comprehension(AMOUNT), version])
            # results.append([f'list_append_{str(i+1)}', list_append(append_list), version])
            results.append([date_time, 'list_append', AMOUNT, list_append(append_list), version])
            # results.append([f'list_sort_{str(i+1)}', list_sort(sort_list), version])
            results.append([date_time, 'list_sort', AMOUNT, list_sort(sort_list), version])
        
        logging.info('FINALIZING LIST TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    # utils.write_to_csv('list', results)

# def list_comprehension(amount: int) -> float:
def list_comprehension(amount):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('list_comprehension()')
        list_ = [x for x in range(amount)]

    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(list_)
    return timer.runtime

# def list_append(values: list) -> float:
def list_append(values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    with timer:
        logging.info('list_append()')
        list_ = []

        for val in values:
            list_.append(val)
            
    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(list_)
    return timer.runtime


# def list_sort(list_: list) -> float:
def list_sort(list_):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()


    with timer:
        logging.info('list_sort()')
        sorted_list = sorted(list_)
    
    logging.info('Result:\t%s seconds\n', timer.runtime)
    utils.devnull(sorted_list)
    return timer.runtime
