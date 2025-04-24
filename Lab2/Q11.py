x1=int(input("Enter x coordinates of first point: "))
y1=int(input("Enter y coordinates of first point: "))
x2=int(input("Enter x coordinates of second point: "))
y2=int(input("Enter y coordinates of second point: "))
x3=int(input("Enter x coordinates of third point: "))
y3=int(input("Enter y coordinates of third point: "))
s12=(y2-y1)/(x2-x1)
s23=(y3-y2)/(x3-x2)
s13=(y3-y1)/(x3-x1)
if (s12==s23==s13):
    print("The points are collinear.")
else:
    print("The points are not collinear.")