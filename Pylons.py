#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, n, arr):
    i = 0 
    num_generators = 0
    while(i < n) :
        index = -1
        for j in range(max(0,i-k+1),min(n,i+k)) :
            if arr[j] == 1 :
                index = j
        if index == -1 :
            num_generators = -1
            break
        else :
            num_generators += 1
            i = index + k
    return num_generators

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
