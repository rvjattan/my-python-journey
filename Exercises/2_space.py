# A program that helps Ryan to keep track of target weight by:
# (i) checking which number planet is equal to 
# (ii) Computing Ryan's weight on the destination planet

# Table of conversion:
#  No.      Planet          Relative Gravity
#   1       Venus           0.91
#   2       Mars            0.38
#   3       Jupiter         2.34
#   4       Saturn          1.06
#   5       Uranus          0.92
#   6       Neptune         1.19

weight = 185
planet = 1

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight is " + str(weight))