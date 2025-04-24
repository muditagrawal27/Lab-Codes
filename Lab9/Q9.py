def count_alpha_digits(str):
    result = {'alphabets': 0, 'digits': 0}
    for i in str:
        if i.isalpha():
            result['alphabets'] += 1
        elif i.isdigit():
            result['digits'] += 1
    return result
str = input("Enter a string: ")
print(count_alpha_digits(str))