set1={'Ashna','Alok','Anshul','Ankit','Abhishek','Bhakti','Bhavna','Bhavya'}
setA={i for i in set1 if i[0]=='A'}
setB={i for i in set1 if i[0]=='B'}
print("The original set is: ",set1)
print("The set of names starting with 'A' is: ",setA)
print("The set of names starting with 'B' is: ",setB)