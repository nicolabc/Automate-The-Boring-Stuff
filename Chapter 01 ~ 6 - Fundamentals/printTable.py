#! python3
import sys

#print('Remember, remember, the fifth of November.'.split())
#print('-'.join('There can be only one.'.split()))

def printTable(table):

    #Find the max num of characters for each column
    maxLenghtCol = []
    for i in range(len(table)):
        maxLenghtCol.append(len(max(table[i],key=len)))

    #iterate over the list assuming that it is square (same length for inner and outer list). Then print it right justed with the
    # corresponding width of max length of characters for each column.
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(maxLenghtCol[j],' '),end=' ')
        print('')

    return 0

def printTable2(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)
    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
	    for j in range(len(inputList[i])):
		    if len(inputList[i][j]) > colWidths[i]:
			    colWidths[i] = len(inputList[i][j])

    '''
    #My solution:
    maxLenghtCol = []
    for i in range(len(inputList)):
        maxLenghtCol.append(len(max(inputList[i], key=len)))'''

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for x in range(len(inputList[0])):
	    for y in range(len(inputList)):
		    print(inputList[y][x].rjust(colWidths[y]), end = ' ')
	    print('')


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)
    print('\n')
    printTable2(tableData)

    #print("No problem", end='\n')
    sys.exit()