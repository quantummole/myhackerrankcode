#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    pairs = []
    arr = sorted(arr)
    n = len(arr)
    min_diff = arr[n-1]-arr[0]+5
    for i in range(1,n) :
        diff = arr[i]-arr[i-1]
        if diff < min_diff :
            pairs = [arr[i-1],arr[i]]
            min_diff = diff
        elif diff == min_diff :
            pairs.append(arr[i-1])
            pairs.append(arr[i])
        else :
            pass
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
