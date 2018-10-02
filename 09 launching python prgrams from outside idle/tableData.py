#!/usr/bin/python3.4

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
    ['Alice', 'Bob', 'Carol', 'David',],
    ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
        colWidths = [0] * len(table)
        for w in range(len(table[0])):
            for l in range(len(table)):
                if len(table[l][w]) > colWidths[l]:
                    colWidths[l] = len(table[l][w])
        print(colWidths)

        for x in range(len(table[0])):
          for y in range(len(table)):
              print(table[y][x].rjust(colWidths[y] + 1), end = '')
          print()
printTable(tableData)
