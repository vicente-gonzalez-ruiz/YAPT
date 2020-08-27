import random

# Paso 1
start = 0  # Número más pequeño
stop = 100 # Número más grande
random_number = random.randrange(start, stop)

# Paso 2
guessed_number = int(input(f"Introduce un número entre {start}, {stop}: "))
assert guessed_number >= start and guessed_number <= stop, \
  f"El número introducido {guessed_number} está fuera del intervalo de enteros [{start}, {stop}]"

# Paso 3
number_of_tries = 1
while random_number != guessed_number:

  print("No has adivinado el número :-/")

  # Paso 3.i
  if guessed_number < random_number:
    print("Tu número es muy pequeño")
  elif guessed_number > random_number:
    print("Tu número es muy grande")

  # Paso 3.ii
  guessed_number = int(input("Introduce un número: "))
  number_of_tries = number_of_tries + 1

  print("¡Yúhú!")
print("Has adivinado el número en", number_of_tries, "intentos :-)")
