# range() - is used to generate a list of consecutive numbers
# range() takes two inputs, the starting point and the end point (1, 10)
# if we are starting from 0, no need to put zero as input, we can just put the last element of the list (10)
# list is stopped before reaching the maximum input value
# before we use this as a list, we need to convert it using the list() method:

my_range = range(10)
print(my_range) # prints range(0, 10)

# we now need to convert this range object to a list
print(list(my_range)) #prints: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_list = range(2, 9) # 2 to 8
print(list(my_list)) # prints 2, 3, 4, 5, 6, 7, 8

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Skip method: we can use a third input that tells the program to how many numbers to skip
#format:   range(starting value, maximum value, difference value)

my_range2 = range(2, 9, 2) # print from 2 to 9(excluding 9) but skip 2 numbers everytime
print(list(my_range2)) # prints 2, 4, 6, 8


my_range3 = range(1, 100, 10)
print(list(my_range3)) #prints: 1, 11, 21, 31, 41, 51, 61, 71, 81, 91
