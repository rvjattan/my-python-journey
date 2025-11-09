# when applied to any boolean expression, it reverses the value

# example:

not 1 + 1 == 2  # False
not 7 < 0       # True

# example:

not (4 + 5 <= 9)        # False

not (8 * 2) != 20 - 4   # True

# example:

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.") 
if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")    # prints this
