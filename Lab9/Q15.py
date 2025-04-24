def revlist(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + revlist(lst[:-1])
lst=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    lst.append(ele)
revlst= revlist(lst)
print(revlst)