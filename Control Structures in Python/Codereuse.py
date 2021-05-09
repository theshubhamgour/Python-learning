'''
Author: Shubham Gour

'''

# Reuse the code again and again
# if you have written a code and you have to refer it number of times then you can make use of coderesue function
# for now let's say you have this file which you want to refer number of times then here is how you cna make use of code reue function

# print("My name is Shubham Gour")
# print("Nagpur")
# print("I Love Virtual realtiy games")


# print("My name is Shubham Gour")
# print("Nagpur")
# print("I Love Virtual realtiy games")


# print("My name is Shubham Gour")
# print("Nagpur")
# print("I Love Virtual realtiy games")

# in the above code if want to change the first statement in each time then you manually have to do it, so in order to get rid of it
# we here use a function and for which we will define one function

def function1():
    print("My name is Shubham Gour")
    print("Nagpur")
    print("I Love Virtual realtiy games")

# now for printing this function viz function1 we will write the below code
# this will call the def function1 and print on the screen
# remember the () brackets indicates that it passes arguments
function1()

# now suppose you want to print this same line of code again and again then you simply have to call the function1
# suppose i want to cal it three times then,

function1()
function1()
function1()


# so whenever i want to make changes in the code then i will just update the defination and thus the entire code will be updated