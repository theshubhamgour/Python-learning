'''
Author: Shubham Gour

'''

fruits= ["Apple", "Mango", "Orange", "Pineapple"]

# First function- Append function to add
fruits.append("Banana")
print(fruits)
# And this will add Banana in the list fruits

# Calculate length of list
# Second function- Len function
print(len(fruits))

# Third function- Insert function
# somehow same as append function but here we have the freedom to place the element wheer ever we want in the list
fruits.insert(1, "Guava")
print(fruits)
# this will add guava in the first position in place of Mango
# syntax of insert function: listname.insert(position,"name of element")

# Fourth function- Index function
# tells the index number of the element
print(fruits.index("Orange"))
# useful when the list have many element in it

