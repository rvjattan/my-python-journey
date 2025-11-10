# list methods are used to create, manipulate and even delete data within the list:

# (i) .append() - it allows us to add an element at the end of the list

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')

print(append_example) # append_example = ['This', 'is', 'an', 'example', 'list']

# (ii) Plus(+) - When we need to add multiple items to a list

items_sold = ["cake", "cookie", "bread"] # if we want to add item to this:
items_sold_new = items_sold + ["biscuits", "coffee"] # prints ['cake', 'cookie', 'bread', 'biscuits', 'coffee']

my_list = [1, 2, 3, 4]
my_list_new = my_list + [5, 6] # prints [1, 2, 3, 4, 5, 6]
