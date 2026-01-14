# -------------------------------------------
# DAY 3 — CONTROL FLOW (IF, FOR, WHILE)
# -------------------------------------------

# IF STATEMENT (CONDITIONALS)

age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# OUTPUT :
# You are an adult


# EXPLANATION :
# - if checks a condition
# - else runs if the condition is False
# - conditions use comparison operators like >=, <=, ==, !=



# -------------------------------------------

# ELIF (ELSE IF)

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")


# OUTPUT :
# Grade B


# EXPLANATION :
# - elif checks another condition if the first is False
# - Useful for multiple choices



# -------------------------------------------

# FOR LOOP (ITERATING OVER ITEMS)

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# OUTPUT :
# apple
# banana
# mango


# EXPLANATION :
# - for loops go through items in a list or sequence
# - Each item is stored in a variable (fruit) inside the loop



# -------------------------------------------

# WHILE LOOP (REPEATING UNTIL CONDITION IS FALSE)

count = 1

while count <= 5:
    print("Count is", count)
    count += 1  # increases count by 1


# OUTPUT :
# Count is 1
# Count is 2
# Count is 3
# Count is 4
# Count is 5


# EXPLANATION :
# - while repeats code while the condition is True
# - Be careful to update the variable to avoid infinite loops



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ if, elif, else
# ✔ comparison operators
# ✔ for loops
# ✔ while loops
# ✔ iteration over lists

# -------------------------------------------

# FINAL DAY 3 PRACTICE 🧠

numbers = [2, 5, 8, 10]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

# Using while loop
i = 1
while i <= 3:
    print("Hello Python", i)
    i += 1
