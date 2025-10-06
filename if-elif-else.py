grade = 100

if grade == 100:
    print("perfect")

if grade == 90:
    print("ok")
    print("keep working hard!")

str_input = input("Enter your grade: ")
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed exam")
else:
    print("you not passed the exam")

# with logic operation
grade = int(input("Enter your current grade: "))
prev_grade = int(input("Enter your previous grade: "))

if grade >= 90 and prev_grade >= 65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome. you definitely working hard, right ?")
elif grade >= 65:
    print("passed exam")
else:
    print("below passing grade")

if (grade >= 65 and not prev_grade >= 65) or (not grade >= 65 and prev_grade >= 65):
    print("at least you passed one exam. good job!")