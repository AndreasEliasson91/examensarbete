import utils

from timer import Timer


def comprehension(amount: int) -> float:
    t = Timer()

    with t:
        list_ = [x for x in range(amount)]

    utils.devnull(list_)
    return t.runtime

def append(values: list) -> float:
    t = Timer()

    with t:
        list_ = list()

        for val in values:
            list_.append(val)
            
    utils.devnull(list_)
    return t.runtime


def sort(list_: list) -> float:
    t = Timer()

    with t:
        sorted_list = sorted(list_)
    
    utils.devnull(sorted_list)
    return t.runtime
