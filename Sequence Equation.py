# Sequence Equation

# HackerRank Problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    dict={
        
    }
    j=1
    for i in p:
        dict[i]=j
        j+=1
    ar=[]
    for k in range(1,n+1):
        ar.append(dict[k])
    arr=[]
    for i in ar:
        q=(p.index(i))+1
        
        arr.append(q)
    return arr

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
