#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr,k):
    n = len(arr)
    p = random.choice(arr)
    if k == 0:
        return min(arr)
    left = []
    right = []
    equals = []
    for i in arr :
        if i < p :
            left.append(i)
        elif i == p :
            equals.append(i)
        else :
            right.append(i)
    l = len(left)
    e = len(equals)
    r = len(right)
    if l <= k - 1 and l + e >= k :
        return p
    elif l > k :
        return findMedian(left,k)
    else  :
        return findMedian(right,k - l -e)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr,n//2+1)

    fptr.write(str(result) + '\n')

    fptr.close()
