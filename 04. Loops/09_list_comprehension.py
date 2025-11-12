# List comprehension is an alternative of writing loops
# more concise syntax for creating lists based on existing iterables (like lists, tuples, or ranges).

# Example:

numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)

# in list comprehension we can write the same loop like:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)


# Example >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)
