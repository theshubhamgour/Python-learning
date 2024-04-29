# Types of operators
'''
Arithmetic Operators ( + , - , * , / , % , ** )

Relational / Comparison Operators ( == , != , > , < , >= , <= )

Assignment Operators ( = , +=, -= , *= , /= , %= , **= )

Logical Operators ( not , and , or )

'''

# ----------------------------------------------------------#
#Arithmetic Operators
a = 5 
b = 2

print("Output for Arithmetic Operators : ")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b)


# ----------------------------------------------------------#
#Relational Operators
x = 4
y = 5

print("Output for Relational Operators : ")
print(x == y) #false
print(x != y) #true
print(x >= y) #false
print(x <= y) #true
print(x > y) #false
print(x < y) #true

# ----------------------------------------------------------#
# Assignment Operators

num = 10
num = num + 10  # num += 10
print("num : ",num)

numb = 10
numb = numb - 10  # numb -= 10
print("num : ",numb)

nums = 10
nums = nums * 10  # nums *= 10
print("num : ",nums)

numd = 10
numd = numd / 10  # numd /= 10
print("num : ",numd)

numf = 10
numf **=5 #to the power 5
print("num : ",numf)

# ----------------------------------------------------------#
# Logical Operators
n = 5
y = 8
print(not False)
print(not True)

print(not (n < y))

val1 = False
val2 = True
print("AND operator:",val1 and val2)

print("OR operator:",(n > y) or (n < y))