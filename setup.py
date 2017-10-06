from distutils.core import setup, Extension

# define the extension module
sum_array_module = Extension('sum_array_module', sources=['sum_array_module.c'])

# run the setup
setup(ext_modules=[sum_array_module])
