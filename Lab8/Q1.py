def add(d1,d2,d3):
    d4={**d1,**d2,**d3}
    print("First Dictionary: ",d1)
    print("Second Dictionary: ",d2)
    print("Third Dictionary: ",d3)
    print("Merged Dictionary: ",d4)
    return d4
d1={'a1':1,'a2':2,'a3':3}
d2={'b1':4,'b2':5,'b3':6}
d3={'c1':7,'c2':8,'c3':9}
add(d1,d2,d3)