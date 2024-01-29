# Count how many even and odd numbers are in given range (10,35)

even_count = 0
for n in range(10,35):
    if n%2==0:
        even_count = even_count + 1
odd_count = len(range(10,35)) - even_count
print(even_count, odd_count)