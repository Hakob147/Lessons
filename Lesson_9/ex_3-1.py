# Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
# columns


#Using ChatGPT

for i in range(6):
    for k in range(i):
        print("* ", end="")
    print()

# Option 2 using one "for" statement
for i in range(6):
        print(i*"* ")