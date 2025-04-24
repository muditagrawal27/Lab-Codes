def totalprice(pricedict,quantitydict):
    total=0
    for items,quantity in quantitydict.items():
        if items in pricedict:
            itemcost=pricedict[items]*quantity
            total+=itemcost
        print(items,":",pricedict[items],"*",quantitydict[items],"=",itemcost)
    print("The total price of the items is: ",total)

pricedict={'banana':40,'apple':20,'orange':15,'pear':35}
quantitydict={'banana':2,'apple':3,'orange':1,'pear':2}
totalprice(pricedict,quantitydict)