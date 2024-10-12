#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    l=[0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            l[0]=l[0]+1
        elif a[i]<b[i]:
            l[1]=l[1]+1
    return l

if __name__ == '__main__':
    fptr = open('C:\\Users\\akfla\\Documents\\Programs\\python\\Python\\testpath\\test.txt', 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
