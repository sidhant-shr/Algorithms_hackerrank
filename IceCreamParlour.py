#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Create a dictionary to store the ice cream flavors and their indices
    flavors = {}
    for i in range(len(arr)):
        if m - arr[i] in flavors:
            # If the complement flavor is in the dictionary, return its index and the current index
            return (flavors[m - arr[i]] + 1, i + 1)
        else:
            # Otherwise, add the current flavor and its index to the dictionary
            flavors[arr[i]] = i
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
