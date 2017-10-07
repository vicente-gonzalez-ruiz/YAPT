#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Python.h>            /* Compulsory in every module */
#include <numpy/arrayobject.h> /* To interact with numpy arrays */
#include "sum_array_lib.c"

static PyObject* sum_array_wrapper(PyObject* self, PyObject* args) {
  int N,i;
  long int sum;
  //int* a;
  PyArrayObject *in_array;
  
  clock_t start, end;
  double cpu_time;

  /*  parse the input */
  //if (!PyArg_ParseTuple(args, "i", &N))
  if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array))
    return NULL;
  /* if the above function returns -1, an appropriate Python exception will
   * have been set, and the function simply returns NULL
   */

  N = PyArray_DIM(in_array, 0);
  printf("array size %d\n", N);

  npy_double* data  = (npy_double*)PyArray_DATA(in_array);
  //a = (int*)malloc(N*sizeof(int));
  //if (!a) return NULL;
  
  /*for(i=0; i<N; i++) {
    data[i] = i;
    }*/

  start = clock();
  sum = sum_array(data, N);
  end = clock();
  cpu_time = ((double) (end - start)) / CLOCKS_PER_SEC;
  cpu_time *= 1000000;
  printf("%f usegs\n", cpu_time);
  
  /*  construct the output (https://docs.python.org/3/c-api/arg.html) */
  return Py_BuildValue("d", sum);
}

/*  define functions in module */
static PyMethodDef module_methods[] = {
  {"sum_array_wrapper", sum_array_wrapper, METH_VARARGS, "Computes the sum of all elements of an array"},
  {NULL, NULL, 0, NULL}
};

/* module initialization */
/* Python version 3*/
static struct PyModuleDef cModPyDem = {
    PyModuleDef_HEAD_INIT,
    "sum_array_module", "Computes the sum of all elements of an array",
    -1,
    module_methods
};

PyMODINIT_FUNC
PyInit_sum_array_module(void) {
    return PyModule_Create(&cModPyDem);
}
