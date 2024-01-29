# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

salaries=[int(input("Enter the first employee salary ")), int(input("Enter the second employee salary ")),
          int(input("Enter the third employee salary "))]
print(max(salaries)-min(salaries))