# Tuples in Python - A built-in data type that lets us create immutable sequences of values.

tup = (2,3,1,2)
print(type(tup))

print(tup[0])
print(tup[1:3])

# Tuple Methods
print(tup.index( 3 )) #returns index of first occurrence
print(tup.count( 2 )) #counts total occurrences