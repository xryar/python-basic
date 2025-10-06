# arithmetic

# +
num_plus = 2 + 2
num_plus_unary = +2

# -
num_min = 2 - 2
num_min_unary = -2

# *
num_multiple = 2 * 2

# /
num_divide = 8 / 2
num_double_divide = 10 // 3

# %
num_mod = 10 % 3

# **
num_power = 3 ** 2

# compare
sm = 4 == 5
ns = 4 != 5
gt = 4 > 5
lt = 4 < 5
gte = 4 >= 5
lte = 4 <= 5

# logics
dan = (4 == 5) and (2 != 3)
atau = (4 == 5) or (2 != 3)
tidak = not (4 == 5)

# bitwise
# x & y = 0
# x | y = 14
# ~x = -11
# x ^ y = 14
# x >> 2 = 2
# x << 2 = 40

# identity is
num_1 = 100001
num_2 = 100001
res = num_1 is num_2
print("num_1 is num_2 = ", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))

# print with string formatter
print("message: %s %s %s" % ("hello", "python", "learner"))
# print without string formatter
print("message:", "hello", "python", "learner")

# id
data_1 = "hello world"
id_data_1 = id(data_1)
print(data_1)
print(id_data_1)

# in
sample_list = [2, 3, 4]
is_3_exist = 3 in sample_list
print(is_3_exist)

sample_tuple = ("hello", "python")
is_hello_exist = "hello" in sample_tuple
print(is_hello_exist)

sample_dict = {"nama": "noval", "age": 21}
is_age_exist = "age" in sample_dict
print(is_age_exist)

sample_set = {"sesuk", "age"}
is_sesuk_exist = "sesuk" in sample_dict
print(is_sesuk_exist)

text = 'Hello world'
is_substring_exists = 'orl' in text
print(is_substring_exists)