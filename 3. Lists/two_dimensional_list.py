# A list that contain other lists is known as 2-D list

# Example:      #Noelle is 61 inches tall
                #Ava is 70 inches tall
                #Sam is 67 inches tall
                #Mia is 64 inches tall
# We can create a list that contain  both names and height:

heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

#accessing 2d list:

#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)


# Example

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

sams_score = class_name_test[2][1]
print(sams_score)

# using negative index
ellies_score = class_name_test[-1][-1]
print(ellies_score)