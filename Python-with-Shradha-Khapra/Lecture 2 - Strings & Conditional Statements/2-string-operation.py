
# Slicing - Accessing parts of a string
str = "Unka_College"
# str[ starting_idx : ending_idx ] : ending idx is not included
print(str[1:5]) # This will print : nka_



# ----------------------------------------------------------#
# Slicing - Using negative index
str = "Apple"
print(str[ -3 : -1 ]) # is “pl”



# ----------------------------------------------------------#
#String Function
str = "i am a coder."



# ----------------------------------------------------------#
# Check if string ends with "er."
print(str.endswith("er."))



# ----------------------------------------------------------#
# Capitalize the first character of the string
print(str.capitalize())



# ----------------------------------------------------------#
# Replace all occurrences of "am" with "ma"
print(str.replace("am", "ma"))



# ----------------------------------------------------------#
# Find the index of the first occurrence of "coder"
print(str.find("coder"))



# ----------------------------------------------------------#
# Count the occurrences of "am" in the string
print(str.count("am"))


