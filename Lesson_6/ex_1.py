# Counting Even Numbers
# Write a program that takes a list of numbers as input and counts the number of even numbers in the list. Use a for
# loop, an if statement, and the modulus operator (%) to determine if a number is even or odd.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
count = 0
for n in numbers:
    if n % 2 == 0:
        count = count+1
print(count)