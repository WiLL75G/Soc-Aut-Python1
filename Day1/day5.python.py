# -------------------------------------------
# DAY 5 — COLLECTIONS (LISTS, TUPLES, DICTIONARIES, SETS)
# -------------------------------------------

# LISTS (ORDERED & CHANGEABLE)

fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
print(fruits[1])


# OUTPUT :
# ['apple', 'banana', 'mango']
# apple
# banana


# EXPLANATION :
# - Lists store multiple items
# - Indexing starts from 0
# - Lists can be modified



# -------------------------------------------

# MODIFYING A LIST

fruits.append("orange")
fruits.remove("banana")

print(fruits)


# OUTPUT :
# ['apple', 'mango', 'orange']


# -------------------------------------------

# TUPLES (ORDERED & NOT CHANGEABLE)

colors = ("red", "green", "blue")

print(colors)
print(colors[2])


# OUTPUT :
# ('red', 'green', 'blue')
# blue


# EXPLANATION :
# - Tuples are like lists
# - But they cannot be changed after creation



# -------------------------------------------

# DICTIONARIES (KEY : VALUE PAIRS)

student = {
    "name": "William",
    "age": 22,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["course"])


# OUTPUT :
# {'name': 'William', 'age': 22, 'course': 'Python'}
# William
# Python


# EXPLANATION :
# - Dictionaries store data as key-value pairs
# - Keys are used to access values



# -------------------------------------------

# SETS (UNORDERED & UNIQUE ITEMS)

numbers = {1, 2, 3, 3, 4}

print(numbers)


# OUTPUT :
# {1, 2, 3, 4}


# EXPLANATION :
# - Sets remove duplicate values
# - Order is not guaranteed



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ lists
# ✔ tuples
# ✔ dictionaries
# ✔ sets
# ✔ indexing
# ✔ key-value pairs

# -------------------------------------------

# FINAL DAY 5 PRACTICE 🧠

languages = ["Python", "JavaScript", "Java"]

profile = {
    "name": "William",
    "skills": languages,
    "learning": True
}

print("Name:", profile["name"])
print("Skills:", profile["skills"])
print("Learning Python:", profile["learning"])
