# adding conditional statements inside iterations:

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)


# Example:

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True

  return False

print(letter_check("banana", "n")) # prints True