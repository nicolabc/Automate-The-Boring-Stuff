#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
newline = []
for i in range(len(lines)):         # loop through all indexes for "lines" list
    #lines[i] = '* ' + lines[i]     # add star to each string in "lines" list
    if lines[i].startswith('List'): # Add star only to lines starting with 'List'
        newline.append('* ' + lines[i])


text = '\n'.join(newline)
pyperclip.copy(text)
#print(text)
