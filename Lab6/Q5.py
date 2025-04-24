lst=[(),(1,2,3,4),(1,),()]
for i in lst:
    if len(i)==0:
        lst.remove(i)
print(lst)