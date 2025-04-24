angle1=int(input("Enter the angle between side 1 and side 2: "))
angle2=int(input("Enter the angle between side 2 and side 3: "))
angle3=int(input("Enter the angle between side 1 and side 3: "))
if ((angle1+angle2+angle3)==180):
    print("It is a vaild triangle.")
else:
    print("It is not a vaild triangle.")