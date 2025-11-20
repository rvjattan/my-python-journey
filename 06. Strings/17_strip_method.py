# .strip() method is used to clean strings, it removes all whitespaces from beginning to end

featuring = "           rob thomas                 "
print(featuring.strip()) # print 'rob thomas'

# using .strip() with a character
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!')) # print 'rob thomas       ' ; does not remove whitespace, it only strips the argument


# Example:

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)