lst1=[1,2,3,4,5,6,7,8,9]
lst2=[10,11,12,3,4,5,6,43,14]
lst3=[]
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print("List 1: ",lst1)
print("List 2: ",lst2)
print("List 3: ",lst3)
