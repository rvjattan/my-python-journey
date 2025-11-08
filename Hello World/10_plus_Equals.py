# a shorthand for updating variables

#Example 1

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14


# it can also be used for string concatenation

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"


# Practice:

total_price = 0

new_books = 50.00

total_price += new_books

new_jeans = 39.00
new_stickers = 20.00

# Update total_price here:
total_price += new_jeans
total_price += new_stickers

print("The total price is", total_price)