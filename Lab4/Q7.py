import math
n=int(input("Enter the number of items: "))
r=int(input("Enter the number of items to choose and permute: "))
if n<r:
    print("Invalid input.")
else:
    nPr= math.factorial(n)/math.factorial(n-r)
    nCr=math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    print("nCr is:",nCr)
    print("nPr is:",nPr)
    