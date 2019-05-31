 #! python3
    # mcb.pyw - Saves and loads pieces of text to the clipboard.
    # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
    #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
    #        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

if __name__ == '__main__':
    mcbShelf = shelve.open('mcb')

    # TODO: Save clipboard content.
    ## Save clipboard content.
    #If the first command line argument (which will always be at index 1 of the sys.argv list) is 'save'
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()               #Store the clipboard value at the input argument
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
    mcbShelf.close()
    sys.exit()