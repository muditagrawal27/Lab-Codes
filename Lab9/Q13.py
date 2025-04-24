def binary(num):
    if num > 1:
        binary(num // 2)
    print(num % 2, end='')
num = int(input("Enter a positive integer: "))
binary(num)
