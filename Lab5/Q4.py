import random
ranlist = [random.randint(-10000,10000) for i in range(30)]
positive=[]
negative=[]
for i in ranlist:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
print("Original List: ",ranlist)
print("Positive List: ",positive)
print("Negative List: ",negative)
