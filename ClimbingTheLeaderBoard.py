#!/bin/python

import sys

def climbingLeaderboard(n,m,scores, alice):
    curr = 0
    output = []
    for i,j in enumerate(scores[-1::-1]) :
        while curr<m  and alice[curr] < j :
            output.append(n-i+1)
            curr += 1
    for i in range(curr,m) :
        output.append(1)
    return output

if __name__ == "__main__":
    n = int(raw_input().strip())
    scores = map(int, raw_input().strip().split(' '))
    scores_unique = [scores[0]]
    unique = 1
    for i in scores[1:] :
        if not scores_unique[-1] == i :
            scores_unique.append(i)
            unique+=1
    m = int(raw_input().strip())
    alice = map(int, raw_input().strip().split(' '))
    result = climbingLeaderboard(unique,m,scores_unique, alice)
    print "\n".join(map(str, result))


