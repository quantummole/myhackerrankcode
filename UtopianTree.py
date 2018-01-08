#!/bin/python

import sys
import math

def utopianTree(n):
    if n == 0 :
        return 1
    ans = lambda x : 2*(2**x - 1)
    return ans(n/2+1) if n % 2 else ans(n/2)+1
    
        
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        result = utopianTree(n)
        print result

