# Write a function that prints the digits of a number. 
# Q3: digits of a number. E.g., n=312 there are 3 digits in 312 and we need to print them.

# HINT -The right most digit of a number N is N%10. and to remove the right most digit from a 
# number,we can do N=N/10.
    
def print_digits(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = n // 10
    digits.reverse()  # Reverse the list to get the correct order of digits
    print("Digits of the number are:", digits)

number = int(input("Enter a number: "))
print_digits(number)