def sanitizelist(lst):
    if not lst:
        return []
    first=0 if lst[0]<0 else lst[0]
    return [first]+sanitizelist(lst[1:])
num=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    num.append(ele)
sanitized = sanitizelist(num)
print(sanitized)