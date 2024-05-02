# Set in Python - Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

nums = { 1, 2,2,2,2, 3, 4 }

print(nums) #set don't print duplicate values
print(type(nums))


set2 = { 1, 2, 2, 2 }
#repeated elements stored only once, so it resolved to {1, 2}



collection = set( ) #empty set syntax
# Set Methods
collection.add( 1 ) #adds an element
collection.add( 2 )
collection.add( 3 )
collection.add( "Barry" )
print(collection)

collection.remove( 2 ) #removes the elem an
print(collection)

collection.pop( ) #removes a random value
print(collection)

collection.clear( ) #empties the set
print(collection)


set1 = {1,2,5,7,8,9,90}
set2 = {1,4,5,7,8,9,999,99,90}
print(set1.union(set2)) #combines both set values & returns new
print(set1.intersection(set2))#combines common values & returns new
