import random

lowest_number = 0
highest_number = 100
random_number = random.randrange(lowest_number, highest_number)
print("I have choosen an integer number between", lowest_number, "and", highest_number)
print("Guess it!")
guessed_number = int(input("Input a number: "))
number_of_tries = 1
while random_number != guessed_number:
  print("Wrong guess :-/")
  if guessed_number < random_number:
    print("Try again with a higher number")
  elif guessed_number > random_number:
    print("Try again with a lower number")
  guessed_number = int(input("Input a number: "))
  number_of_tries = number_of_tries + 1
print("Congratulations!")
print("You guessed the number in", number_of_tries, "attempts :-)")
