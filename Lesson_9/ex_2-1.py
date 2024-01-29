# Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
# columns


# #Using ChatGPT
for i in range(5):
    for j in range(5):
        print("* ", end=" ")
    print()

# Option 2 using one "for" statement
for i in range(5):
    print(5*"* ")