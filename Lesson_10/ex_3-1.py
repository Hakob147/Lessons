# Write a Python program that calculates the sum of all even numbers between 1 and 100
# using a while loop

n= 0
sum = 0
while n < 101:
    if n % 2 == 0:
        sum = sum + n
    n = n + 1
print(sum)