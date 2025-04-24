def convert(str):
    words = str.split()
    unique = set(words)
    sorted = sorted(unique)
    result = ' '.join(sorted)
    return result
str = input("Enter a string: ")
print(convert(str))
