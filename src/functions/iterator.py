import logging
from datetime import datetime

import utils
from utils import Timer


# def run(version: str):
def run(version):
    results = list()
    amounts = [1000000, 50000000, 100000000]

    for amount in amounts:
        # results.append([f'iteration_test_set_{str(amount)}', iteration_test(set(i for i in range(amount))), version])
        results.append(['iteration_test_set_{0}'.format(str(amount)), iteration_test(set(i for i in range(amount))), version])
        # results.append([f'iteration_test_tuple_{str(amount)}', iteration_test(tuple(i for i in range(amount))), version])
        results.append(['iteration_test_tuple_{0}'.format(str(amount)), iteration_test(tuple(i for i in range(amount))), version])
        # results.append([f'iteration_test_list_{str(amount)}', iteration_test(list(i for i in range(amount))), version])
        results.append(['iteration_test_list_{0}'.format(str(amount)), iteration_test(list(i for i in range(amount))), version])

    # utils.write_to_csv('iterator', results)

# def iteration_test(iterable: iter) -> float:
def iteration_test(iterable):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()
    
    with timer:
        logging.info('Start iteration_test() on %s with %s elements', type(iterable), len(iterable))

        for _ in iterable:
            pass

        logging.info('Finalizing iteration_test()')

    logging.info('Result:\t%s seconds\n', timer.runtime)
    return timer.runtime
