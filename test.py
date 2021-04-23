from copy import copy, deepcopy

array = [[0, 0],[0, 0]]
copy = deepcopy(array)

print("before")
print(array)
print(copy)

copy[0][0] = 44

print("after")
print(array)
print(copy)