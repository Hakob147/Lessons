# You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
# line segments on a line. Find the length of their intersection. Note that the
# order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
# and [2;1] are considered the same.

a1=float(input("enter a1 "))
a2=float(input("enter a2 "))
b1=float(input("enter b1 "))
b2=float(input("enter b2 "))

if (a1>=b1 and a2 >= b1) and (a1<=b2 and a2 <=b2) or (a1>=b2 and a2 >= b2) and (a1<=b1 and a2 <=b1):
    print(a2-a1)
elif (b1>=a1 and b2 >= a1) and (b1<=a2 and b2 <=a2) or (b1>=a2 and b2 >= a2) and (b1<=a1 and b2 <=a1):
    print(b2-b1)
elif a1<=b1 and a2 <= b1 and a1 <= b2 and a2 <= b2:
    print(0)
elif b1<=a1 and b2 <= a1 and b1<= a2 and b2 <= a2:
    print(0)
elif (a1 < b1 and b1 < a2 and a2 < b2) or (a2 < b1 and b1 < a1 and a1 < b2) or (a1<b2 and b2 < a2 and a2 <b1) or (a2 < b2 and b2 < a1 and a1 <b1):
    print(max(a1,a2)-min(b1,b2))
elif (b1 < a1  and a1< b2 and b2 < a2) or (b2 < a1 and a1 < b1 and b1< a2) or (b1<a2 and a2 < b2 and b2 <a1) or (b2 < a2 and a2 < b1 and b1 <a1):
    print(max(b1, b2) - min(a1, a2))
