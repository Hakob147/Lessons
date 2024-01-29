# Create a program that will display the numbers from 1 to 50 which is divisible by 5

n = 1
while n < 51:
    if n % 5 == 0:
        print(n)
    n = n + 1