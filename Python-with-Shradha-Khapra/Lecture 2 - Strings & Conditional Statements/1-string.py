# String is data type that stores a sequence of characters.
str1 = "This is a string"
str2 = 'This is another string'
str3 = """"This is another way of string"""

# Here we made use of "" and ' to seperate the characters
print("This is a string's with a 's'")

# Escape sequence characters used for formatting
strr = "This is line one \n This is next line"
print(strr)

# Concatenation
str1 = "This is a string"
str2 = "This is another string"
final_str = str1 + str2
print(final_str)

# Length Function to find length of string
str1 = "This is a string"
print(len(str1))

# Indexing - Index is a position of the characters NOTE: we can access not modify via indexing
str = "Apna_College"
# str[0] is ‘A’, str[1] is ‘p’ ...
print(str[2])

# Slicing - Accessing parts of a string
str = "Unka_College"
# str[ starting_idx : ending_idx ] : ending idx is not included
print(str[1:5]) # This will print : nka_