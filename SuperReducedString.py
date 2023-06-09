#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    s = input()

flag = True
while flag and s != "":
    flag = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            flag = True
            s = s[:(i)] + s[(i+2):]
            break

if s == "":
    print('Empty String')
else:
    print(s)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
