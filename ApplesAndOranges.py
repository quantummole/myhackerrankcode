#!/bin/python

import sys

def appleAndOrange(s, t, a, b, apple, orange):
    num_apples = 0
    num_oranges = 0
    for x in apple :
        if s<= a+x <= t :
            num_apples += 1
    for x in orange :
        if s<= b+x <= t :
            num_oranges += 1
    return num_apples,num_oranges

if __name__ == "__main__":
    s, t = raw_input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = raw_input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = raw_input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = map(int, raw_input().strip().split(' '))
    orange = map(int, raw_input().strip().split(' '))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print "\n".join(map(str, result))
