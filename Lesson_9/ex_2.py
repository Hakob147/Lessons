# Get the same items in two ranges using
# nested loop.(0, 10), (5,15)

range_1 = range(0,11)
range_2 = range(5,16)

for n in range_1:
    if n in range_2:
        print(n)