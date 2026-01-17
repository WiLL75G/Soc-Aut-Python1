# -------------------------------------------
# DAY 4 — FUNCTIONS (REUSABLE CODE)
# -------------------------------------------

# BASIC FUNCTION

def greet():
    print("Hello, welcome to Python")


greet()


# OUTPUT :
# Hello, welcome to Python


# EXPLANATION :
# - def is used to define a function
# - Functions help us reuse code
# - greet() calls the function



# -------------------------------------------

# FUNCTION WITH PARAMETERS

def greet_user(name):
    print("Hello", name)


greet_user("William")
greet_user("Python Learner")


# OUTPUT :
# Hello William
# Hello Python Learner


# EXPLANATION :
# - Parameters are values passed into a function
# - name is a parameter
# - We can pass different values when calling the function



# -------------------------------------------

# FUNCTION WITH MULTIPLE PARAMETERS

def add_numbers(a, b):
    print(a + b)


add_numbers(5, 3)
add_numbers(10, 20)


# OUTPUT :
# 8
# 30


# -------------------------------------------

# RETURN VALUES

def multiply(a, b):
    return a * b


result = multiply(4, 5)
print(result)


# OUTPUT :
# 20


# EXPLANATION :
# - return sends a value back from a function
# - Returned values can be stored in variables



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ functions
# ✔ def keyword
# ✔ parameters
# ✔ arguments
# ✔ return values

# -------------------------------------------

# FINAL DAY 4 PRACTICE 🧠

def calculate_age(current_year, birth_year):
    return current_year - birth_year


age = calculate_age(2024, 2002)

print("I am", age, "years old")
print("I am mastering Python step by step")
