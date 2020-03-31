#include <stdio.h>

#define N 10

int main() {
  double a[N];
  int i;
  FILE *ofile = fopen("data.float64", "wb");
  for(i=0; i<N; i++) {
    a[i] = i;
  }
  fwrite(a, sizeof(double), N, ofile);
  fclose(ofile);
  fprintf(stderr,"create_float64: done\n");
}
