import os
import sys
import time


class Timer():
    def __init__(self) -> None:
        self.start = time.time()
        self.runtime = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.runtime = round(end - self.start, 2)

        print(f'The function took {self.runtime} seconds')
        return self.runtime


def test_run() -> None:
    import random

    for _ in range(10):
        time.sleep(random.choice(range(1,5)))



def devnull(x) -> None:
    """
    Function to print to devnull,
    to prevent results from potentially being removed in optimization
    """
    stdout = sys.stdout

    with open(os.devnull, 'w') as f:
        sys.stdout = f

        try:
            print(len(x))
        except TypeError:
            print(x)

    sys.stdout = stdout