def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
a = int(input("Enter the base: "))
b = int(input("Enter the power: "))
res=power(a,b)
print(a,"raised to the power of",b,"is",res)