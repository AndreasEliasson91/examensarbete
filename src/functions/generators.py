import logging
from datetime import datetime
from typing import Any

import utils
from utils import Timer


def generate_generator(values: list) -> Any:
    for val in values:
        yield val

def generator_iter(values: list) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    running: bool = True
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
