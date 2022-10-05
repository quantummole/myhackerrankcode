#!/bin/python3

import sys

def get_max_multiples(N,a):
    if N < a:
        answer = 0
    else:
        N = N if N % a > 0 else N-1
        answer = (N-a)//a + 1
    return answer

def sum_multiples(N,a):
    return N*a + N*(N-1)*a//2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_3 = sum_multiples(get_max_multiples(n,3),3)
    sum_5 = sum_multiples(get_max_multiples(n,5),5)
    sum_15 = sum_multiples(get_max_multiples(n,15),15)
    answer = sum_3 + sum_5 - sum_15
    print(answer)
    
