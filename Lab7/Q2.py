import random
set1={random.randint(15,45) for i in range(10)}
count=0
for i in set1:
    if i<30:
        count+=1
set2={i for i in set1 if i<=35}

print("The original set is: ",set1)
print("The number of elements less than 30 is: ",count)
print("The set after removing elements greater than 35 is: ",set2)