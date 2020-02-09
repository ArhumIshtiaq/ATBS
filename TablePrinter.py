
def printTable(table):
	colWidths = [0] * len(table)
	ll = len(table)
	lol = len(table[0])
	for i in range(ll):
		for x in table[i]:
			if (colWidths[i] < len(x)):
				colWidths[i] = len(x)

	for i in range(lol):
		for x in range(ll):
			print(table[x][i].rjust(colWidths[x]), end=" ")
		print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)