
# Slicing - Accessing parts of a string
str = "Unka_College"
# str[ starting_idx : ending_idx ] : ending idx is not included
print(str[1:5]) # This will print : nka_

# Slicing - 
str = "Apple"
print(str[ -3 : -1 ]) # is “pl”

#String Function
str = "I am a coder."

print(str.endsWith("er.")) #returns true if string ends with substr
print(str.capitalize( ))#capitalizes 1st char
print(str.replace( "am", "ma" )) #replaces all occurrences of old with new
print(str.find( "coder" )) #returns 1st index of 1st occurrence
print(str.count("am")) #counts the occurrence of substr in string

