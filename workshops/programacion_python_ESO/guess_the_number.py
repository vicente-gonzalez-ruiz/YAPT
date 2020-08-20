import random

lowest_number = 0
highest_number = 100
random_number = random.randrange(lowest_number, highest_number)
print("He elegido un número entero entre", lowest_number, "y", highest_number)
print("Adivínalo!")
guessed_number = int(input("Introduce un número: "))
assert guessed_number >= lowest_number and guessed_number <= highest_number, \
  f"El número introducido {guessed_number} está fuera del intervalo de enteros [{lowest_number}, {highest_number}]"
number_of_tries = 1
while random_number != guessed_number:
  print("No has adivinado el número :-/")
  if guessed_number < random_number:
    print("Inténtalo de nuevo con un valor más alto")
  elif guessed_number > random_number:
    print("Inténtalo de nuevo con un valor más bajo")
  guessed_number = int(input("Introduce un número: "))
  number_of_tries = number_of_tries + 1
print("¡Felicidades!")
print("Has adivinado el número en", number_of_tries, "intentos :-)")
