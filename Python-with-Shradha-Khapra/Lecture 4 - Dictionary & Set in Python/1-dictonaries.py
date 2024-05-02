# Dictionary in Python - Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don’t allow duplicate keys

dict = {
    "name" : "Shubham",
    "cgpa" : 9.8,
    "marks" : [98,97,96],
    "isadult" : True,
    "subjects": {
        "phy" : 98,
        "maths" : 100,
        "chem" : 99
    }
}
# To print from dictionary
print(dict["name"])
print(dict)
print(type(dict))
print(dict["subjects"]["phy"])

# Overriding a existing key and adding new key
# dict["name"] = "Siddharth"
# dict["Surname"] = "Malhotra"
# print(dict["name"])
# print(dict)


# Dictionary Methods
print(dict.keys( )) #returns all keys
print(dict.items( )) #returns all (key, val) pairs as tuples
print(dict.values( )) #returns all values
print(dict.get( "name" )) #returns the key according to value
print(dict.get( "name2" )) #returns the none if key not found
dict.update({"city" : "Nagpur"}) #updates values in dictonaries
print(dict)




