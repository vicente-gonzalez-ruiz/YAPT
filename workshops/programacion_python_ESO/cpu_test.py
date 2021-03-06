import time
import sys
import math

def compute_sqrt(input_array):
    output_array = [float]*len(input_array)
    for i in range(len(input_array)):
        output_array = math.sqrt(input_array[i])
    return output_array

if len(sys.argv) < 2:
    print("Give me a number of FLOPS (1000000 for example)")
else:
    n = int(sys.argv[1])
    sequence_of_numbers = [float]*n
    for i in range(n):
        sequence_of_numbers[i] = i
    start = time.time()
    sequence_of_sqrts = compute_sqrt(sequence_of_numbers)
    end = time.time()
    time_taken = end - start
    print(f"The program took {time_taken} seconds to execute {n} square roots")
    print(f"MFLOPS (millions of floating point operations per second) = {n/time_taken/1000000}");
