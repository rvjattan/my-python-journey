# .pop method is used to remove elements at a specific index
# it takes single input, the index of the element we want to remove:

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

#remove "Clowns 101":
cs_topics.pop() #no index input removes the last item
print(cs_topics) #prints Python, Data Structures, Balloon Making, Algorithms

#remove "Balloon Making":
cs_topics.pop(2)
print(cs_topics) # prints Python, Data Structures, Algorithms