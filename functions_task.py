# functions_task.py
# Question 4: Functions - Area of a Circle

# Import pi from the math library
from math import pi

# Define the function
def area_of_circle(radius):
    """Return the area of a circle given its radius."""
    if radius <= 0:
        return "Invalid radius. Radius must be greater than 0."
    area = pi * (radius ** 2)
    return round(area, 2)

# Test the function
user_input = float(input("Enter the radius of the circle: "))
result = area_of_circle(user_input)
print(f"The area of the circle is: {result}")
