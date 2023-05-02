#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
def countSort(arr):
    counts = [0] * 100

    # Count the frequency of each number
    for i in range(len(arr)):
        counts[int(arr[i][0])] += 1

    # Calculate the cumulative counts
    for i in range(1, 100):
        counts[i] += counts[i-1]

    # Build the sorted array
    sorted_arr = [''] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        index = counts[int(arr[i][0])] - 1
        sorted_arr[index] = arr[i][1] if i >= len(arr) // 2 else '-'
        counts[int(arr[i][0])] -= 1

    sorted_arr = ' '.join(sorted_arr)
    print(sorted_arr)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
