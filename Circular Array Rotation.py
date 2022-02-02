# Circular Array Rotation

# HackerRank Problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    
    m=len(a)
    l=[]
    l2=[]
    if(k>m):
        k=k%m
    k1=m-k+1
    m1=len(queries)
    for i in range(k1-1,m):
        l.append(a[i])        
    for j in range(k1-1):
        l.append(a[j])
    for i in range(m1):
        s=queries[i]
        t=l[s]
        print(t)
        l2.append(t)
    return l2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
