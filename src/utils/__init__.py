import os
import sys
import logging
import time
from datetime import datetime

# from typing import Any


class Timer():
    # def __init__(self) -> None:
    def __init__(self):
        self.start = time.time()
        self.runtime = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.runtime = end - self.start
        return self.runtime


# def devnull(x: Any) -> None:
def devnull(x):
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

# def range_sequence(start: int, stop: int, step: int) -> list:
def range_sequence(start, stop, step):
    result = list(zip(range(start, stop, step), range(start+step, stop, step)))
    if (stop - start) % step != 0:
        last_fst_elem = result[-1][-1] if result else start
        result.append((last_fst_elem, stop))
    return result

# def write_to_csv(datatype: str, results: list) -> None:
def write_to_csv(datatype, results):
    import csv

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('Writing %s results to csv', datatype)
    # with open(f'c:/code/projects/master-thesis/doc/results/{datatype}_results.csv', 'a') as csv_file:
    with open('c:/code/projects/master-thesis/doc/results/{0}_results.csv'.format(datatype), 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        for line in results:
            writer.writerow(line)

    logging.info('%s done!\n', datatype)
