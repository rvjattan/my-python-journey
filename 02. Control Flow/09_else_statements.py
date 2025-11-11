# else statements always appear in conjunction with if statements.
# else statements allows us to describe what we want our code to do if certain conditions are not met.

# example
age = 17

if age >= 13:
  print("Access granted.") # prints this as condition is true
else:
  print("Sorry, you must be 13 or older to watch this movie.")

# example
credits = 132
gpa = 3.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!") # prints this as both the conditions are satisfied.
else:
  print("You do not meet the requirements to graduate.")