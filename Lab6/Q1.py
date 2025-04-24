bcount=gcount=0
lst=['girl1','girl2','girl3',('boy1','boy2','boy3',)]
for i in lst:
    if isinstance(i,tuple):
        for j in i:
            bcount+=1
    else:
        gcount+=1
print("Number of Boys:",bcount)
print("Number of Girls:",gcount)