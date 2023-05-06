import logging
from datetime import datetime
# from typing import Any

import utils
from utils import Timer

AMOUNT = 1000000
NUM_ROUNDS = 10

# def run(version: str):
def run(version):
    total_timer = Timer()
    results = list()
    values = [i for i in range(AMOUNT)]

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START GENERATOR TEST CASES FOR V. %s\n', version)

    with total_timer:
        for i in range(NUM_ROUNDS):
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))
            # results.append([f'generator_iter_{str(amount)}', generator_iter([i for i in range(amount)]), version])
            results.append([date_time, 'generator_iter', AMOUNT, generator_iter(values), version])
        
        logging.info('FINALIZING GENERATOR TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    # utils.write_to_csv('generator', results)

# def generate_generator(values: list) -> Any:
def generate_generator(values):
    for val in values:
        yield val

# def generator_iter(values: list) -> float:
def generator_iter(values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timer = Timer()

    running = True
    generated_values = generate_generator(values)

    with timer:
        logging.info('generator_iter()')
        
        while running:
            try:
                value = next(generated_values)
                utils.devnull(value)
            except StopIteration:
                running = False

    logging.info('Result:\t%s seconds\n', timer.runtime)
    return timer.runtime
