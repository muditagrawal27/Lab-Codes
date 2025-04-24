num=int(input("Enter the number:"))
ornum=num
noofdigits=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum+=digit**noofdigits
    num//=10
if sum==ornum:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")