def ispangram(s):
    charset=set(s.lower())
    alphaset=set("abcdefghijklmnopqrstuvwxyz")
    return charset>=alphaset
s=input("Enter a string: ")
if ispangram(s):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")