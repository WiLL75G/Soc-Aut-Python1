# -------------------------------------------
# DAY 8 — ERROR HANDLING (TRY, EXCEPT, FINALLY)
# -------------------------------------------

# BASIC ERROR EXAMPLE

print(10 / 2)
# print(10 / 0)  # This would cause an error


# EXPLANATION :
# - Some code can cause errors
# - Errors can stop the program if not handled



# -------------------------------------------

# USING TRY & EXCEPT

try:
    result = 10 / 0
    print(result)
except:
    print("Something went wrong!")


# OUTPUT :
# Something went wrong!


# EXPLANATION :
# - try tests code that may cause an error
# - except runs when an error occurs
# - Program does not crash



# -------------------------------------------

# HANDLING SPECIFIC ERRORS

try:
    number = int("abc")
    print(number)
except ValueError:
    print("Cannot convert text to a number")


# OUTPUT :
# Cannot convert text to a number


# EXPLANATION :
# - ValueError happens when conversion fails
# - You can catch specific errors



# -------------------------------------------

# USING FINALLY

try:
    x = 5 / 1
    print(x)
except:
    print("Error occurred")
finally:
    print("This always runs")


# OUTPUT :
# 5.0
# This always runs


# EXPLANATION :
# - finally runs whether there is an error or not
# - Used for cleanup tasks



# -------------------------------------------

# RAISING YOUR OWN ERROR

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")


# EXPLANATION :
# - raise is used to create custom errors
# - Helps enforce rules in your program



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ errors
# ✔ try & except
# ✔ handling specific errors
# ✔ finally
# ✔ raise keyword

# -------------------------------------------

# FINAL DAY 8 PRACTICE 🧠

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("Result:", num1 / num2)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")
finally:
    print("Day 8 practice completed")
