def ispalindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
s=input("Enter a string: ")
if ispalindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")