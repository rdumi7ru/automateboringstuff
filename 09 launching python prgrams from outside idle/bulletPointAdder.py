#!/usr/bin/python3.4
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of the text on the clipboard.
import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)


# Example:
# print("* " + "\n* ".join("foo\nbar\nbaz".splitlines()))

# Copied text
'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''
