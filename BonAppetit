#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    actual = (sum(ar) - ar[k])/2
    difference = b - actual
    return "Bon Appetit" if difference == 0 else difference

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
