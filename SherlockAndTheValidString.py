#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    counts = Counter(s)
    values = list(counts.values())
    values_dict = {} 
    for count in values :
        if not count in values_dict :
            values_dict[count]=[1,count]
        else :
            p,_ = values_dict[count]
            values_dict[count] =  [p+1,count]
    all_values = list(values_dict.values())
    if len(all_values) == 1 :
        return 'YES'
    elif len(all_values) > 2 :
        return 'NO'
    elif (all_values[0][0] == 1 and (all_values[0][1] == all_values[1][1] + 1 or all_values[0][1]==1 )) or (all_values[1][0] == 1 and (all_values[1][1] == all_values[0][1] + 1 or all_values[1][1]==1)) :
        return 'YES'
    else :
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
