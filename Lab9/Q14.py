def countvowels(s):
    vowels = "aeiouAEIOU"
    if not s:
        return 0
    if s[0] in vowels:
        return 1 + countvowels(s[1:])
    else:
        return countvowels(s[1:])
str = input("Enter a string: ")
print("Number of vowels:", countvowels(str))