#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

if __name__ == '__main__':
    n = int(input().strip())

    arr = [None]*100

    for i in range(n):
        x,y = input().rstrip().split()
        x = int(x)
        if arr[x] is not None :
            if i < n//2 :
                arr[x].append('-')
            else :
                arr[x].append(y)
        else :
            arr[x] = []
            if i < n//2 :
                arr[x].append('-')
            else :
                arr[x].append(y)
    arr = [i for i in arr if not i is None]
    print(" ".join(reduce(lambda x,y:x+y,arr)))        
