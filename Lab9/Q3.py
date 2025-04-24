def create_array(a,b,c,n):
    arr=[[[n for i in range(c)] for j in range(b)] for k in range(a)]
    return arr
a=int(input("Enter Dimension 1: "))
b=int(input("Enter Dimension 2: "))
c=int(input("Enter Dimension 3: "))
n=int(input("Enter initial value of the array: "))
arr=create_array(a,b,c,n)
print("The 3-D array of dimension",a,"x",b,"x",c,"with initial value",n,"is:")
print(arr)
    