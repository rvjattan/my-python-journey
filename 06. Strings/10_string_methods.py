# string methods allow us to perform various functions on a string:

print("Hello World".upper())  # changes the alphabets to upper case

print(" ".join(["Hello", "World"])) # joins the strings given as argument

print("Hello World".lower()) # changes the alphabets to lower case

print("Hello World".replace("H", "J"))  # replaces the H(first argument) with J(second argument)

print("hello world".title()) # changes the first alphabet of the words to uppercase

print("    Hello World     ".strip()) # strips the string of the unnecessary spaces

print("Hello World".split()) # splits the string into a list containing 2 words: ['Hello', 'World']

print("{} {}".format("Hello", "World")) # prints the parameter strings as necessary