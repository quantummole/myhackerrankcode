#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
def get_insertion_shift(arr):
    n = len(arr)
    if n == 0  :
        return 0,arr
    elif n == 1 :
        return 0, arr
    elif n == 2 :
        if arr[0] > arr[1] :
            return 1, [arr[1],arr[0]]
        else :
            return 0,arr
    else :
        m = n//2
        shiftl,left = get_insertion_shift(arr[0:m])
        shiftr,right = get_insertion_shift(arr[m:])
        lleft = len(left)
        lright = len(right)
        if lleft == 0 :
            return shiftr,right
        if lright == 0 :
            return shiftl,left
        i=0
        j = 0
        shiftm = 0
        arr = [None]*n
        for k in range(n) :
            if i == lleft :
                arr[k] = right[j]
                j += 1
            elif j == lright :
                arr[k] = left[i]
                i += 1
            elif left[i] <= right[j] :
                arr[k] = left[i]
                i = i+1
            else :
                arr[k] = right[j]
                j = j +1
                shiftm += lleft - i
        return shiftl+ shiftr+shiftm,arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = get_insertion_shift(arr)[0]

        fptr.write(str(result) + '\n')

    fptr.close()
