# .insert() - this method allows us to add an element to a specific index in a list.
# it takes two inputs:  (i) the index you want to insert to
#                       (ii) the element you want to insert at that specific index

# format:     .insert(index, value)

store_line = ["Karla", "Maxium", "Martim", "Isabella"]

# now we need to add Vikor behind Maxim:

store_line.insert(2, "Vikor") # Martim was occupying index 2, so we positioned Vikor at number 2 behind Maxim
print(store_line) #prints Karla, Maxium, Vikor, Martim, Isabella
