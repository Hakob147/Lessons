# Write a program that calculates the sum of numbers from 1 to a user-defined limit using a while loop

# Option 1
n = 1
sum = 0
m = int(input("Enter the end number " ))
while n < m:
    sum = (1+m) * (m/2)
    n = n + 1
print(sum)

# Option 2
n = 1
sum = 0
m = int(input("Enter the end number " ))
while n <= m:
    sum = sum + n
    n = n + 1
print(sum)