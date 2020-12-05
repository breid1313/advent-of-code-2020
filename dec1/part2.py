# -*- coding: utf-8 -*-

#####
# solution to advent of coding, December 1
#####

"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""

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
    tmp = list(inputs)
    tmp.remove(i)
    for j in tmp:
        target2 = target - j
        if target2 in tmp:
            print("Solution found: {} + {} + {} = {} with product {}".format(i, j, target2, i + j + target2, i * j * target2))