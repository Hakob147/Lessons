# Arrange string characters such that lowercase letters should come first

characters = input("Enter the characters ")
lower_characters = []
upper_characters = []
for n in characters:
    if n.islower():
        lower_characters.append(n)
    elif n.isupper():
        upper_characters.append(n)
lower = "".join(lower_characters)
upper = "".join(upper_characters)

print(lower+upper)

