# "or" combines two expressions into one larger expression that is True if either component is true

# example

True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

# example:

(2 - 1 > 3) or (-5 * 2 == -10)     # True
(9 + 5 <= 15) or (7 != 4 + 3)      # True

# example:

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")