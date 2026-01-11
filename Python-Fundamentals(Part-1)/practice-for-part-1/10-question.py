# Take a decimal number as input (like 45.78 ) and output its:
# • integer part - 45
# • fractional part - .78

decimal_input = input("Enter a decimal number: ")
decimal_number = float(decimal_input)
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part
print("Integer part:", integer_part)
print("Fractional part:", fractional_part)