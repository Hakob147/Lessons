# Write a Python function to find the Max of three numbers

def max_of_three(one,two,three):
    if one > two and one > three:
        return one
    if two > one and two > three:
        return two
    if three > one and three > two:
        return three
x = max_of_three(12,10,8)
print(x)