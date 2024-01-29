# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.
n = 1
m = int(input("Enter the number "))
list_1 = [0, 1, 1, 2]
while n < 2:
    if max(list_1) <= m:
        list_1.append(list_1[-1] + list_1[-2])
    else:
        print(sum(list_1)-list_1[-1])
        break