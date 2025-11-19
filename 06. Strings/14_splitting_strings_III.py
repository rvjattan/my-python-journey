# we can also split strings using escape sequences.
# Escape Sequences are used to indicate that we want to want split by something in a string that's not necessarily a character.

# \n Newline - allows us to split a multi-line strings by line breaks
# \t Horizontal Tab - allows us to split a string by tabs 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)
