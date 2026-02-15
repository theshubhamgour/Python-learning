# Write a function that takes two integers and prints all even numbers between them (inclusive).
def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

# Example usage:
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
print_even_numbers(start_num, end_num)