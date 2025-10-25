# lists_loops.py
# Question 3: Lists and Loops

# Create a list of 9 student names
students = ["Monicah", "Irwine", "Benedict", "Gloria", "Faith", "Teddy", "Sandra", "Drina", "Ryan"]

# Use a for loop to print each name in uppercase with its index number
for index, name in enumerate(students, start=1):
    print(f"{index}. {name.upper()}")
