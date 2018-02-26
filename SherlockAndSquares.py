#!/bin/python

import sys
import math

def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))
    return int(y - x + 1)

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        a, b = raw_input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print result
