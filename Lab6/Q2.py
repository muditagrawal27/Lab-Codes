lst=[(12,"Mudit",19),
     (13,"Rahul",18),
     (14,"Rohan",19),
     (15,"Rohit",20),
     (16,"Rohini",21),
     (17,"Parthvi",18),
     (18,"Jiya",19) ]
rollno=[]
names=[]
age=[]
for i in lst:
    rollno.append(i[0])
    names.append(i[1])
    age.append(i[2])

print("Roll Numbers:",rollno)
print("Names:",names)
print("Ages:",age)