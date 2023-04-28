import utils
from utils import Timer

import random


def dictionary_comprehension(keys: list, values: list) -> float:
    t = Timer()

    with t:
        dict_ = {key: value for key, value in zip(keys, values)}

    utils.devnull(dict_)
    return t.runtime

def dictionary_insert(keys: list, values: list) -> float:
    t = Timer()

    dict_ = {key: None for key in keys}
    random.shuffle(keys)

    with t:
        for key, value in zip(keys, values):
            dict_[key] = value

    utils.devnull(dict_)
    return t.runtime

def dictionary_merge(dict_one: dict, dict_two: dict) -> float:
    t = Timer()

    with t:
        dict_one.update(dict_two)

    utils.devnull(dict_one)
    return t.runtime

def read_dictionary_values(dict_: dict) -> float:
    t = Timer()

    with t:
        for key in dict_.keys():
            value = dict_[key]
            utils.devnull(value)

    return t.runtime
