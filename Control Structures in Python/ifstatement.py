'''
Author: Shubham Gour

'''

# Determine a person is adult or not by accepting value from user

age= input("Enter your age: ")
age= int(age)
# This can also be done in one line 
# age = int(input("Enter your age: "))

if age>= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# The syntax of if else is:  (if condition: print else: print)