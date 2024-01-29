# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.

import random
random_number = random.randint(1,100)
# print(random_number)
n = 1
while n < 2:
    guess_number = int(input("Guess the number "))
    if guess_number - random_number >= 50:
        print("Too High")
    if 50 > guess_number - random_number >= 25:
        print("High")
    if 25 > guess_number - random_number > 0:
        print("Near high")
    if random_number - guess_number >= 50:
        print("Too Low")
    if 50 > random_number - guess_number >= 25:
        print("Low")
    if 25 > random_number - guess_number > 0:
        print("Near low")
    if guess_number == random_number:
        print("Congratulations !!!, You guess the number")
        break