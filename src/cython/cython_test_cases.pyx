import logging
from cpython.object cimport PyObject
from datetime import datetime

import utils
from utils import Timer

AMOUNT = 1000000
NUM_ROUNDS = 10

cdef extern from "Python.h":
    void Py_INCREF(PyObject *)
    PyObject * PyInt_FromLong(long ival)
    list PyList_New(Py_ssize_t size)
    void PyList_SET_ITEM(list l, Py_ssize_t, PyObject *)

def list_comprehension(long n) -> float:
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cdef long i
    timer = Timer()

    with timer:
        logging.info('list_comprehension()')
        list_ = [i for i in range(n)]

    logging.info('Result:\t%s seconds\n', timer.runtime)
    
    return timer.runtime
        

def list_iterator(long n):
    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cdef long i
    cdef list T = PyList_New(n)
    timer = Timer()

    with timer:
        logging.info('list_iterator()')

        for i in range(n):
            PyList_SET_ITEM(T, i, PyInt_FromLong(i))

    logging.info('Result:\t%s seconds\n', timer.runtime)
    
    return timer.runtime


def cython_run() -> None:
    total_timer = Timer()
    results = list()

    logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('START CYTHON TEST CASES\n')
    with total_timer:
        for i in range(NUM_ROUNDS):
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logging.info('Round %s of %s\n', str(i+1), str(NUM_ROUNDS))
            results.append([date_time, f'list_comprehension_{str(i+1)}', AMOUNT, list_comprehension(AMOUNT), 'Cython'])
            results.append([date_time, f'list_iterator_{str(i+1)}', AMOUNT, list_iterator(AMOUNT), 'Cython'])


        logging.info('FINALIZING CYTHON TEST CASES')
    logging.info('Total time elapsed:\t%s seconds\n', total_timer.runtime)
    utils.write_to_csv('cython', results)

