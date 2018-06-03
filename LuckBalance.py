#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(n, k, contests):
    important_contests = []
    total_luck = 0
    for x,y in contests :
        if y == 1 :
            important_contests.append(x)
        else :
            total_luck += x
    important_contests = sorted(important_contests)[::-1]
    return total_luck + sum(important_contests[0:k]) - sum(important_contests[k:])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(n, k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
