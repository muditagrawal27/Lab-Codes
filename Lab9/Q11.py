def create_list(l1, l2):
    intersection = list(set(l1) & set(l2))
    return intersection
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(create_list(l1, l2))