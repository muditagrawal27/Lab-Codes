def compute(n):
    for i in range(n,n+4):
        sum=i+i*i+i**3+i**4
        print(sum)
n=int(input("Enter a number: "))
compute(n)
