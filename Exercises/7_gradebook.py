# learning lists through exercise:

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Step 1: putting all the subjects in a list:
subjects = ['physics', 'calculus', 'poetry', 'history'] 

# Step 2: putting the grades in a list:
grades = [98, 97, 85, 88]

#Step 3: 2d list of subjects and grades:
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#Step 4: using .append() add computer science grades:
gradebook.append(["computer science", 100])

#Step 5: add visual arts grade:
gradebook.append(["visual arts", 93])

#Step 6: modify visual arts grade:
gradebook[-1][-1] = 98

# Step 7: remove poetry grade:
gradebook[2].remove(85)

# Step 8: add a new Pass value to poetry:
gradebook[2].append("Pass")

# Step 9: combining two lists:
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)