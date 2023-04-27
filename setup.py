from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# TODO: Add extensions

extensions = [
    Extension(''),  # .py
    Extension(''),  # .pyx, lang=C++
    Extension(''),  # .pyx
]

setup(ext_modules=cythonize(extensions))
