#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryChildren function below.
def angryChildren(k, n, arr):
    arr = sorted(arr)
    unfairness = 1000000000
    for i,x in enumerate(arr[0:n-k+1]) :
        unfair = arr[i+k-1] - x
        if unfair < unfairness :
            unfairness = unfair
    return unfairness
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = angryChildren(k, n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
