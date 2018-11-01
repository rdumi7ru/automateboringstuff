#!/usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python3.4 mcb_extendet.pyw save <keyword> - Saves clipboard to keyword.
#        python3.4 mcb_extendet.pyw <keyword> - Loads keyword to clipboard.
#        python3.4 mcb_extendet.pyw list - Loads all keywords to clipboard.
#        python3.4 mcb_extendet.pyw del - Delete's the key that you enter

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard 
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # List keywords, load content, and delete key.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'del':
        # Get the key that will be deleted.
        key = input(('Enter the keyword you want do delete:\n'))
        del mcbShelf[key]
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()


# I also could use:
#elif sys.argv[1].lower() == 'delete':
#        for k in list(mcbShelf.keys()):
#            del mcbShelf[k]
