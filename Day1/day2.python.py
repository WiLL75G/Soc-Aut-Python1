# -------------------------------------------
# DAY 2 — DATA TYPES (STRINGS, NUMBERS, BOOLEANS)
# -------------------------------------------

# STRINGS (TEXT DATA)

name = "William"
message = "Python is fun"

print(name)
print(message)


# OUTPUT :
# William
# Python is fun


# EXPLANATION :
# - Strings are text data
# - Strings must be inside quotes " " or ' '



# -------------------------------------------

# NUMBERS (INTEGERS & FLOATS)

age = 22        # integer
height = 1.75  # float (decimal number)

print(age)
print(height)


# OUTPUT :
# 22
# 1.75


# EXPLANATION :
# - Integers are whole numbers
# - Floats are numbers with decimals



# -------------------------------------------

# BOOLEANS (TRUE OR FALSE)

is_student = True
has_graduated = False

print(is_student)
print(has_graduated)


# OUTPUT :
# True
# False


# EXPLANATION :
# - Booleans store True or False values
# - They are used in decision-making



# -------------------------------------------

# TYPE CHECKING

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# OUTPUT :
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>


# -------------------------------------------

# TYPE CONVERSION

age_as_string = str(age)
height_as_int = int(height)

print(age_as_string)
print(height_as_int)


# OUTPUT :
# 22
# 1


# EXPLANATION :
# - str() converts to string
# - int() converts to integer
# - float() converts to decimal number



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ strings
# ✔ integers
# ✔ floats
# ✔ booleans
# ✔ type()
# ✔ type conversion

# -------------------------------------------

# FINAL DAY 2 PRACTICE 🧠

name = "William"
age = "22"

age_number = int(age)

print("My name is", name)
print("Next year I will be", age_number + 1)
print("Learning Python is awesome!")
