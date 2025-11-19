# three methods that can change the casing of the string:
# it does not change the original string but creates a new string


# .lower() - returns the string with all lower characters, 

favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase) # prints 'smooth'

# .title() - returns the string with only first letter of each word changed to uppercase

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed) # prints Spring Storm

# .upper() - return the string with all upper characters

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)