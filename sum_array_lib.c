double sum_array(double* a, int N) {
  int i;
  double sum = 0;
  for(i=0; i<N; i++) {
    sum += *a+i;
  }
  return sum;
}
