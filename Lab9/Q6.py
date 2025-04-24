def cubes(x):
    for i in range(1,x+1):
        print(tuple([i,i**2,i**3]))
x=int(input("Enter a number: "))
cubes(x)