from cpython cimport array
import array

#import numpy as np
#cimport numpy as np

def sum_array(double[:] a, int N):
    cdef double sum = 0.0
    cdef int i = 0
    while i<N:
        sum += a[i]
        i += 1
    return sum

#def sum_array(np.ndarray a, int N):
#    cdef double sum = 0.0
#    cdef int i = 0
#    while i<N:
#        sum += a[i]
#        i += 1
#    return sum
