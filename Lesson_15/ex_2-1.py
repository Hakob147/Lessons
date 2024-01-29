# Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers,
# and symbols)

import random
import string

def password_generator(length):
    result = ""
    for i in range(length):
        result += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return result

x  = password_generator(10)
print(x)
