def toggle_case(str):
    str1=""
    for char in str:
        av=ord(char)
        if (65<=av<=90):
            str1+=chr(av+32)
        elif(97<=av<=122):
            str1+=chr(av-32)
        else:
            str1+=char
    return str1

str=input("Enter string: ")
print("Final string:",toggle_case(str))