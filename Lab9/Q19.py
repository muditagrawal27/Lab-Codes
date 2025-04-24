def recursive_length(s):
    if s == "":
        return 0
    return 1 + recursive_length(s[1:])
str=input("Enter a string: ")
print("Length of the string is",recursive_length(str))