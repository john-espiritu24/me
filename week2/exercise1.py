"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

#I think this will print the words from the some_wors list
for word in some_words:
    print(word)
#Prints one word on each line from the list

#does the same function as above for 'x' and 'word' are just names
for x in some_words:
    print(x)
#^^

# Prints the whole list
print(some_words)
# Prints the list as a list '[]' included, rather than just the words

# If the length is of a word is > 3 will print the string
if len(some_words) > 3:
    print('some_words contains more than 3 words')
# the string was printed because words longer than 3 characters were found in the list

# 
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
