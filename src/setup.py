from setuptools import setup
# from distutils.extension import Extension
from Cython.Build import cythonize
# import numpy

# TODO: Add extensions

# extensions = [
#     # Extension('CPP', ['./cython/cpp_test_cases.pyx'], language='c++'),  # .pyx, lang=C++
#     Extension('Cython', ['./cython/cython_test_cases.pyx']),  # .pyx
# ]

setup(
    ext_modules=cythonize('C:/code/projects/master-thesis/src/cython/cython_test_cases.pyx'),
)
