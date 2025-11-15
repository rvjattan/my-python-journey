# because strings are lists, it means we can iterate through a string using a "for" loop or "while" loop

def print_each_word(word):
    for letter in word:
        print(letter)

company = "Samsung"
print_each_word(company)

# getting length of a string:

def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

samsung = get_length("Samsung")
print(samsung) #prints 7