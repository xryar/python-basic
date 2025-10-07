tuple_1 = (1, 2, "hello", True)

print("elem 0", tuple_1[0])
print("elem 1", tuple_1[1])

# loop tuple
tuple_2 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')
for t in tuple_2:
    print(t)

for i in range(0, len(tuple_2)):
    print("index", i, "elem", tuple_2[i])

# enumerate
for i, v in enumerate(tuple_2):
    print("index", i, "elem", v)

# check if tuple element if exist
tuple_1 = (10, 70, 20)
n = 70

if n in tuple_1:
    print(n, "is exist")
else:
    print(n, "is not exist")

# nested tuple
tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))

# vertikal
# tuple_nested = (
#     (0, 2),
#     (0, 3),
#     (2, 2),
#     (2, 4)
# )

for row in tuple_nested:
    for cel in row:
        print(cel, end=" ")
    print()

# combine list and tuple
data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

# append tuple to list
data.append(("noob saibot", 6, False, ['brotherhood of shadow']))

data.append(("tifa lockhart", 2, True, ['avalanche']))

# print data
print("name | rank | win | affliation")
print("------------------------------")
for row in data:
    for cel in row:
        print(cel, end=" | ")
    print()

# tuple conversion
# string to tuple
alphabets = tuple("abcdefgh")
print(alphabets)

# list to tuple
numbers = tuple([1, 2, 3, 4])
print(numbers)

# range to tuple
r = range(0, 3)
rtuple = tuple(r)
print(rtuple)

# packing and unpacking tuple
# tuple packing
first_name = "aerith gainsborough"
rank = 11
win = False

# you can write tuple with () or not
row_data = (first_name, rank, win)
#row_data = first_name, rank, win

print(row_data)

# tuple unpacking
row_data = ('aerith gainsborough', 11, False)
first_name, rank, win = row_data

print(first_name, rank, win)