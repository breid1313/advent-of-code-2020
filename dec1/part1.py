# -*- coding: utf-8 -*-

#####
# solution to advent of coding, December 1
#####

# read data from the inputs file
# assumes running from one level up
inputFile = 'dec1/input.txt'
with open(inputFile, 'r') as f:
    inputs = f.read().splitlines()
    f.close()

# cast the values to integers
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

for i in inputs:
    target = 2020 - i
    if target in inputs:
        print("Solution found: {} + {} = {} with product {}".format(i, target, i + target, i * target))
