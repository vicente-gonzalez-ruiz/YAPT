import math

print("+---------------------------------+")
print("| Compruebo si un número es primo |")
print("+---------------------------------+")

N = int(input("Introduce un número natural mayor que 2: "))
assert N>2, f"N={N} (recuerda que el número tiene que ser mayor que 2)"

N_is_prime = True

sqrt_N = int(math.sqrt(N))
sqrt_N_plus_1 = sqrt_N + 1
print(sqrt_N)
primes = []
for i in range(2, sqrt_N_plus_1):
    primes.append(i)

for i in range(2, sqrt_N_plus_1):
    if i in primes:
        for j in range(i*2, sqrt_N_plus_1, i):
            if j in primes:
                primes.remove(j)
print(f"lista de números primos menores o iguales que {sqrt_N}: {primes}")

for i in primes:
    if N % i == 0:
        N_is_prime = False # porque i divide a N
        break

print("¿Es", N, "primo?:", N_is_prime)
