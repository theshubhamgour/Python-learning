# Lambda functions in Python are small anonymous functions that can have any number of arguments but can only have one expression.
# They are defined using the lambda keyword and are often used for short, simple functions that are not reused elsewhere in the code.
# Syntax: lambda arguments: expression

# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print("The sum is:", result)
