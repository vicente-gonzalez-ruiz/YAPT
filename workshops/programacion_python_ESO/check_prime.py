# Test, for example, 9973

import math

print("+---------------------------------+")
print("| Compruebo si un número es primo |")
print("+---------------------------------+")

N = int(input("Introduce un número natural mayor que 2: "))
assert N>2, f"N={N} (recuerda que el número tiene que ser mayor que 2)"

N_is_prime = True

sqrt_N = int(math.sqrt(N))
sqrt_N_plus_1 = sqrt_N + 1
primes = []

print(f"Rellenando la lista inicial con {sqrt_N_plus_1} enteros ...", end=' ')
for i in range(2, sqrt_N_plus_1):
    primes.append(i)
print("hecho")

print("Cribando ...")
for i in range(2, sqrt_N_plus_1):
    if i in primes:
        for j in range(i*2, sqrt_N_plus_1, i):
            if j in primes:
                print(f"{j}/{sqrt_N_plus_1}", end='\r', flush=True)
                primes.remove(j)
print("\nhecho")
                
print("Probando factores primos", end=' ')
for i in primes:
    print(f"{i}", end=' ', flush=True)
    if N % i == 0:
        N_is_prime = False # porque i divide a N
        break
print()

print("¿Es", N, "primo?:", N_is_prime)
