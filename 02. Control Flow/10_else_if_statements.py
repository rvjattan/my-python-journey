# else if statements or commonly known as "elif" statements
# an "elif" statement check other conditions after the previous "if" conditions are not met.

# example
donation = 2000
print("Thank you for the donation!")

if donation >= 1000:
  print("You've achieved platinum status")  #prints this
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")

# example

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:   #prints this
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")