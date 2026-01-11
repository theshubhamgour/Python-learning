# Write a program to swap values of two numbers entered by the user.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num3 = num1
num1 = num2
num2 = num3

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)