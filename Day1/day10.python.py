# -------------------------------------------
# DAY 10 — MINI PROJECTS (PUTTING IT ALL TOGETHER)
# -------------------------------------------

# MINI PROJECT 1 — SIMPLE CALCULATOR
# Uses: variables, input, functions, conditionals

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"


print(calculator(10, 5, "add"))
print(calculator(10, 5, "multiply"))


# OUTPUT :
# 15
# 50



# -------------------------------------------

# MINI PROJECT 2 — STUDENT PROFILE
# Uses: dictionaries, functions, print formatting

def student_profile(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    return student


profile = student_profile("William", 22, "Python")

print("Name:", profile["name"])
print("Age:", profile["age"])
print("Course:", profile["course"])


# -------------------------------------------

# MINI PROJECT 3 — EVEN & ODD CHECKER
# Uses: loops, conditionals

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


# -------------------------------------------

# MINI PROJECT 4 — FILE LOGGER
# Uses: file handling

file = open("progress.txt", "w")
file.write("Python Learning Progress\n")
file.write("Completed Day 1 to Day 10\n")
file.write("Next goal: Build real projects")
file.close()

file = open("progress.txt", "r")
print(file.read())
file.close()


# -------------------------------------------

# MINI PROJECT 5 — OOP PRACTICE
# Uses: classes, objects, methods

class Learner:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def introduce(self):
        print("My name is", self.name)
        print("I am learning", self.skill)


learner = Learner("William", "Python")
learner.introduce()


# -------------------------------------------

# WHAT I LEARNED IN 10 DAYS ✅
# ✔ Python basics
# ✔ data types
# ✔ control flow
# ✔ functions
# ✔ collections
# ✔ modules
# ✔ file handling
# ✔ error handling
# ✔ OOP
# ✔ building mini projects

# -------------------------------------------

# FINAL MESSAGE 🚀

print("Congratulations!")
print("You have completed Python Basics in 10 Days 🎉")
print("Next step: Practice, build projects, and stay consistent 💻🔥")
