#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#



def get_longest_prefix(reference, offset, start, stop):
    prefix_len = stop - start - offset 
    if prefix_len == 0:
        return 0
    elif prefix_len == 1:
        if reference[start] == reference[start+offset]:
            return 1
        else:
            return 0
    elif prefix_len == 2:
        if reference[start] == reference[start+offset]:
            if reference[start+1] == reference[start+offset+1]:
                return 2
            else:
                return 1
        else:
            return 0
    elif not reference[start] == reference[start+offset]:
        return 0
    else:
        index = prefix_len//2
        lindex = get_longest_prefix(reference, offset, start, start+offset+index)
        if not reference[start+index] == reference[start+offset+index]:
            return lindex
        else:
            if not lindex == index:
                return  lindex
            else:
                rindex = get_longest_prefix(reference, offset, start+index+1, stop)
                return lindex + 1 + rindex
    
def stringSimilarity_Recursion(s):
    strlen = len(s)
    answer = 0
    for p in range(strlen):
        temp = get_longest_prefix(s, p, 0, strlen)
        answer += temp
    return answer
    
def stringSimilarity(s):
    n = len(s)
    z = [0]*n
    z[0] = n
    lt = 0
    rt = 0
    for i in range(1,n):
        pair_index = i - lt
        if i > rt or z[pair_index] == 0: 
            while i+z[i] < n and s[i+z[i]] == s[z[i]]:
                z[i]+=1                
            if z[i] > 0:
                rt = i + z[i] - 1
                lt = i
        elif i + z[pair_index] <= rt:
            z[i] = z[pair_index]
        else:
            print(i,z[pair_index],lt,rt)
            z[i] =  rt - i + 1 
            while i+z[i] < n and s[i+z[i]] == s[z[i]]:
                z[i]+=1
            rt = i + z[i] - 1
            lt = i
    print(z)
    return sum(z)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
