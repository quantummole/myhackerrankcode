#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
# https://www.hackerrank.com/challenges/crush/problem

class TreeNode:
    def __init__(self, a, b, v):
        self.left = a
        self.right = b
        self.value = v
        self.left_interval = None
        self.right_interval = None
        self.between_interval = None
        self.max_val = v
    def add_node(self, a,b, v):
        if b < self.left:
            if self.left_interval is None:
                self.left_interval = TreeNode(a,b,v)
            else:
                self.left_interval.add_node(a,b,v)
        elif a > self.right:
            if self.right_interval is None:
                self.right_interval = TreeNode(a,b,v)
            else:
               self.right_interval.add_node(a,b,v)
        elif a > self.left and b < self.right:
            if self.between_interval is None:
                self.between_interval = TreeNode(a,b,v)
            else:
                self.between_interval.add_node(a,b,v)
        else:
            intervals = [[a,self.left-1, 'left'], [max(a,self.left), min(b,self.right),'between'], [self.right+1,b, 'right']]
            intervals = [i for i in intervals if i[0]<=i[1]]
            #print(intervals)
            for a, b, typ in intervals:
                if typ == 'left':
                    if self.left_interval is None:
                        self.left_interval = TreeNode(a,b,v)
                    else:
                        self.left_interval.add_node(a,b,v)
                if typ == 'right':
                    if self.right_interval is None:
                        self.right_interval = TreeNode(a,b,v)
                    else:
                        self.right_interval.add_node(a,b,v)
                if typ == 'between':   
                    if a == self.left and b == self.right:
                        self.value = self.value + v  
                    elif self.between_interval is None:
                        self.between_interval = TreeNode(a,b,v)
                    else:
                        self.between_interval.add_node(a,b,v)
        self.max_val = self.fetch_max_value()
        
    def fetch_max_value(self):
        between_val = self.value
        if self.between_interval is not None:
            between_val += self.between_interval.max_val
        left_val = 0
        if self.left_interval is not None:
            left_val = self.left_interval.max_val
        right_val = 0
        if self.right_interval is not None:
            right_val = self.right_interval.max_val
        return max(between_val, left_val, right_val)
    def print(self, num_spaces):
        print(' '*num_spaces,self.left, self.right, self.value, self.max_val)
        if self.left_interval is not None:
            self.left_interval.print(num_spaces+2)        
        if self.right_interval is not None:
            self.right_interval.print(num_spaces+2)        
        if self.between_interval is not None:
            self.between_interval.print(num_spaces+2)        

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    max_val = 0
    root = None
    for (i,j,v) in queries:
        if root is None:
            root = TreeNode(i,j,v)
        else:
            root.add_node(i,j,v)
    #root.print(1)
    return root.max_val
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
