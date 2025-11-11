# .sort() - is used to sort a list in either alphabetical or numerical order:
# it modifies the list directly and doesn't need a variable

names_1 = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names_1.sort()
print(names_1) # prints 'Angel', 'Buffy', 'Giles', 'Willow', 'Xander'

# we can also do reverse sorting:
names_2 = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names_2.sort(reverse=True)
print(names_2) # prints ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)


names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()

# sorting in reverse
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)