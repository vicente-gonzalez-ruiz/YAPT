import numpy
import time
import sys

def compute_sqrt(input_array):
    return numpy.sqrt(input_array)

if len(sys.argv) < 2:
    print("Give me a number of FLOPS (100000000 for example)")
else:
    n = int(sys.argv[1])
    sequence_of_numbers = numpy.arange(n)
    start = time.time()
    sequence_of_sqrts = compute_sqrt(sequence_of_numbers)
    end = time.time()
    time_taken = end - start
    print(f"The program took {time_taken} seconds to execute {n} square roots")
    print(f"MFLOPS (millions of floating point operations per second) = {n/time_taken/1000000}");
