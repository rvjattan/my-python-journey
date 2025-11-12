# in "for" loops, the number of iterations are pre-defined, means we already know how many times it needs to run

# format:   for <temporary variable> in <collection>:
#                 <action>

# "for" indicates the start of the loop
# "temporary variable" is used to represent the value of element in the collection the loop is currently on.
# "in" keyword seperates the temporary variable from collection
# "collection" represents a collection of data to loop over
# "action" represent the action needs to be takes on each iteration of loop

# Example:

ingredients = ["Milkshake", "Coffee", "Custard", "Bread Pudding", "Butter Naan", "Sandwich"]

for ingredient in ingredients:
    print(ingredient) # prints each item on a new line

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games:
    print(game)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

sport_games = ["football", "hockey", "baseball", "cricket"]

for sport in sport_games:
    print(sport)
