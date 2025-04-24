import random
ranlist = [random.randint(1,20) for i in range(20)]
num=int(input("Enter a number: "))
found=False
print(ranlist)
for i in range(20):
    if ranlist[i]==num:
        print("Number found at index: ",i)
        found=True
if not found:
    print("Number not found.")
        