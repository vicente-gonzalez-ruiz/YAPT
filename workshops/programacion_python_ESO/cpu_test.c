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

void work(int n) {
  int i;
  for(i=0; i<n; i++) {
    float x = sqrt(i);
  }
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    printf("Give me a number of FLOPs");
  } else {
    int n = atoi(argv[1]);
    clock_t t;
    t = clock();
    work(n);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // calculate the elapsed time
    printf("The program took %f seconds to execute %d square roots\n", time_taken, n);
    printf("MFLOPS (millions of floating point operations per second) = %f\n", n/time_taken/1000000);
  }
}
