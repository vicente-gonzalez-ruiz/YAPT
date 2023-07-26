from distutils.core import setup
from Cython.Build import cythonize
#import numpy

setup(
    ext_modules=cythonize("Cython/cdef/sum_array_lib.pyx"),
    #include_dirs=[numpy.get_include()]
)
