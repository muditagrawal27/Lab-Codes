num=int(input("Enter the number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("Factorial of",num,"is",factorial)