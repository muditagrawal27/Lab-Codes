num=int(input("Enter the number of elements in the list: "))
list1=[]
for i in range(num):
    list1.append(input("Enter the element: "))
upset={word.upper() for word in list1}
print("The original list is: ",list1)
print("The set of the list after converting to uppercase is: ",upset)