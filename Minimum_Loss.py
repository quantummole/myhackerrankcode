#!/bin/python3

import math
import os
import random
import re
import sys


class BST :
    def __init__(self, node) :
        self.node = node
        self.left = None
        self.right = None
        self.diff = 1e21
    def leaf(self) :
        return self.diff is None
# Complete the minimumLoss function below.

def insert_node(root,node) :
    min_val = 1e+21
    if node >  root.node and root.right is None:
        root.right = BST(node)                                                       
        minna = root.diff
    elif node > root.node :
        minna = insert_node(root.right,node)
    elif root.left is None :
        root.left = BST(node)
        root.diff = min(root.diff,abs(node - root.node))
        minna = root.diff
    else :
        root.diff = min(root.diff,abs(root.node - node))
        minna = min(root.diff,insert_node(root.left,node))
    return min(min_val,minna) 


def display(root) :
    print(root.node,root.diff)
    if root.left is not None :
        display(root.left)
    if root.right is not None :
        display(root.right)
    
def minimumLoss(price):
    min_val = 1e21
    root = BST(price[0])
    for x in price[1:] :
        minna = insert_node(root,x)
        min_val = min(min_val,minna)
    return min_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
