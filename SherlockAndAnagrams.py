#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    count = 0  # Initialize count to 0
    for i in range(1, len(s)):  # Loop through all possible substring lengths
        substrings = {}
        for j in range(len(s)-i+1):  # Loop through all substrings of length i
            substring = ''.join(sorted(s[j:j+i]))
            if substring in substrings:
                count += substrings[substring]
                substrings[substring] += 1
            else:
                substrings[substring] = 1
    return count

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
