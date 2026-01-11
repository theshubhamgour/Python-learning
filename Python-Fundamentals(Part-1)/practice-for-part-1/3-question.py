# Ask the user to enter two integers and one float. Convert them all to floats and print their average.

num1 = float(input("Enter the first integer: "))
num2 = float(input("Enter the second integer: "))
num3 = float(input("Enter a float: "))

average = (num1 + num2 + num3) / 3
print("The average is:", average)