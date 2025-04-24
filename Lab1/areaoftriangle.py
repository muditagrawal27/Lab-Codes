side1=int(input("Enter first side: "))
side2=int(input("Enter second side: "))
side3=int(input("Enter third side: "))
semiper=(side1+side2+side3)/2
area=(semiper*(semiper-side1)*(semiper-side2)*(semiper-side3))**0.5
print("Area of the triangle is: ",area)
