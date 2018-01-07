#!/bin/python

import sys

freq = [0,0,0,0,0]
def migratoryBirds(n, ar):
    for x in ar :
        freq[x-1] += 1
    result = 1
    max_freq = 0
    for (i,f) in enumerate(freq) :
        if f > max_freq :
            result = i+1
            max_freq = f
    return result

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
