from distutils.core import setup, Extension
import numpy.distutils.misc_util

# define the extension module
sum_array_module = Extension(
    'sum_array_module',
    sources=['sum_array_module.c'],
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs()
)

# run the setup
setup(
    ext_modules=[sum_array_module],
)
