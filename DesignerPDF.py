#!/bin/python

import sys

def designerPdfViewer(h, word):
    init = ord('a')
    ht = max(map(lambda y : h[ord(y) - init],word))
    return ht*len(word)

if __name__ == "__main__":
    h = map(int, raw_input().strip().split(' '))
    word = raw_input().strip()
    result = designerPdfViewer(h, word)
    print result
