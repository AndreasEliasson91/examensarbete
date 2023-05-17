import os
import sys

import csv
import json
import logging
import random
import string
import time

from datetime import datetime


class Timer():
    def __init__(self):
        self.start = time.time()
        self.runtime = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.runtime = end - self.start
        return self.runtime


def devnull(x):
    """
    Print to devnull.
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

def generate_dict_keys(amount: int) -> None:
    strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(amount)]

    with open(f'src/data/json/{amount}_dict_keys.json', 'w', encoding='utf-8') as f:
        json.dump(strings, f)

def range_sequence(start, stop, step):
    result = list(zip(range(start, stop, step), range(start+step, stop, step)))
    if (stop - start) % step != 0:
        last_fst_elem = result[-1][-1] if result else start
        result.append((last_fst_elem, stop))
    return result

def write_to_csv(datatype, results):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('Writing %s results to csv\n', datatype)

    with open('../doc/results/timer/{0}_results_100.csv'.format(datatype), 'a', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        for line in results:
            writer.writerow(line)
