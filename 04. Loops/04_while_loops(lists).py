# we can use while loop to iterate through a list as well

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# while loops needs some form of varaible to keep track of condition
#so we can use len() function
length = len(ingredients) # length of ingredients is 5
index = 0

while index < length:   #checks index against length
    print(ingredients[index])    # prints ingredients with index
    index += 1      # adds 1 to the index

# Example 2: 

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
  print("I am learning about", python_topics[index])
  index += 1