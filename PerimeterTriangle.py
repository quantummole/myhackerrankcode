#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks = sorted(sticks)[::-1]
    a = sticks[0]
    b = sticks[1]
    c = 0
    for i in sticks[2:] :
        if b + i > a :
            c = i
            break
        else :
            a = b
            b = i
    if c == 0 :
        return [-1]
    else :
        return [c,b,a]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
