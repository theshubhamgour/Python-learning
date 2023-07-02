# Write a  program which performs the addition of two numbers entered by the user
# Let's say the user enters 39 then the addition should be as follows 3 + 9 = 12

print("----- Exercise ----- \n")
variable = input("Enter any two-digit number: ")
vsplit1 = int(variable[0])
vsplit2 = int(variable[1])

# The number is split into the below
print("The first number is: " + str(vsplit1))
print("The second number is: " + str(vsplit2))

result = vsplit1 + vsplit2
print("The addition is: " + str(result))

