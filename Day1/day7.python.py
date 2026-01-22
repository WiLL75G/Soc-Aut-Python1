# -------------------------------------------
# DAY 7 — FILE HANDLING (READ, WRITE, APPEND)
# -------------------------------------------

# WRITING TO A FILE

file = open("example.txt", "w")
file.write("Hello, Python!\n")
file.write("This is Day 7 practice.")
file.close()


# OUTPUT :
# (Creates a file named example.txt with the text inside)


# EXPLANATION :
# - "w" mode opens a file for writing
# - If file doesn’t exist, it will be created
# - Always close the file after writing



# -------------------------------------------

# READING FROM A FILE

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()


# OUTPUT :
# Hello, Python!
# This is Day 7 practice.


# EXPLANATION :
# - "r" mode opens a file for reading
# - read() gets all content from the file



# -------------------------------------------

# READING LINE BY LINE

file = open("example.txt", "r")
for line in file:
    print(line)
file.close()


# OUTPUT :
# Hello, Python!
# This is Day 7 practice.


# EXPLANATION :
# - We can loop through each line in a file
# - Useful for large files



# -------------------------------------------

# APPENDING TO A FILE

file = open("example.txt", "a")
file.write("\nI am learning Python from zero.")
file.close()

# Reading to check
file = open("example.txt", "r")
print(file.read())
file.close()


# OUTPUT :
# Hello, Python!
# This is Day 7 practice.
# I am learning Python from zero.


# EXPLANATION :
# - "a" mode adds content to the end of the file
# - It doesn’t erase existing content



# -------------------------------------------

# WHAT I LEARNED TODAY ✅
# ✔ open() function
# ✔ read mode "r"
# ✔ write mode "w"
# ✔ append mode "a"
# ✔ reading files line by line
# ✔ closing files

# -------------------------------------------

# FINAL DAY 7 PRACTICE 🧠

# Create and write
file = open("my_info.txt", "w")
file.write("Name: William\n")
file.write("Age: 22\n")
file.write("Learning: Python")
file.close()

# Read file
file = open("my_info.txt", "r")
print(file.read())
file.close()
