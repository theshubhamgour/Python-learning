'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.
'''
# user_input = {}

# x = int(input("Enter Physics : "))
# user_input.update({"phy": x})

# y = int(input("Enter Maths : "))
# user_input.update({"maths": y})

# z = int(input("Enter Chem : "))
# user_input.update({"chem": z})

# print(user_input)


'''
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
'''
# Method 1 : make another string
values = {9 , '9.0'}
print(values)

#Method 2 : Create a tuple pairs
values2 = {
    ("float" , 9.0),
    ("int" , 9)
}
print(values2)