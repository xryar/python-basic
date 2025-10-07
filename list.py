# list with vertical declaration
list_2 = [
    "ab",
    "cd",
    "ef",
    "gh",
]

# list with another data types
list_3 = [3.14, "hello python", True, False]

# empty list
list_4 = []

# for list
for e in list_2:
    print("elem:", e)

# with index
for i in range(0, len(list_2)):
    print("index:", i, "elem:", list_2[i])

# enumerate func
for i, v in enumerate(list_2):
    print("index", i, "elem", v)

# nested list
matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()

# convert to list

# range to list
range_1 = range(0, 10)
list_1 = list(range_1)
print(list_1)

range_2 = range(0, 22, 3)
list_2 = list(range_2)
print(list_2)

range_3 = range(100, 0, -10)
list_3 = list(range_3)
print(list_3)

# string to list
alphabets = "abcdefghijk" 
list_4 = list(alphabets)
print(list_4)

# tuple to list
tuple_1 = (1, 2, 3, 4)
list_5 = list(tuple_1)
print(list_5)

# operation on list
# access element via index
list_1 = [1, 2, 3]
elem_1 = list_1[0]
elem_2 = list_1[1]
elem_3 = list_1[2]
print(elem_1, elem_2, elem_3)

# check if element is exist in list
list_1 = [1, 2, 3, 4]
n = 2

if n in list_1:
    print(n, "is exist")
else:
    print(n, "is not exist")

# slicing
list_2 = ["ab", "cd", "ef", "gh"]
print("list_2", list_2)

list_1 = list_2[1:3]
print("slice 1", list_1)

# change value in list
list_1 = ['ac', 'bc', 'dc', "uc"]
print("before", list_1)

list_1[1] = "cd"
list_1[3] = "ad"
print("after", list_1)

# append element
# via method
list_1 = [10, 70, 20]
print("before", list_1)

list_1.append(88)
list_1.append(98)
print("after with method", list_1)

# via slicing
list_1 =[10, 70, 20]
print("before", list_1)

list_1[len(list_1):] = [88, 87]
print("after with slicing", list_1)

# extend or union
# via method
list_1 = [11, 22]
list_2 = [33, 44]
list_1.extend(list_2)
print("extend with method", list_1)

# via slicing
list_1 = [11, 22]
list_2 = [33, 44]
list_1[len(list_1):] = list_2
print("extend with slicing", list_1)

# via operator
list_1 = [11, 22]
list_2 = [33, 44]
list_3 = list_1 + list_2
print("extend with operator", list_3)

# Insert element at specific index
list_3 = [10, 20, 30, 40, 50]
list_3.insert(0, 90)
print(list_3)
list_3.insert(2, 80)
print(list_3)

# remove an element
list_3 = [10, 70, 20, 70]

list_3.remove(70)
print(list_3)

list_3.remove(70)
print(list_3)

# remove an element at specific index
# you can choose between pop or del
list_3 = [10, 70, 20, 70]
x = list_3.pop(2)
print("list_3:", list_3)
print("removed element:", x)

x = list_3.pop()
print("list_3:", list_3)
print("removed element:", x)

# range delete
list_3 = [10, 70, 20, 70]

del list_3[1:3]
print(list_3)

# calculate element
list_3 = [10, 70, 20, 70]
print(len(list_3))

count = list_3.count(70)
print("jumlah element dengan data `70`:", count)

# find index element
list_2 = ['ab', 'cd', 'hi', 'ca']

idx_1st = list_2.index("cd")
print("index", idx_1st)

# clear list
# you can choose how to clear a list with clear(), [] or del
list_1 = [10, 20, 30]
list_1.clear()
list_1 = []
del list_1[:]

print(list_1)

# reverse list
list_1 = [10, 20, 30]
list_1.reverse()
print(list_1)

# duplicate list
# you can duplicate a list with copy() or with slice
list_1 = [10, 70, 20]
list_2 = list_1.copy()
print(list_1)
print(list_2)

list_1 = [10, 70, 20]
list_2 = list_1[:]
print(list_1)
print(list_2)

# sorting
list_1 = [10, 70, 20]
list_1.sort()
print(list_1)

list_2 = ['z', 'h', 'c']
list_2.sort()
print(list_2)