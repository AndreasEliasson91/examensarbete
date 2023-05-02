from setuptools import setup
# from distutils.extension import Extension
from Cython.Build import cythonize

# TODO: Add extensions

# extensions = [
#     Extension(''),  # .py
#     Extension(''),  # .pyx, lang=C++
#     Extension(''),  # .pyx
# ]

setup(ext_modules=cythonize('C:/code/projects/master-thesis/src/cy/test_cases.pyx'))
