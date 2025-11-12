# we can add conditions to list comprehensions:

# Example:

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled)  # prints [-2, -90]

# the above code can be written in list comprehension as:

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

# Example >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ] # 2 conditions applied
print(doubled)

# Example: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [i for i in heights if i > 161]

print(can_ride_coaster)