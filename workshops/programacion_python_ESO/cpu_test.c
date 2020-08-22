/*
  Measure the number of millions of floating point operations per
  second (MFLOPS). The Square Root operation is performed.

  Compile with: gcc cpu_test.c -o cpu_test -lm
  Try with: ./cpu_test 100000000
*/

#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

float *compute_sqrts(float *input_array, int length) {
  int i;
  float *output_array = (float *)malloc(length * sizeof(float));
  for(i=0; i<length; i++) {
    output_array[i] = sqrt(input_array[i]);
  }
  return output_array;
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    printf("Give me a number of FLOPs (100000000 for example)");
  } else {
    int n = atoi(argv[1]), i;
    float *input_array = (float *)malloc(n * sizeof(float));
    for (i=0; i<n; i++) {
      input_array[i] = i;
    }
    clock_t t;
    t = clock();
    float *output_array = compute_sqrts(input_array, n);
    t = clock() - t;
    free(input_array);
    free(output_array);
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // calculate the elapsed time
    printf("The program took %f seconds to execute %d square roots\n", time_taken, n);
    printf("MFLOPS (millions of floating point operations per second) = %f\n", n/time_taken/1000000);
  }
}
