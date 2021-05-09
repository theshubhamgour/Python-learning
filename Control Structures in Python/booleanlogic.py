'''
Author: Shubham Gour

'''

# boolean logic is used when you have to check certain conditions
# we are going to make a simple user login system

# first of all we will create two variables named username and password and assign the values in them
username = "Admin"
password = "root"

# so to comfirm the accurate password we will make use of and boolean logic "and" which throws true when both the conditions are true
if username =="Admin" and password == "root":
    print("Login Successful")
else:
    print("Login Failed")
# you will se the output as login Successful since th values are true


# now to take input from the user you may follow the below code
email= input("Enter you email: ")
passd= input("Enter password: ")

if email== "iamthe@gmail.com" and passd== "seoul":
    print("Login Successfull")
else:
    print("Unauthorized access")


# what if you want to check either of one conditions then we will make use of second boolean logic viz "or"
location= input("Your City: ")
region= input("Your region: ")

if location=="Nagpur" or region=="Pune":
    print("You're in")
else:
    print("Sorry better luck next time")


