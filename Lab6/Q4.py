foodmenu=[("Burger", 150), ("Fries", 100), ("Coke", 60), ("Pizza", 200), ("Sandwich", 100)]
sortedmenu=sorted(foodmenu, key=lambda x: x[1],reverse=True)
print("Food Prices in descending order:")
for i in sortedmenu:
    print(i[0],":",i[1])