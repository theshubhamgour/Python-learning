# Take the radius (r) as user input and print the area.
# Use the formula: Area = π * r^2 (value of π = 3.14)

radius_input = input("Enter the radius: ")
radius = float(radius_input)
pi = 3.14
area = pi * (radius ** 2)
print("The area of the circle with radius", radius, "is:", area)