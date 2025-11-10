# to modify a value in a list, reassign the value using the specific index, example:
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries" # replaces "cauliflower with strawberries"
garden[-1] = "Raspberries" # we can also use negative indices: replaces grapes with raspberries

print(garden)

# Example
# a list containing name of customers:
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla" # adds Calla in place of Adam
garden_waitlist[-1] = "Alex" # adds Alex in place of Alisha

print(garden_waitlist)