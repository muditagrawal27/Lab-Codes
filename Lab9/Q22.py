import random 
rannum=random.sample(range(-15, 16),10)
sqrnum = [num ** 2 for num in rannum]
print("Random Numbers:", rannum)
print("Squared Numbers:", sqrnum)