import json
import logging
import random

from copy import copy
from cpython.object cimport PyObject
from datetime import datetime

import utils
from utils import Timer

AMOUNT = 10000000
NUM_ROUNDS = 100

cdef extern from "Python.h":
    void Py_INCREF(PyObject *)
    PyObject * PyInt_FromLong(long ival)
    list PyList_New(Py_ssize_t size)
    void PyList_SET_ITEM(list l, Py_ssize_t, PyObject *)


cdef void run_cython():
    cdef list results = list()
    total_timer = Timer()


    append_tuple = [i for i in range(AMOUNT)]
    sort_tuple = [random.randint(0,100) for _ in range(AMOUNT)]
    sort_list = [random.randint(0,100) for _ in range(AMOUNT)]

    dict_keys, dict_values = get_dict_keys(AMOUNT)
    shuffled_keys = copy(dict_keys)
    random.shuffle(shuffled_keys)
    dict_one, dict_two = {k: v for k, v in zip(dict_keys, dict_values)}, {v: k for k, v in zip(dict_keys, dict_values)}

    set_one = set(random.randint(0,AMOUNT*2) for _ in range(AMOUNT))
    set_two = set(random.randint(0,AMOUNT*2) for _ in range(AMOUNT))

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START CYTHON TEST CASES\n')
    with total_timer:
        for i in range(NUM_ROUNDS):
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))

            results.append(['dictionary_comprehension', AMOUNT, dict_comprehension(dict_keys, dict_values), 'Cython'])
            results.append(['dictionary_insert', AMOUNT, dictionary_insert(dict_keys, dict_values, shuffled_keys), 'Cython'])
            results.append(['dictionary_merge', AMOUNT, dictionary_merge(dict_one, dict_two), 'Cython'])
            results.append(['read_dictionary_values', AMOUNT, read_dictionary_values(dict_one), 'Cython'])
            results.append(['generator_iter', AMOUNT, generator_run(AMOUNT), 'Cython'])
            results.append(['iteration_test_list', AMOUNT, list_iterator(AMOUNT), 'Cython'])
            results.append(['iteration_test_set', AMOUNT, set_iterator(AMOUNT), 'Cython'])
            results.append(['iteration_test_tuple', AMOUNT, tuple_iterator(AMOUNT), 'Cython'])
            results.append(['list_append', AMOUNT, list_append(AMOUNT), 'Cython'])
            results.append(['list_comprehension', AMOUNT, list_comprehension(AMOUNT), 'Cython'])
            results.append(['list_sort', AMOUNT, list_sort(sort_list), 'Cython'])
            results.append(['set_merge', AMOUNT, set_merge(set_one, set_two), 'Cython'])
            results.append(['tuple_append', AMOUNT, tuple_append(sort_tuple), 'Cython'])
            results.append(['tuple_sort', AMOUNT, tuple_sort(append_tuple), 'Cython'])

        logging.info('FINALIZING CYTHON TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    utils.write_to_csv('cython', results)

cdef tuple get_dict_keys(amount):
    with open(f'c:/code/projects/master-thesis/src/data/json/{str(amount)}_dict_keys.json', 'r') as f:
        keys = json.load(f)

    return keys, [i for i in range(amount)]

cdef float dict_comprehension(list keys, list values):
    timer = Timer()

    with timer:
        dict_ = {key: value for key, value in zip(keys, values)}
    
    return timer.runtime


cdef float dictionary_insert(list keys, list values, list shuffled_keys):
    dict_ = {key: None for key in keys}
    timer = Timer()

    with timer:
        for key, value in zip(shuffled_keys, values):
            dict_[key] = value

    return timer.runtime

cdef float dictionary_merge(dict dict_one, dict dict_two):
    timer = Timer()

    with timer:
        dict_one.update(dict_two)

    return timer.runtime

cdef float read_dictionary_values(dict dict_):
    timer = Timer()

    with timer:
        for key in dict_.keys():
            value = dict_[key]

    return timer.runtime

cdef float generator(int i):
    return i

cdef float generator_run(long amount):
    cdef int i
    running = True
    timer = Timer()
 
    with timer:
        while running:
            for i in range(amount):
                generator(i)
            running = False

    return timer.runtime

cdef float list_iterator(long amount):
    cdef int num
    list_ = [num for num in range(amount)]
    timer = Timer()

    with timer:
        for _ in list_:
            pass

    return timer.runtime

cdef float set_iterator(long amount):
    cdef int num
    cdef set set_ = set(num for num in range(amount))
    timer = Timer()

    with timer:
        for _ in set_:
            pass

    return timer.runtime

cdef float tuple_iterator(long amount):
    cdef int num
    cdef tuple tuple_ = tuple(i for i in range(amount))

    timer = Timer()

    with timer:
        for _ in tuple_:
            pass

    return timer.runtime

cdef float list_comprehension(long amount):
    cdef int i
    timer = Timer()

    with timer:
        list_ = [i for i in range(amount)]

    return timer.runtime

cdef float list_append(list values):
    list_ = list()
    cdef int val
    timer = Timer()

    with timer:
        for val in values:
            list_append(val)
    
    return timer.runtime


cdef float list_sort(list list_):
    timer = Timer()

    with timer:
        sorted_list = sorted(list_)

    return timer.runtime

cdef float set_merge(set set_one, set set_two):
    timer = Timer()

    with timer:
        set_one.update(set_two)

    return timer.runtime

cdef float tuple_append(list values):
    cdef tuple tuple_append
    cdef int val
    timer = Timer()

    with timer:
        for val in values:
            tuple_ += (val,)

    return timer.runtime

cdef float tuple_sort(tuple tuple_):
    cdef tuple sorted_tuple
    timer = Timer()

    with timer:
        sorted_tuple = sorted(tuple_)

    return timer.runtime
