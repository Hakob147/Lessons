# Display the numbers from 1 to 10 except 6.

n = 1
while n < 11:
    if n == 6:
        n = n + 1
        continue
    print(n)
    n = n + 1