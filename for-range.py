for i in range (5):
    print("index", i)

r = range(5)
print("r:", list(r))

print("for range step")
for i in range(2, 10, 2):
    print("index: ", i)

print("negative for range step")
for i in range(5, -5, -1):
    print("index: ", i)

print("data list")
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

print("data tuple")
numbers = ("twenty four", 24)
for n in numbers:
    print(n)

for char in "hello python":
    print(char)

bio = {
    "name": "toyota camry",
    "year": 1993,
}

for key in bio:
    print("key:", key, "value:", bio[key])

numbers = {"twenty four", 24}
for n in numbers:
    print(n)