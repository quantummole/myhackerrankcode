#!/bin/python

import sys

def hurdleRace(k, height):
    return max([0,max(height) - k])

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = map(int, raw_input().strip().split(' '))
    result = hurdleRace(k, height)
    print result
