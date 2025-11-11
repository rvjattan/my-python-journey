# .count() is used to count the occurrences of an item in a list

# Example:

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i) # prints 4 because i appears 4 times in the list

# using .count in a 2-D list:

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs) # prints 2


# Example:

votes = ["p1", "p2", "p1", "p3", "p1", "p2", "p1", "p1"] 
p1_votes = votes.count("p1")
print(p1_votes) #prints 5