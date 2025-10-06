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

# convert range to list