# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user.

password = "secret"
n=1
while n < 2:
    p = input("Enter the password ")
    if password == p:
        print("Password is correct")
    else:
        continue
    n=n+1