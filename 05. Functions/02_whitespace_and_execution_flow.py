# In Python, the amount of whitespace tells the computer what is part of a function and what is not.

# in below example both print statements run because both have same base level of indentation
def trip_welcome():
  print("Welcome to Vacation House!") 
  print("Let's get you to your destination.")

# to write a new line outside of trip_welcome(), we need need to unindent the new line: >>>>>>>>>>>>>>>>>>

def trip_welcome_new():
  # Indented code is part of the function body
  print("Welcome to Vacation House!") 
  print("Let's get you to your destination.")

# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")

trip_welcome_new()
