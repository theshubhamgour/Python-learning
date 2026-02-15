# Range function generates a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# Syntax: range(start, stop, step)

# Example 1: Using range() to generate a sequence of numbers
for i in range(5):
    print(i)

# Example 2: Using range() with a start and stop value
for i in range(1, 6):
    print(i)

# Example 2: Using range() with a start and stop value
for i in range(1, 10, 2):
    print(i)

# print sum of n numbers using range function

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of numbers from 1 to", n, "is:", total)