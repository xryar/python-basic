# string
string_1 = "acumalaka"

# multiple line string
string_2 = """acumalaka
cihuy
yyyy"""

# bool
bool_1 = True
bool_2 = False

# none
data = "hello"
print(data)
data = None
print(data)

# list
list_1 = [1, 2, 3, 4, 5]
print(list_1[2])
list_2 = ["grayson", "bruce", "ucogs", "acumalaka"]
print(list_2[1])
list_3 = [1, 2, "grayson", "acumalaka", False]
print(list_3[4])

# tuple. like list but in const
tuple_1 = (2, 3, 4)
print(tuple_1[2])
tuple_2 = ("numero", "uno")
print(tuple_2[1])
tuple_3 = (24, False, "acumalaka")
print(tuple_3[0])

# dictionary. same with map i think
profile_1 = {
    "name": "Arya",
    "is_male": False,
    "age": 16,
    "hobbies": ["gaming", "learning"]
}
print("name: %s" % (profile_1["name"]))
print("hobbies: %s" % (profile_1["hobbies"]))

# set
set_1 = {"pineapple", "spaghetti"}
print(set_1)