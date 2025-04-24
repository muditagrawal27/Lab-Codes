num=int(input("Enter number of elements in tuple: "))
lst=[]
for i in range(num):
    a=int(input("Enter element: "))
    lst.append(a)
tuple1=tuple(lst)
print("Original Tuple: ",tuple1)
eleindex=int(input("Enter index of element to be removed: "))
lst1=list(tuple1)
lst1.pop(eleindex)
tuple2=tuple(lst1)
print("Tuple after removing element: ",tuple2)