#!/bin/python

import sys

def catAndMouse(x, y, z):
    diff_a = abs(x - z)
    diff_b = abs(y - z)
    return "Mouse C" if diff_a == diff_b else ("Cat A" if diff_a <diff_b else "Cat B")
if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print result



