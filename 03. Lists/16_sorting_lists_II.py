# sorted() method is also used to sort lists
# it generates a new list instead of modifying the existing one
# it comes before a list: sorted(list)

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names) #prints 'Angel', 'Buffy', 'Giles', 'Willow', 'Xander'

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)

print(games) # prints the unsorted list
print(games_sorted) # prints sorted list