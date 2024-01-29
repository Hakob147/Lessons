# You are given four real numbers - the coordinates of two points on a
# plane. The first two numbers are the x and y coordinates of the first point,
# and the last two numbers are the x and y coordinates of the second point.
# Output the length of the line segment bounded by the two points.

x1=(input("Enter x1 "))
y1=(input("Enter y1 "))
x2=(input("Enter x2 "))
y2=(input("Enter y2 "))

print(((((float(x2)-float(x1))**2+((float(y2)-float(y1))**2))**0.5)))