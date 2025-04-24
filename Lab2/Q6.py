num=int(input("Enter the number: "))
count=0
if num==0:
    print("Number of digits: 1")
else:
    while num>0:
        num//=10
        count+=1
print("Number of digits:",count)