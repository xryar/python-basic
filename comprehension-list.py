# example
seq = []
for i in range(5):
    seq.append(i * 2)

print(seq)

# comprehension
seq = [i * 2 for i in range(5)]
print(seq)

# example
seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)

print(seq)

# comprehension
seq = [i for i in range(10) if i % 2 == 1]
print(seq)

# example
seq = []
for i in range(1, 10):
    if i % 2 == 0:
        seq.append(i * 2)
    else:
        seq.append(i * 3)

print(seq)

# tenary comprehension
seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))

print(seq)

# comprehension
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]

print(seq)

# example
list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

seq = []
for x in list_x:
    for y in list_y:
        seq.append(x + y)

print(seq)

# comprehension
seq = [x + y for x in list_x for y in list_y]
print(seq)

# example
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    tr = []
    for row in matrix:
        tr.append(row[i])
    transposed.append(tr)

print(transposed)

# comprehension 1
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# comprehension 2
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)