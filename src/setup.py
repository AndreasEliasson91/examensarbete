from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

# TODO: Add extensions

extensions = [
    Extension('CPP', ['./cython/cpp_test_cases.pyx'], language='c++'),  # .pyx, lang=C++
    # Extension('Cython', ['./cython/cython_test_cases.pyx']),  # .pyx
]

setup(
    name='CPP',
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)
