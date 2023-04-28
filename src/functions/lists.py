import utils
from utils import Timer


def list_comprehension(amount: int) -> float:
    t = Timer()

    with t:
        list_ = [x for x in range(amount)]

    utils.devnull(list_)
    return t.runtime

def list_append(values: list) -> float:
    t = Timer()

    with t:
        list_ = []

        for val in values:
            list_.append(val)
            
    utils.devnull(list_)
    return t.runtime


def list_sort(list_: list) -> float:
    t = Timer()

    with t:
        sorted_list = sorted(list_)
    
    utils.devnull(sorted_list)
    return t.runtime
