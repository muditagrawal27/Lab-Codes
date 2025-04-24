lst = ['madam', 'Python', 'malayalam', 12321]
def ispalindrome(s):
    s=str(s)
    return s == s[::-1]
for item in lst:
    if ispalindrome(item):
        print(item)