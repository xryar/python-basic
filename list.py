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