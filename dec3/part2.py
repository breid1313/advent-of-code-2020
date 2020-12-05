# -*- coding: utf-8 -*-

#####
# solution to advent of coding, December 3
#####

"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

# read data from the inputs file
# assumes running from one level up
inputFile = 'dec3/input.txt'

with open(inputFile, 'r') as f:
    inputs = f.read().splitlines()
    f.close()

def countTrees(inputs, slopeRight, slopeDown):
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
        row = row + slopeDown
        column = column + slopeRight
    print("Hit {} trees.".format(trees))
    return trees

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

tree_arr = []

for slope in slopes:
    count = countTrees(inputs, slope[0], slope[1])
    tree_arr.append(count)

result = 1
for res in tree_arr:
    result = result * res

print(result)