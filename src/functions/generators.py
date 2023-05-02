import logging
from datetime import datetime
# from typing import Any

import utils
from utils import Timer


# def run(version: str):
def run(version):
    results = list()
    amounts = [10000, 500000, 1000000]

    for amount in amounts:
        # results.append([f'generator_iter_{str(amount)}', generator_iter([i for i in range(amount)]), version])
        results.append(['generator_iter_{0}'.format(str(amount)), generator_iter([i for i in range(amount)]), version])

    # utils.write_to_csv('generator', results)

# def generate_generator(values: list) -> Any:
# def generate_generator(values: list):
def generate_generator(values):
    for val in values:
        yield val

# def generator_iter(values: list) -> float:
def generator_iter(values):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # running: bool = True
    running = True
    generated_values = generate_generator(values)
    timer = Timer()

    with timer:
        logging.info('Start generator_iter() with %s elements', len(values))
        
        while running:
            try:
                value = next(generated_values)
                utils.devnull(value)
            except StopIteration:
                logging.info('Finalizing generator_iter()')
                running = False

    logging.info('Result:\t%s seconds\n', timer.runtime)
    return timer.runtime
