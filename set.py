data_1 = {1, "acbd", 3.14, False, (2, 8)}

print("data", data_1)

# access element in set
fellowship = {'laragon', 'gemini', 'cihuy'}
for p in fellowship:
    print(p)

# eliminate duplicate element
data = {1, 2, 3, 1, 2, 4, 3, 4, 5, 6}
print(data)

data = [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
print(data)

data_unique_set = set(data)
print(data_unique_set)

data_unique = list(data_unique_set)
print(data_unique)

# check if element is exist
fellowship = {'aragorn', 'gimli', 'legolas'}
to_find = "gimli"

if to_find in fellowship:
    print(to_find, "is exist")

# set operation
# add new data
fellowship = set()

fellowship.add('laragon')
print("len:", len(fellowship), "data", fellowship)

fellowship.add('xampp')
print("len:", len(fellowship), "data", fellowship)

fellowship.add('mysql')
print("len:", len(fellowship), "data", fellowship)

# delete data
fellowship = {'narya', 'nenya', 'nilya'}

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

# delete specific data
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print("fellowship", fellowship)

fellowship.discard("boromir")
print("fellowship", fellowship)

fellowship.remove("gandalf")
print("fellowship", fellowship)

# clear set
fellowship = {'aragorn', 'gimli', 'legolas'}
fellowship.clear()

print("len:", len(fellowship), "data:", fellowship)

# copy set
data1 = {'aragorn', 'gimli', 'legolas'}
print("len:", len(data1), "data1:", data1)

data2 = data_1.copy()
print(data2)

# difference between set
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

diff = fellowship.difference(hobbits)
print(diff)

fellowship.difference_update(hobbits)
print("fellowship", fellowship)