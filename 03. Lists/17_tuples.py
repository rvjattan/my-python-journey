# one of the built in data structures of python.
# tuples are more memory efficient than lists.
# tuples have slightly higher time efficiency than lists.

# we can't modify a tuple after creating one, so they should be used with data that won't need to be changed.
# tuples can hold objects of different data types

my_tuple = ('abc', 123, 'def', 456)

# tuples can also hold one item as long as that item is followed by a comma:
my_tuple = ('abc',)

# items in a tuple can be accessed with their index
my_tuple_new = ('abc', 123, 'def', 456)
print(my_tuple_new[0]) # prints abc

# slicing can be applied:
print(my_tuple[3:5]) # prints 456, 789

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# tuples have limited built in methods:
# .len(): >>>>>>>>>>>>>>>>
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(my_tuple)) # prints 6

# >>>>>>>>>.max(): if used with numerical values, it returns the maxium value >>>>>>>>>>>>>>>>>>
my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
 
my_tuple = ('orange', 'blue', 'red', 'green') #determines max() on the basis of alphabetical order
max(my_tuple) # returns "red"
 
my_tuple = ('abc', 234, 567, 'def') 
max(my_tuple) # throws an error!

# .min(): >>>>>>>>>>>>>>>>>>>>>>>>>>
my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2

my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"

my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!

# .index(): takes value of argument and returns its index
my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

# .count() - takes value to find the number of occurrences
my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1