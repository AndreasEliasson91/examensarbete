import os
import sys
import time

from typing import Any


class Timer():
    def __init__(self) -> None:
        self.start = time.time()
        self.runtime = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.runtime = end - self.start

        print(f'The function took {self.runtime} seconds')
        return self.runtime


def devnull(x: Any) -> None:
    """
    Po print to devnull.
    Used to prevent results from potentially being removed in optimization
    """
    stdout = sys.stdout

    with open(os.devnull, 'w') as f:
        sys.stdout = f

        try:
            print(len(x))
        except TypeError:
            print(x)

    sys.stdout = stdout

def range_sequence(start: int, stop: int, step: int):
    result = list(zip(range(start, stop, step), range(start+step, stop, step)))
    if (stop - start) % step != 0:
        last_fst_elem = result[-1][-1] if result else start
        result.append((last_fst_elem, stop))
    return result

