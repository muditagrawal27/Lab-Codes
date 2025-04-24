num=int(input("Enter the number:"))
sum=0
ornum=num
noofdigits=len(str(num))
#Prime number
if num<=1:
    print("It is not a prime number.")
else:
    for i in range(2,num):
        if num%i==0:
            print("It is not a prime number.")
            break
        else:
            print("It is a prime number.")
            break
#Perfect number
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")
#Armstrong number
while num>0:
    digit=num%10
    sum+=digit**noofdigits
    num//=10
if sum==ornum:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
#Palindrome number
if (str(num)==str(num)[::-1]):
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")
#Automorphic number
if (str(num**2)==str(num)[-(len(str(num))):]):
    print("It is an automorphic number.")