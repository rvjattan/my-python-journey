# "while" loops are a form of indefinite iteration
# a "while" loop performs a certain fuction as long as the given condition is true

# structure: while <conditional statement>:
#                 <action>

# Example: (Working of a while loop)

count = 0       # declare a variable with value 0

while count <= 3:       #the loop check the condition, if variable count is less than or equal to zero
  # Loop Body
  print(count)          #variable count keeps printing
  count += 1            #after printing loop it adds 1 to the count variable and loop restarts again

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Example: While Loop

count = 0
print("Starting While Loop")

while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Example:

countdown = 10

while countdown >= 0:
  print(countdown) # prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 0
  countdown -= 1
print("We have liftoff") #prints at last "We have liftoff"