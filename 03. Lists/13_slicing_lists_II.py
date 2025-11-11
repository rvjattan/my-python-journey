# we can format like: list[:n], empty first value start from zero and goes till the other value
# on the contrary; list[n:], if last value is empty, the list goes till the last element

# we can also use negative indexing:
# list[-2:] prints last two elements of the list
# list[:-2] prints all elements except the last two elements

#Example

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
print(fruits[:3]) # prints "apple", "cherry", "pineapple"
print(fruits[2:]) # prints pineapple", "orange", "mango"

print(fruits[-2:]) # prints "orange", "mango"
print(fruits[:-2]) # prints "apple", "cherry", "pineapple"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Example

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
 
last_two_elements = suitcase[-2:]
print(last_two_elements) # prints "pajamas", "books"

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three) #prints shirt", "shirt", "pants"