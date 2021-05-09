'''
Author: Shubham Gour

'''

# To create a calcuator which calcuates the Simple intrest
# Task  1 : Take user input for Principle value, Numer of years and Rate of intrest
# Task  2 : Convert sting value to integer value (Here p,n,r)
# Task  3 : Calculate using formua (p*n*r)/100, Store to SI and print the result

# Taking user input
p = input("Enter the Principle value: ")
n = input("Enter Number of Years: ")
r = input("Enter the Rate of intrest: ")

# Converting to integer
p=int(p)
n=int(n)
r=int(r)

# Calculating using given formula
SI=(p*n*r)/100
print(SI)

# You can test the answer by using the value p=1000,n=1 and r=10 and your answer should resemble 100.0