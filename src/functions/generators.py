import utils
from utils import Timer

from typing import Any


def generate_generator(values: list) -> Any:
    for val in values:
        yield val

def generator_iter(values: list) -> float:
    running: bool = True
    generated_values = generate_generator(values)
    t = Timer()

    with t:
        while running:
            try:
                value = next(generated_values)
                utils.devnull(value)
            except StopIteration:
                running = False

    return t.runtime
