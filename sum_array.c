#include <stdio.h>
#include <time.h>
#include "sum_array_lib.c"

#define N 100000

int main() {
  int a[N];
  int i;
  clock_t start, end;
  double cpu_time;
  for(i=0; i<N; i++) {
    a[i] = i;
  }
  start = clock();
  long int sum = sum_array(a,N);
  end = clock();
  printf("%ld ", sum);
  cpu_time = ((double) (end - start)) / CLOCKS_PER_SEC;
  cpu_time *= 1000000;
  printf("%f usegs\n", cpu_time);
}
