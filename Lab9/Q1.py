def count_upper_lower(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return {"uppercase": upper, "lowercase": lower}
str=input("Enter a string: ")
result = count_upper_lower(str)
print(result)