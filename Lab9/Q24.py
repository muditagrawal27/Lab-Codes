fac=[]
n=int(input("Enter the number of faculty members: "))
for i in range(n):
    name=input("Enter the name of the faculty member: ")
    fac.append(name)
filtered=[]
for i in fac:
    if len(i)>8:
        filtered.append(i)
print("Filtered Names:", filtered)