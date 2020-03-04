import math
# def binary_search(a, key):
#     return binary_search_index(a, key, 0)
#
#
# def binary_search_index(a, key, inset_index):
#     if len(a) == 0:
#         return -1
#
#     if len(a) == 1:
#         if a[0] == key:
#             return inset_index
#         else:
#             return -1
#
#     index = math.floor(len(a) / 2)
#     if a[index] == key:
#         return index + inset_index
#     elif a[index] < key:
#         return binary_search_index(a[index:], key, inset_index + index)
#     else:
#         return binary_search_index(a[:index], key, inset_index)

def binary_search(a, key):
    if len(a) == 0:
        return -1
    low = 0
    high = len(a) - 1
    while low <= high:
        middle = math.floor((low + high) / 2)
        if a[middle] == key:
            return middle
        elif a[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return -1


array = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
array2 = [1]
array3 = []
# print(binary_search(array, 133))
# print(array[11])
print(binary_search(array, 100))
print(binary_search(array, 222))
print(binary_search(array, 1))
print(binary_search(array3, 1))
