import logging
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

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START CYTHON TEST CASES\n')
    with total_timer:
        for i in range(NUM_ROUNDS):
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))
            results.append(['list_comprehension', AMOUNT, list_comprehension(AMOUNT), 'Cython'])
            results.append(['list_iterator', AMOUNT, list_iterator(AMOUNT), 'Cython'])
            results.append(['generator', AMOUNT, generator(AMOUNT), 'Cython'])


        logging.info('FINALIZING CYTHON TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    utils.write_to_csv('cython', results)

cdef float dict_comprehension(list keys, list values):
    timer = Timer()

    with timer:
        cdef dict dict_ = {key: value for key, value in zip(keys, values)}
    
    return timer.runtime


cdef float dictionary_insert(list keys, list values, list shuffled_keys):
    cdef dict dict_ = {key: None for key in keys}
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

cdef float generate_generator(long amount):
    cdef int i
    for i in range(amount):
        yield(i)

cdef float generator(long amount):
    running = True
    timer = Timer()
 
    with timer:
        while running:
            for _ in generate_generator(amount):
                pass
            running = False

    return timer.runtime

cdef float list_iterator(long amount):
    cdef int num
    cdef list list_ = [num for num in range(amount)]
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

cdef float list_comprehension(long n):
    cdef int i
    timer = Timer()

    with timer:
        cdef list list_ = [i for i in range(n)]

    return timer.runtime

cdef float list_append(list values):
    cdef list list_ = list()
    cdef int val
    timer = Timer()

    with timer:
        for val in values:
            list_append(val)
    
    return timer.runtime

cdef float list_sort(list list_):
    cdef list sorted_list
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
