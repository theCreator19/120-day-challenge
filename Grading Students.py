# Grading Students

# Hackerrank Problem solved using Python.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    g=grades
    for i in range(grades_count):
        if ((g[i]+1) %5==0 and (g[i]+1)>=40):
            
            g[i]+=1
        if((g[i]+2)%5==0 and (g[i]+2)>=40):
            
            g[i]+=2
    return g

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
