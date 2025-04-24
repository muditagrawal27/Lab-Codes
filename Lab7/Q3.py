set1=set()
for i in range(5):
    ele=input("Enter the element: ")
    set1.add(ele)
print("The original set is: ",set1)
modifiyele=input("Enter the element to be modified: ")
newele=input("Enter the new element: ")
set1.remove(modifiyele)
set1.add(newele)
print("The modified set is: ",set1)
for i in range(2):
    delele=input("Enter the element to be deleted: ")
    set1.remove(delele)
print("The set after deletion is: ",set1)

