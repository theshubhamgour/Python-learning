# Write a Python program to find the maximum element in an array.

# Try : 
# elements = [1,2,3,4,5,5,6,6,6,6,5,4,3,2,2,4,323,2321,2]
# print("Total elements in the array is : ",len(elements))

# Your code snippet counts the total number of elements in the array, which is not the same as finding the maximum element.


# Actual
elements = [1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 5, 4, 3, 2, 2, 4, 323, 2321, 2]
max_element = elements[0]  # Initialize max_element with the first element of the array

for element in elements:
    if element > max_element:
        max_element = element

print("Maximum element in the array:", max_element)