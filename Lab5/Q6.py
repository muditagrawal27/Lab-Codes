flist=[12,34,56,78,90,23,45,67]
cellist=[]
for i in range(len(flist)):
    cellist.append((flist[i]-32)*5/9)
print("Fahrenheit List: ",flist)
print("Celsius List: ",cellist)