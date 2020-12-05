# -*- coding: utf-8 -*-

#####
# solution to advent of coding, December 2
#####

"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

# read data from the inputs file
# assumes running from one level up
inputFile = 'dec2/input.txt'

with open(inputFile, 'r') as f:
    inputs = f.read().splitlines()
    f.close()

compliant = 0

for inVal in inputs:
    # pre-process the input line
    inList = inVal.split(' ')
    password = {}
    char = inList[1][0]
    index1 = int(inList[0].split('-')[0])
    index2 = int(inList[0].split('-')[1])
    password = inList[-1]

    char1 = password[index1 - 1]
    char2 = password[index2 - 1]
    if (char1 == char or char2 == char) and not (char1 == char and char2 == char):
        compliant = compliant + 1

print("Number of compliant passwords = {}".format(compliant))