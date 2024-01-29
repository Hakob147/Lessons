# Write a python program which will check is your number equal
# the random number of computer (1-10)if yes print True otherwise False.
import random
def random_check(number):
    result = False
    if number == random.randint(1,10):
        result = True
    return result
# x = random_check(int(input()))
x = random_check(5)
print(x)