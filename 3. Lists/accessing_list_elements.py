# the location of an element in a list is called its index
# Python lists are zero-indexed means they start from 0
# Example: in a list "call" that contains name of students:

call = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]

#   Element	    Index
#   "Juan"	    0
#   "Zofia"	    1
#   "Amare"	    2
#   "Ezio"	    3
#   "Ananya"	4

# to print the name Zofie:

print(call[1])


# Accessing list elements using negative index:

# We can use [-1] to select the last item of the list, example:
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
print(pancake_recipe[-1]) # prints love
