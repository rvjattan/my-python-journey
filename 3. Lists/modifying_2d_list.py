# To change a value in 2d list, we need to reassign the value using the specific index

# Example contains student names and their hobbies: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
print(class_name_hobbies)

# Jenny changed her mind and is now more interested in meditation:
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)


# Negative indices work as well: Grace now likes Chess:
class_name_hobbies[-1][-1] = "Chess"
print(class_name_hobbies)


# Example: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)

#modify Madison's grade to 8:
incoming_class[2][2] = 8
print(incoming_class)

#modify Kenny's name to Ken:
incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Example: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

# add "Medium to preferred_size"
preferred_size.append("Medium")
print(preferred_size)

# create a 2-d list that contains value in ["Name", "Size", Fast_Shipping] format:
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

#change boolean value of Chani from True to False:
customer_data[2][2] = False

# remove boolean value from Ben's list
customer_data[1].remove(False)

# add new sub-lists to the existing list
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)