import random
ranlist = [random.randint(1,30) for i in range(50)]
unique=[]
for i in ranlist:
    if i not in unique:
        unique.append(i)
print("Original List: ",ranlist)
print("Unique List: ",unique)