#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()

    min=0
    max=0
    for i in range(len(arr)-1):

        min=min+arr[i]
    print(min,end=" ")
    for j in range(1,len(arr)):

        max=max+arr[j]
    print(max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
