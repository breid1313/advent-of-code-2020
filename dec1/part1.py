# -*- coding: utf-8 -*-

#####
# solution to advent of coding, December 1
#####

"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
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
    if target in inputs:
        print("Solution found: {} + {} = {} with product {}".format(i, target, i + target, i * target))
