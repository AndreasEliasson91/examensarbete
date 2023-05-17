from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension('CPP', ['./cpp/cpp_test_cases.pyx'], language='c++'),  # .pyx, lang=C++
    Extension('Cython', ['./cython/cython_test_cases.pyx']),  # .pyx
]

setup(
    ext_modules=cythonize(extensions),
)
