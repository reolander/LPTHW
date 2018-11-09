#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0; valleys = 0; mountains = 0
    for character in s:
        if sea_level == -1 and character == 'U':
            valleys += 1
        elif sea_level == 1 and character == 'D':
            mountains += 1
            
        if character == 'U':
            sea_level += 1
        elif character == 'D':
            sea_level -= 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
