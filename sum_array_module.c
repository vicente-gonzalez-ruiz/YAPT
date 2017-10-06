#include <stdlib.h>
#include <Python.h>
#include "sum_array_lib.c"

static PyObject* sum_array_func(PyObject* self, PyObject* args) {
  int N,i;
  long int sum;
  int* a;
  
  /*  parse the input, from python float to c double */
  if (!PyArg_ParseTuple(args, "i", &N))
    return NULL;
  /* if the above function returns -1, an appropriate Python exception will
   * have been set, and the function simply returns NULL
   */

  a = (int*)malloc(N*sizeof(int));
  if (!a) return NULL;
  
  for(i=0; i<N; i++) {
    a[i] = i;
  }

  /* call cos from libm */
  sum = sum_array(a, N);
  
  /*  construct the output, from c double to python float */
  return Py_BuildValue("li", sum);
}

/*  define functions in module */
static PyMethodDef SumArrayMethods[] = {
  {"sum_array_func", sum_array_func, METH_VARARGS, "Computes the sum of all elements of an array"},
  {NULL, NULL, 0, NULL}
};

/* module initialization */
/* Python version 3*/
static struct PyModuleDef cModPyDem = {
    PyModuleDef_HEAD_INIT,
    "sum_array_module", "Some documentation",
    -1,
    SumArrayMethods
};

PyMODINIT_FUNC
PyInit_sum_array_module(void) {
    return PyModule_Create(&cModPyDem);
}
