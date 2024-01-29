# Develop a program that checks if a given number is prime using a while loop. Ask
# the user for input and print whether the number is prime or not.

m = int(input("Enter the number "))
result = True
for n in range(2,round((m ** 0.5)+1)):
    if m % n == 0:
        result = False
print(result)