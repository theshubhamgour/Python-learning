# Write a program to calculate the factorial of a number.

def calculate_factorial(n):
    fact =1
    for i in range(1, n + 1):
        fact *= i
    return fact

number = int(input("Enter a number to calculate its factorial: "))
factorial_result = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial_result}")