long int sum_array(int a[], int N) {
  int i;
  long int sum = 0;
  for(i=0; i<N; i++) {
    sum += *a+i;
  }
  return sum;
}
