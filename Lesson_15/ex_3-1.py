# Write a function that will get a function string and check if the password is strong or not.
# Strong password must contain | One uppercase letter | one special symbol | one number
# Length of the password should be 8 or more
# If your password is Strong you will return True. else return False

import random
import string

def password_checker(password):
    if len(password) < 8:
        raise Exception("Length of the password should be 8 or more")
    result = False
    for i in password:
        if i in string.punctuation and string.digits and string.ascii_uppercase:
            result = True
    return result

password = password_checker("1aAdsdf=h")
print(password)
