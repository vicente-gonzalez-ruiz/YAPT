from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("sum_array_lib__cython.pyx"),
)
