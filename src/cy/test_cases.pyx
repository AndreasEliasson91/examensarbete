import logging
from cpython.object cimport PyObject
from datetime import datetime

import utils
from utils import Timer

cdef extern from "Python.h":
    void Py_INCREF(PyObject *)
    PyObject * PyInt_FromLong(long ival)
    list PyList_New(Py_ssize_t size)
    void PyList_SET_ITEM(list l, Py_ssize_t, PyObject *)

def list_comprehension(long n) -> float:
    cdef long i
    timer = Timer()

    with timer:
        list_ = [i for i in range(n)]
    
    return timer.runtime
        

def list_iterator(long n):
    cdef long i
    cdef list T = PyList_New(n)
    timer = Timer()

    with timer:
        for i in range(n):
            PyList_SET_ITEM(T, i, PyInt_FromLong(i))
    
    return timer.runtime


def cython_run() -> None:
    results = list()
    amounts = [10000, 500000, 1000000]
    print('Hej')

    for amount in amounts:
        results.append(['list_comprehension_{0}'.format(str(amount)), list_comprehension(amount), 'Cython'])
        results.append(['list_iterator_{0}'.format(str(amount)), list_iterator(amount), 'Cython'])

    utils.write_to_csv('cython', results)

cython_run()
