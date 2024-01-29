# Ex_1
# def file_not_found(filename):
#     try:
#         open(filename)
#     except FileNotFoundError as e:
#         print(f"File not found: {e}")
#
# a = file_not_found("45.txt")
#
# # Ex_2
# def zero_division_error(number, divided_number):
#     try:
#         print(number/divided_number)
#     except ZeroDivisionError as e:
#         print(f"The number cannot divide to zero: {e}")
#
# a = zero_division_error(5,0)

# # Ex3
# def invalid_syntax(filename):
#     with open(filename) as file:
#         content = file.read()
#         if content[0].isdigit():
#             raise Exception("Invalid File")
#         print(content)
#
# a = invalid_syntax("test_1.txt")

