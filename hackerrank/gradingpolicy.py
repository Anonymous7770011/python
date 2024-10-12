#!/bin/python3

import math
import os
import random
import re
import sys



def gradingStudents(grades):
    t=[]
    for i in grades:
        if i<=33:
            t.append(i)
        else:
            s=i//5
            s=s+1
            t.append(i if (s*5)-i>=3 else (s*5))
    return t
if __name__ == '__main__':
    fptr = open('C:\\Users\\akfla\\Documents\\Programs\\python\\Python\\testpath\\test.txt', 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
