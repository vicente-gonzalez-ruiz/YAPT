print("Compruebo si un número es primo")
N = int(input("Introduce un número natural mayor que 2: "))
N_is_prime = True
I = 2
while I <= N//2 - 1:
    print(I, N)
    if N % I == 0:
        N_is_prime = False # I divide a N
        I = N//2
    I = I + 1
print("¿Es", N, "primo?:", N_is_prime)
