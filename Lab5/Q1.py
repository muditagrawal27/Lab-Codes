import random
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
odd=[random.randint(1,100)*2-1 for i in range(5)]
print("Original Odd List: ",odd)
even=[random.randint(1,100)*2 for i in range(4)]
print("Original Even List: ",even)
odd[2]=even
print("Nested List: ",odd)
print("Flattened List: ",flatten(odd))
print("Sorted List: ",sorted(flatten(odd)))