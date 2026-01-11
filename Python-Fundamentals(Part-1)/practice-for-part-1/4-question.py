# The user enters a string containing a number (e.g., "45" ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.

user_input = 45
int_value = int(user_input)
float_value = float(user_input)
str_value = str(user_input)     

print("Integer value:", int_value, "Type:", type(int_value))
print("Float value:", float_value, "Type:", type(float_value))
print("String value:", str_value, "Type:", type(str_value))