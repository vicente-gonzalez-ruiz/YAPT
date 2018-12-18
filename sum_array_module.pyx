cdef extern from "sum_array_lib.c":
    double sum_array(int N)

def sum_array_func(N):
    return sum_array(N)
