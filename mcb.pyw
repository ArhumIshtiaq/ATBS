#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import sys, pyperclip, shelve, json

c = sys.argv[1]
if (len(sys.argv) == 3):
	f = sys.argv[2]

mcbShelf = shelve.open('mcbData')

if (c == "save"):
	p = pyperclip.paste()
	mcbShelf[f] = p
	print("Your data has been saved to the keyword", f)

elif (c == "list"):
	pyperclip.copy(mcbShelf)
	print("All your data has been copied to your clipboard.")

else:
	try:
		pyperclip.copy(mcbShelf[c])
		print("All your data related to the keyword",c,"has been copied to your clipboard.")

	except KeyError:
		print("Sorry the keyword does not exist, try saving something to it and then try again.")

print(mcbShelf)

mcbShelf.close()
