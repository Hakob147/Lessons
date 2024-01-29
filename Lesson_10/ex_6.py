# Write a Python program that takes a positive integer as input and calculates the sum
# of its digits. For example, if the input is 12345, the output should be 15 (1 + 2 + 3 + 4
# + 5 = 15). Use a while loop to perform this task.


m = input("Enter the number ")
sum = 0
n = 0
while n < len(m):
    sum = sum +int(m[n])
    print(m[n],"+ ", end="")
    n = n + 1

print("=",sum)
