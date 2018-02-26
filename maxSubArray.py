#!/bin/python

import sys

def maxSubarray(arr):
    # Complete this function
    prev_best = arr[0]
    residue = arr[0]
    min_neg = arr[0]
    max_sum_positive = max([0,arr[0]])
    for ele in arr[1:] :
        if ele > 0 :
            max_sum_positive += ele
        else :
            if min_neg < ele :
                min_neg = ele
        
        residue = max([residue+ele,ele])
        prev_best = max([prev_best,residue])

    sum_subsequence = max_sum_positive if max_sum_positive > 0 else min_neg
    sum_subarray = prev_best if prev_best > 0 else min_neg
    return sum_subarray,sum_subsequence
    
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = maxSubarray(arr)
        print " ".join(map(str, result))
