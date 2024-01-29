# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise

first_number=int(input("Enter the first number "))
second_number=int(input("Enter the second number "))
third_number=int(input("Enter the third number "))
if((first_number>=second_number and second_number>=third_number) or
first_number<=second_number and second_number<=third_number):
    print("Sorted")
else:
    print("Unsorted")