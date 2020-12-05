# -*- coding: utf-8 -*-

#####
# solution to advent of coding, December 2
#####

"""
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
"""

# read data from the inputs file
# assumes running from one level up
inputFile = 'dec3/input.txt'

with open(inputFile, 'r') as f:
    inputs = f.read().splitlines()
    f.close()

bottom = len(inputs)
numColumns = len(inputs[0])

row = 0
column = 0

trees = 0

while row <= bottom - 1:
    # check for a tree
    columnMod = column % numColumns
    if inputs[row][columnMod] == "#":
        trees = trees + 1
    row = row + 1
    column = column + 3
print("Hit {} trees.".format(trees))
    