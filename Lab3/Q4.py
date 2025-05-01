def remove_str(str,str1):
    if(str1 in str):
        return str.replace(str1,"")
    else:
        return str
str=input("Enter a string: ")
finder=input("Enter the string to be searched: ")
print("Final String:",remove_str(str,finder))
