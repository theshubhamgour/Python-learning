'''
Author: Shubham Gour

'''

# when we want to change the value of a variable time to time we make use of inplace operator
# like we can understand it with the example of age
age=21
print(age)

# now we will increment the age by 1
age+=1
print(age)

# now we will increment the age by 10
age+=10
print(age)

# Likewise you can substract age in the same way
age-=5
print(age)
# here age got substracted with the value 37 since it got updated

# We can also multiply the age using the same operator
age*=5
print(age)
# Here 27 (the updated value) will get multiplied by 5

# You can also add a string to the another string using inplace operator
b="Hello"
b+="World"
print(b)