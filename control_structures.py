# control_structures.py
# Question 2: Control Structures

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check the number
if number < 0:
    print("Invalid input – negative numbers not allowed.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
