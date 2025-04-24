import math
x=int(input("Enter x coordinate of center of circle: "))
y=int(input("Enter y coordinate of center of circle: "))
rad=int(input("Enter radius of circle: "))
x1=int(input("Enter x coordinate of the point: "))
y1=int(input("Enter y coordinate of the point: "))
d=math.sqrt((x1-x)**2 - (y1-y)**2)
if(d>rad):
    print("The point is outside the circle.")
elif(d==rad):
    print("The point lies on the circle.")
else:
    print("The point is inside the circle.")