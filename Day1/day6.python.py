# -------------------------------------------
# DAY 6 — MODULES & PACKAGES
# -------------------------------------------

# USING A BUILT-IN MODULE

import math

print(math.sqrt(16))
print(math.pi)


# OUTPUT :
# 4.0
# 3.141592653589793


# EXPLANATION :
# - A module is a file that contains Python code
# - Python has built-in modules like math
# - import allows us to use them



# -------------------------------------------

# IMPORTING SPECIFIC FUNCTIONS

from math import pow

print(pow(2, 3))


# OUTPUT :
# 8.0


# EXPLANATION :
# - We can import specific functions
# - This avoids writing the module name every time



# -------------------------------------------

# USING ALIASES

import random as rnd

print(rnd.randint(1, 10))


# OUTPUT :
# (Random number between 1 and 10)


# EXPLANATION :
# - Aliases shorten module names
# - Useful for long module names



# -------------------------------------------

# CREATING YOUR OWN MODULE (EXAMPLE)

# file name: my_module.py
# def greet(name):
#     print("Hello", name)

# In another file:
# import my_module
# my_module.greet("William")


# EXPLANATION :
# - You can create your own modules
# - Save reusable functions in separate files



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ modules
# ✔ import
# ✔ from ... import
# ✔ aliases
# ✔ built-in libraries

# -------------------------------------------

# FINAL DAY 6 PRACTICE 🧠

import datetime

current_year = datetime.datetime.now().year

print("Current year:", current_year)
print("I am growing as a Python developer")
