# .split() - it is performed on a string, takes one argument and returns a list of sub-strings found between the given argument
# if no argument is given it splits the string at spaces


# syntax -   string_name.split(delimiter) - delimiter is the argument
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#no argument given so string is splitted at spaces

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words) # prints ["The", "sky", "has", "given", "over"]