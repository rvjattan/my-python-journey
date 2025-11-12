# "continue" is used to skip the current iteration and proceed to the next iteration of the loop

# Example: print only positive integer

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
    if i <= 0:
        continue        # skips the current iteration if i <= 0
    print(i)

# Example 2: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:      # checks if age is less than 21
    continue        # skip the current iteration if age is less than 21
  print(age)
  