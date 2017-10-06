#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Python.h>
#include "sum_array_lib.c"

static PyObject* sum_array_func(PyObject* self, PyObject* args) {
  int N,i;
  long int sum;
  int* a;
  
  clock_t start, end;
  double cpu_time;

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

  start = clock();
  sum = sum_array(a, N);
  end = clock();
  cpu_time = ((double) (end - start)) / CLOCKS_PER_SEC;
  cpu_time *= 1000000;
  printf("%f usegs\n", cpu_time);
  
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
