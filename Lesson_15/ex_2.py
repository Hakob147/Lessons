# Write a python function which will get a number and check is
# your number great or equal the random number of computer (10-100)if yes print True otherwise False.

import random
def random_check(number):
    result = False
    if number >= random.randint(10,100):
        result = True
    return result

y = random_check(60)
print(y)
