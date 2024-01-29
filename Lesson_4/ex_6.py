#Input two positive integers, and output a line describing their relation.

first_number=input("Enter the first number ")
second_number=input("Enter the second number ")
if first_number>second_number:
    print(first_number,">",second_number)
elif first_number<second_number:
    print(first_number,"<",second_number)
else:
    print(first_number,"=",second_number)