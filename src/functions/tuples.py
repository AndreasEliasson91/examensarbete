import utils
from utils import Timer


def tuple_append(values: list) -> float:
    t = Timer()

    with t:
        tuple_ = tuple()

        for val in values:
            tuple_ += (val,)

    utils.devnull(tuple_)
    return t.runtime

def tuple_sort(tuple_: tuple) -> float:
    t = Timer()

    with t:
        sorted_tuple = tuple(sorted(tuple_))

    utils.devnull(sorted_tuple)
    return t.runtime
