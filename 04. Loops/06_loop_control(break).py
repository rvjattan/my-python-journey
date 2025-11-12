# "break" is used to terminate the loop if the required condition has been satisfied

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":   # stops look at knit dress
    break

print("End of search!")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Example:

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)      #iterates through the list while printing individual values
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break