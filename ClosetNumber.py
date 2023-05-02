#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()  # sort the array in ascending order
    min_diff = float('inf')  # initialize minimum difference to infinity
    pairs = []  # initialize empty list of pairs
    
    # find the minimum difference between adjacent elements
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
            pairs = [(arr[i], arr[i+1])]
        elif diff == min_diff:
            pairs.append((arr[i], arr[i+1]))
    
    # flatten the list of pairs and return it as a single list
    return [num for pair in pairs for num in pair]

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
