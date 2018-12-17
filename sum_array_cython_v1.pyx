def sum_array_cython(a, N):
    sum = 0
    for i in range(N):
        sum += a[i]
    return sum
