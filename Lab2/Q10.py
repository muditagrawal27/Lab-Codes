len=int(input("Enter the length of rectangle: "))
bre=int(input("Enter the breadth of rectangle: "))
area=(len*bre)
peri=2*(len+bre)
if area>peri:
    print("Area is greater than perimeter.")
else:
    print("Area is lesser than perimeter.")