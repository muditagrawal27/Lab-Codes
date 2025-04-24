str=input("Enter the string:")
acount=0
numcount=0
for i in str:
    if i.isalpha():
        acount+=1
    if i.isdigit():
        numcount+=1
print("Number of alphabets in the string:",acount)
print("Number of digits in the string:",numcount)