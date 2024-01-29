# Count all letters, digits, and special symbols from a given string

#97-122 lower case
#65-90 upper case
#48-57 digits

letters = input("Enter the letters ")
digits = list(range(48,58))
chars = list(range(65,91))+list(range(97,123))

chars_count=0
digits_count=0
symbol_count=0

for n in letters:
    if ord(n) in digits:
        digits_count=digits_count+1
    elif ord(n) in chars:
        chars_count=chars_count+1
    else:
        symbol_count=symbol_count+1

print("chars = ", chars_count)
print("digits = ", digits_count)
print("symbol = ", symbol_count)

