# Write a Python program that prints all
# the numbers from 0 to 7 except 3 and 6

for n in range(0, 8):
    if n == 3 or n == 6:
        continue
    print(n)