def avg(numbers, total=0, count=0):
    if not numbers:
        if count != 0:
            return total / count 
        else:
            return 0  
    return avg(numbers[1:], total + numbers[0], count + 1)
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    ele = int(input("Enter the element: "))
    numbers.append(ele)
print("Average:",avg(numbers))