# allows us to quickly combine associated data sets without needing to rely on multi-dimensional lists.
# Example:

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

# using the zip function:
names_and_heights = zip(names, heights) #object is created, not the list, convert object to list

converted_list = list(names_and_heights)
print(converted_list)

#prints [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]

