#!/bin/python3

import math
import os
import random
import re
import sys

"""
https://www.hackerrank.com/challenges/determining-dna-health/problem
"""
class Trie:
    def __init__(self, parent, value, is_endpoint):
        self.parent = parent
        self.value = value
        self.is_endpoint = is_endpoint
        self.children = [None for _ in range(27)]
        self.counter = 0
    
    def find_child(self, value):
        return self.children[ord(value)-ord('a')]
    def add_child(self, node):
        existing_node = self.find_child(node.value)
        if existing_node is not None:
            existing_node.is_endpoint = existing_node.is_endpoint or node.is_endpoint
            node = existing_node
        else:
            node.parent = self
            self.children[ord(node.value)-ord('a')] = node
        return node
    def print_tree(self, num_spaces):
        print(' '*num_spaces,self.value, "endpoint", self.is_endpoint, 'counter',self.counter)
        for node in self.children:
            if node is not None:
                node.print_tree(num_spaces+2)
    def construct(self, word):
        num_characters = len(word)
        parent = self
        for i, char in enumerate(word):
            node = Trie(parent, char, i == num_characters - 1)
            parent = parent.add_child(node)
        return parent
    def search_and_update(self, word):
        if len(word) == 0:
            return
        elif len(word) == 1:
            character = word
        else:
            character = word[0]
        if self.value == character :
            if self.is_endpoint:
                self.counter += 1
            if len(word) > 1:
                child = self.children[ord(word[1])-ord('a')]   
                if child is not None:
                    child.search_and_update(word[1:])
        if self.value == '$':
            for i, character in enumerate(word):
                child = self.children[ord(character)-ord('a')]
                if child is not None:
                    child.search_and_update(word[i:])
    def zero(self):
        self.counter = 0
        for child in self.children:
            child.zero()

def stringSimilarity(prefix, s):
    s = prefix + '#' + s
    m = len(prefix) + 1
    n = len(s)
    z = [0]*n
    z[0] = n
    lt = 0
    rt = 0
    for i in range(m,n):
        pair_index = i - lt
        if i > rt or z[pair_index] == 0: 
            while z[i] < m and i+z[i] < n and s[i+z[i]] == s[z[i]]:
                z[i]+=1                
            if z[i] > 0:
                rt = i + z[i] - 1
                lt = i
        elif i + z[pair_index] <= rt:
            z[i] = z[pair_index]
        else:
            z[i] =  rt - i + 1 
            while z[i] < m and i+z[i] < n and s[i+z[i]] == s[z[i]]:
                z[i]+=1
            rt = i + z[i] - 1
            lt = i
    z = z[m:]
    #print(prefix, s[m:], z)
    return len([i for i in z if i == m - 1])

if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    
    root = Trie(None, '$', False)
    gene_parents = []
    de_duplicate = {}
    for word in genes:
        gene_parent = de_duplicate.get(word,root.construct(word))
        de_duplicate[word] = gene_parent
        gene_parents.append(gene_parent)
    
    answers = []
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        root.search_and_update(d)
        
        #root.print_tree(1)
        total_value = 0
        for i in range(first, last+1):
            #print(genes[i], gene_parents[i].counter, health[i])
            total_value += gene_parents[i].counter*health[i]
        for gp in gene_parents:
            gp.counter = 0
        #print(total_value)
        answers.append(total_value)
    print(min(answers), max(answers))
            
