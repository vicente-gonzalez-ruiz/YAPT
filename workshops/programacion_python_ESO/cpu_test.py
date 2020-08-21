import numpy
import time
import sys

def work(n):
    for i in range(n):
        x = numpy.sqrt(i)

if len(sys.argv) < 2:
    print("Give me a number of FLOPS")
else:
    n = sys.argv[1]  
    start = time.time()
    work(10000000)
    end = time.time()
    time_taken = end - start
    print("The program took {end} seconds to execute {n} square roots")
    print("MFLOPS (millions of floating point operations per second) = %f\n", n/time_taken/1000000);
    print(end - start)
